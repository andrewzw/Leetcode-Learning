import os
import time


def delete_files(folder_path):
    deleted_files = 0
    permission_denied = 0
    error_deleting = 0
    error_accessing = 0
    print(f"\nCleaning folder: {folder_path}")
    try:
        files = os.listdir(folder_path)
        for file in files:

            file_path = os.path.join(folder_path, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file}")
                deleted_files += 1
            except PermissionError as e:
                print(f"Permission denied: {file}: {e}")
                permission_denied += 1
            except Exception as e:
                print(f"Error deleting: {file}: {e}")
                error_deleting += 1
    except Exception as e:
        print(f"Error accessing folder {folder_path}: {str(e)}")
        error_accessing += 1
    print(
        f"\n=============== Logs ===============\nFolder: {folder_path}\nFiles deleted: {deleted_files}"
    )
    print(
        f"---------- Errors ----------\nPermission denied: {permission_denied}\nError deleting: {error_deleting}\nError accessing: {error_accessing}"
    )
    print("Finished cleaning folder \n=============== End ===============")


def userName(user):
    folders = [f"C:/Users/{user}/AppData/Local/Temp", "C:/Windows/Temp"]
    return folders


if __name__ == "__main__":
    try:
        folders = userName("ZW")
        for folder in folders:
            delete_files(folder)

        print("\nCleaning complete! Exiting in 2 seconds...")
        time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")
        print("\nPress Enter to exit...")
        input()
