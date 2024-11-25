"""

(c)Peharge

"""

import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
from PyQt5.QtGui import QImage
import soundfile as sf
import whisper
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
from PyQt5.QtGui import QPainterPath, QRegion
from PyQt5.QtCore import QRectF
import ollama
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPen
import datetime
from PIL import Image
import psutil
import cv2
import logging
import sounddevice as sd
from PyQt5.QtWidgets import QGroupBox, QFormLayout, QSlider, QMessageBox, QComboBox
import torch
import tensorflow as tf
import pandas as pd
import pygame
import numpy as np
from transformers import __version__ as transformers_version
import time
import os
import ctypes
from PyQt5.QtWidgets import QScrollArea,QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QImageReader, QPainter, QBrush, QColor, QLinearGradient
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QProgressBar, QFrame
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtSvg import QSvgWidget
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl


class AudioThread(QThread):
    audio_signal = pyqtSignal(np.ndarray)

    def run(self):
        try:
            fs = 16000  # Sample rate
            recording_duration = 5  # Record for 5 seconds to test
            print("Recording for 5 seconds...")
            recording = sd.rec(int(recording_duration * fs), samplerate=fs, channels=1, dtype='float32')
            sd.wait()  # Wait until recording is finished

            print("Recording finished.")
            self.audio_signal.emit(np.squeeze(recording))  # Send the recorded audio

        except Exception as e:
            logging.error(f"Error in AudioThread: {e}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start_listening()

    def start_listening(self):
        try:
            # Start the audio thread to record
            self.audio_thread = AudioThread()
            self.audio_thread.audio_signal.connect(self.process_audio)
            self.audio_thread.start()

            # Capture image immediately
            self.image_path = self.capture_image()

        except Exception as e:
            print(f"Error in start_listening: {e}")

    def capture_image(self):
        try:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                raise Exception("Could not open video device")

            ret, frame = cap.read()
            if not ret:
                raise Exception("Could not read frame")

            cap.release()

            current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            image_path = f"img/image_{current_time}.png"
            cv2.imwrite(image_path, frame)
            return image_path
        except Exception as e:
            print(f"Error in capture_image: {e}")
            return ""

    def process_audio(self, audio):
        try:
            # Check if audio was recorded
            if audio is None or len(audio) == 0:
                print("No audio data received.")
                return

            print("Processing audio with Whisper...")
            result = model.transcribe(audio, fp16=False)
            text = result["text"]
            print(f"Transcribed Text: {text}")

            if not self.image_path:
                print("No image captured.")
                return

            # Send text and image to LLava
            res = ollama.chat(
                model="llava:7b",
                messages=[{
                    'role': 'user',
                    'content': text,
                    'images': [self.image_path]
                }]
            )

            llama_output = res['message']['content']
            print(f"LLava Output: {llama_output}")

            # Process with TTS and play
            self.process_with_professional_tool(llama_output.strip())

        except Exception as e:
            print(f"Error in process_audio: {e}")

    def process_with_professional_tool(self, text_output, language="en"):
        try:
            if language == "en":
                model_name = "tts_models/en/ljspeech/vits" #tts_models/en/ljspeech/glow-tts // tts_models/en/ljspeech/vits // Nicht installiert: tts_models/en/ljspeech/fastspeech2 // tts_models/en/ljspeech/tacotron2_wavenet
            elif language == "de":
                model_name = "tts_models/de/thorsten/tacotron2-DCA" #tts_models/de/thorsten/tacotron2-DCA

            tts = TTS(model_name=model_name, progress_bar=False, gpu=False)
            current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            output_filename = f"output_{current_time}.wav"
            tts.tts_to_file(text=text_output, file_path=output_filename)

            config = XttsConfig()
            config.load_json(os.path.join("xtts-v2", "config.json"))
            xtts_model = Xtts(config)
            xtts_model.load_checkpoint(config, checkpoint_dir="xtts-v2", eval=True)

            speaker_wav_path = os.path.join("marsorbit-79697.mp3")

            if not os.path.exists(speaker_wav_path):
                raise FileNotFoundError(
                    f"Die Datei {speaker_wav_path} existiert nicht. Bitte überprüfen Sie den Pfad und versuchen Sie es erneut.")

            outputs = xtts_model.synthesize(
                text_output,
                config,
                speaker_wav=speaker_wav_path,
                gpt_cond_len=3,
                language="en",
            )

            output_file = f"output_{current_time}_xtts.wav"
            if "wav" in outputs.keys():
                sample_rate = config.audio['sample_rate']
                with sf.SoundFile(output_file, "w", samplerate=sample_rate, channels=1) as file:
                    file.write(outputs["wav"])
                logging.info(f"Die Audiodatei wurde erfolgreich gespeichert unter: {output_file}")

                pygame.mixer.init()
                pygame.mixer.music.load(output_file)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

            else:
                raise KeyError("Output dictionary does not contain 'wav'")

            if os.path.exists(output_filename):
                os.remove(output_filename)

            if os.path.exists(output_file):
                os.remove(output_file)

        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
        except KeyError as e:
            print(f"KeyError: {e}")
        except Exception as e:
            print(f"Error in process_with_professional_tool: {e}")



if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        model = whisper.load_model("medium.en")  # Load Whisper model
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
        print("exit")  # Print exit message at the end
    except Exception as e:
        print(f"Error in main execution: {e}")