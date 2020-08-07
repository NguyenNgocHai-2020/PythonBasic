import os


class DemoFile:
    def __init__(self, directory_path, file_path, file_obj=None):
        self.file_obj = file_obj
        self.file_path = file_path
        self.directory_path = directory_path

    def create_directory(self):
        os.makedirs(self.directory_path, 777, True)

    def process_file(self):
        self.file_obj = open(self.directory_path + self.file_path, 'w')
        self.file_obj.write('Đây là bài ')

demo_file = DemoFile('d:\\noi_luu_file\\', 'lession_10.txt')
demo_file.create_directory()
demo_file.process_file()

