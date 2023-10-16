import os 
from pathlib import Path
class FileSystemExpection:
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class ScanFolder:
    def __init__(self, user_directory_path):
        self.user_directory_path = Path(user_directory_path)

    def check_directory_status(self) -> None:
       if not os.path.isdir(self.user_directory_path) or len(os.listdir(self.user_directory_path)) <= 0:
           raise FileSystemExpection("The directory you enter is either empty or does not exist")

    def scan(self)->list:
        self.check_directory_status()
        return list(self.user_directory_path.glob('*'))
            
        