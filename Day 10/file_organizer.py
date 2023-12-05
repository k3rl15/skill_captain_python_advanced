import logging
import os
from shutil import move
from time import sleep


def main():
    """Main function to organize files from source to destination."""
    logging_config()
    logging.debug("Starting program.")
    source_path, destination_path = get_paths()
    logging.debug("Organizing started...")
    organize_files(source_path, destination_path)
    sleep(.1)
    logging.debug("Organizing completed.")
    sleep(1)
    logging.debug("Closing program.")


def logging_config():
    """Configure logging for the program."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler()]
    )


def get_paths():
    """Get source and destination paths from user input."""
    sleep(.1)
    source = get_valid_path("Enter the source path directory: ")
    destination = get_valid_path("Enter the destination path directory: ")

    return source, destination


def get_valid_path(prompt):
    """Prompt user for a valid directory path."""
    while True:
        path = input(prompt)
        if os.path.exists(path) and os.path.isdir(path):
            return path
        logging.error("Invalid directory. Please enter a valid path.")
        sleep(.1)


def organize_files(source_dir, destination_dir):
    """Organize files from source to destination based on file extensions."""
    extension_categories = {
        ('txt', 'pdf', 'doc', 'docx', 'rtf', 'odt', 'log', 'xls', 'xlsx', 'ppt', 'pptx'): 'Documents',
        ('jpg', 'jpeg', 'png', 'gif', 'bmp', 'ico'): 'Images',
        ('mp3', 'm4a', 'aac', 'wav', 'ogg', 'wma'): 'Music',
        ('mp4', 'wwv', 'avi', 'webm', 'flv', 'mov', 'mkv'): 'Videos',
        ('c', 'cpp', 'java', 'js', 'py', 'html', 'css'): 'Programming Files',
        ('zip', '7z', 'tar', 'rar', 'tgz', 'gz'): 'Compressed Files',
        ('json', 'xml', 'csv'): 'Data Structure Files',
        'exe': 'Executable'
    }
    try:
        all_files = os.listdir(source_dir)

        for file_name in all_files:
            file_path = os.path.join(source_dir, file_name)
            if os.path.isfile(file_path):
                file, extension = os.path.splitext(file_name)
                if not extension:
                    extension = file
                extension = extension[1:].lower()

                categories = "Other Files"
                for extensions, category in extension_categories.items():
                    if extension in extensions:
                        categories = category
                        break

                category_path = os.path.join(destination_dir, categories)

                if not os.path.exists(category_path) or not os.path.isdir(category_path):
                    create_category_directory(category_path)

                destination_path = os.path.join(category_path, file_name)

                if os.path.isfile(destination_path):
                    logging.error(f"Path: {category_path}: File - {file_name} already exists.")
                else:
                    move(file_path, destination_path)
                    logging.info(f"File - {file_name} Moved to Path: {destination_dir} into {categories} folder.")

    except (FileNotFoundError, PermissionError) as e:
        logging.error(f"{str(e).capitalize()}.")


def create_category_directory(category_path):
    """Create a new directory for a specific file category."""
    os.mkdir(category_path)


if __name__ == "__main__":
    main()
