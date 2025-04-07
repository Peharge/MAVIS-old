#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <command>\n", argv[0]);
        return 1;
    }

    // Concatenate all arguments into a single command string
    char command[1024] = {0};
    for (int i = 1; i < argc; ++i) {
        strcat(command, argv[i]);
        if (i < argc - 1) {
            strcat(command, " ");
        }
    }

    // Prepend the WSL execution command
    char wsl_command[1064] = "wsl -e ";
    strcat(wsl_command, command);

    // Execute the command and capture the output
    int result = system(wsl_command);

    return result;
}