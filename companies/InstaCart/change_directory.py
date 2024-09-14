from typing import List


def change_directory(commands: List[str]) -> str:
    """
    Simulates the change directory command and returns the absolute path from the root.

    Args:
        commands (List[str]): A list of cd commands to process.

    Returns:
        str: The absolute path from the root directory.
    """
    path = []

    for command in commands:
        if command == "cd /":
            # Go to the root directory
            path = []
        elif command == "cd .":
            # Stay in the current directory
            continue
        elif command == "cd .." and path:
            # Go up one level, if possible
            path.pop()
        elif command.startswith("cd "):
            # Change to the specified subdirectory
            subdirectory = command[
                3:
            ].strip()  # Extract the subdirectory from the command, .strip() removes leading/trailing spaces
            if subdirectory:  # Ensure it's not empty
                path.append(subdirectory)

    # Generate the absolute path from the root
    return "/" + "/".join(path)


# Example usage
commands = ["cd /", "cd a", "cd b", "cd ..", "cd c", "cd /", "cd d"]
print(change_directory(commands))  # Output: /d

commands = ["cd user", "cd codesignals", "cd ..", "cd admin"]
print(change_directory(commands))  # Output: /user/admin

commands = ["cd user", "cd .", "cd admin", "cd /", "cd volumes"]
print(change_directory(commands))  # Output: /volumes

commands = ["cd user", "cd .", "cd admin", "cd /", "breakkkk"]
print(change_directory(commands))  # Output: /
