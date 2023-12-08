import logging
import json
logging.basicConfig(level=logging.INFO)
current_directory = None
total_space_available = 70000000
min_space_free        = 30000000
class dir_file():
    def __init__(self, name: str, size: int):
        self.name: str = name
        self.size: int = size
    
    def update_size(self):
        logging.debug(f"updated size  of {self.name} to {self.size}")
        return self.size
    
    def __repr__(self):
        return f"{self.name} - {self.size}"


class directory():
    def __init__(self, name: str, parent):
        self.name = name
        self.contents = {}
        self.parent = parent
        self.size = 0
    
    def add_item(self, f: dir_file):
        logging.debug( f"added {f.name} to {self.name}")
        self.contents[f.name] = f
        self.size += f.size
    
    def update_size(self):
        self.size = 0
        for i in self.contents.values():
            i.update_size()
            self.size += i.size
        logging.debug( f"updated size  of {self.name} to {self.size}")
        return self.size
    
    def get_dir(self, dir_name: str):
        logging.debug( f"getting {dir_name} from {self.name}")
        return self.contents[dir_name]
    
    def get_less_than(self, filter_size):
        total = 0
        if self.size < filter_size:
            total += self.size
        for k in self.contents:
            if type(self.contents[k]) == directory:
                total += self.contents[k].get_less_than(filter_size)
        return total
    
    def get_dir_sizes(self):
        dir_sizes = []
        for i in self.contents.items():
            if type(i[1]) == directory:
                dir_sizes.append((i[0], i[1].size))
                dir_sizes = dir_sizes + i[1].get_dir_sizes()
        return dir_sizes
    
    def find_dir_to_delete(self):
        min_dir_delete_size = self.size - (total_space_available - min_space_free)
        dir_sizes = self.get_dir_sizes()
        dir_sizes = sorted(dir_sizes, key=lambda item: item[1])
        logging.debug(f"min delet {min_dir_delete_size}")
        for d in dir_sizes:
            logging.debug(f"checking {d}")
            if d[1] >= min_dir_delete_size:
                return d
                

def list_files(command):
    logging.debug(f"list_files {command}")
    if command[0] == 'dir':
        current_directory.add_item(directory(command[1], current_directory))
    else:
        current_directory.add_item(dir_file(command[1], int(command[0])))

def change_dir(dir_name):
    global current_directory
    if current_directory == None:
        current_directory = directory(dir_name, None)
        return
    if dir_name == "..":
        current_directory = current_directory.parent
    else:
        current_directory = current_directory.get_dir(dir_name)
    
    
with open("day-7/input.txt") as commands:
    for command in commands:
        command = command.strip().split()
        if command[0] == "$":
            if command[1] == 'cd':
                change_dir(command[2])
            else:
                pass
        else:
            list_files(command)
    
    while current_directory.parent != None:
        current_directory = current_directory.parent
    current_directory.update_size()
    print("current dir size ", current_directory.size)
    print(current_directory.find_dir_to_delete())
                
    
