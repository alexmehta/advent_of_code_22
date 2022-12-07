global_dirs = []
def search(curr):
    ans = 0
    for dir in curr.dirs:
        if(dir.is_directory):
            ans+= int(search(dir))
        else:
            ans +=int(dir.size)
    return ans
class Directory():
    def add_dir(self,dir):
        self.dirs.append(dir)
    def __init__(self,size,name,is_directory=False,parent=None):
        self.size = size
        self.name = name
        self.dirs = []
        self.parent = parent
        self.is_directory = is_directory
    def __str__(self) -> str:
        return self.name 
        

directories = Directory(0,'/')
curr_dir = directories
while True:
    line = input()
    if(line=='done'):
        break
    if(line=='$ ls'):
        inp = input()
     
        while not inp.startswith('$'):
            if(inp.startswith('dir')):
                a = Directory(0,inp.split()[1],is_directory=True,parent=curr_dir)
                curr_dir.add_dir(a)
                global_dirs.append(a)
            else:
                if(inp=='done'):
                    line = inp
                    break
                size,file = inp.split()[0],inp.split()[1]

                added = Directory(size,file,parent=curr_dir)
                curr_dir.add_dir(added)
            inp = input()
        if(inp=='done'):
            break
        line = inp
    
    if(line.startswith('$ cd')):
        prev= curr_dir
        dir = line.split(' ')[2]
        if(dir=='..'):
            curr_dir = curr_dir.parent
        elif(dir=='/'):
            curr_dir = directories
        else:
            for dirz in curr_dir.dirs:
                if(dirz.name==dir):
                    curr_dir = dirz
                    break
    
filter = []
for dir in global_dirs:
    filter.append(search(dir))
filter.append(search(directories))
filters = []
disk_space =70000000 -  search(directories)
needed = 30000000 - disk_space
parta = []
for dir in filter:
    if(dir<=100000):
        parta.append(dir)
    if(dir>=needed):
        filters.append(dir)
print(sum(parta))
print(sorted(filters)[0])
