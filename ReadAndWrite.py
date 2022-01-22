# read and write 

# name of the file in the current working directory (call also be a path)
name_of_the_file_to_open = 'data_for_read.txt'
# you can get the path by using the library 'os'
import os
current_working_directory = os.getcwd()
full_file_path = os.path.join(current_working_directory, 'data_for_read.txt')
print('This is the full file path:\n', full_file_path)

# mode available for opening a file (some of them can be combined like 'rt')
# r: read (default) 
# w: write (removes the file if it already exists)
# x: create and write (Error if file already exists)
# a: append at the end(if already exists) and write
# +: read and write
# t: textmode(default), b: binary mode
mode_for_file_open = 'rt' 

# python defaults to local encoding so it's better to specify 'utf-8' (the most common encoding)
encoding_of_the_file = "utf-8" 

file = open(file=name_of_the_file_to_open, mode=mode_for_file_open, encoding=encoding_of_the_file)
# readline method will read one line can continue for the next call
# a file streaming cursor keeps track of the current reading position in the file
a = file.readline()
print(a)
# note that the newline is also read, and can be easily removed by replace()
a = file.readline().replace('\n', '')
print(a)
# readlines reads all remaining lines into a list of which elements are lines read
a = file.readlines()
print(a)
# at the end of the file, readline/readlines returns empty string/list
a = file.readline()
print(f'readline returns empty string:{a}!')
a = file.readlines()
print(f'readlines returns empty list:{a}!')
# close the file
file.close()
exit()


# the streaming cursor can be controlled by the method seek()
amount_of_move_forward = 0 # in units of character; can be negative
reference_point_of_the_move = 1 # 0: beginning(default), 1: current, 2: end of the file
# the seek method returns the position of the streaming cursor after the move
print('seek method:')
file = open(file=name_of_the_file_to_open, mode=mode_for_file_open, encoding=encoding_of_the_file)
print('current cursor position:', file.seek(0, 1))
print(file.readline().replace('\n', ''))
print('current cursor position:', file.seek(0, 1))
print(file.readline().replace('\n', ''))
print('current cursor position:', file.seek(0, 1))
# move cursor back to the beginning
print('current cursor position:', file.seek(0, 0))
print(file.readline().replace('\n', ''))
print('current cursor position:', file.seek(0, 1))
file.close()



# Opening a file using 'with' (a more standard and safer way):
# file is automatically terminated after leaving the 'with' scope
print('Stardard opening:')
with open(file=name_of_the_file_to_open, mode=mode_for_file_open, encoding=encoding_of_the_file) as file:
	a =  file.readlines()
print(a)

# writing to a file
name_of_the_file_to_open = 'data_for_write.txt'
mode_for_file_open = 'w'
encoding_of_the_file = 'utf-8'
with open(name_of_the_file_to_open, mode=mode_for_file_open, encoding=encoding_of_the_file) as file:
	file.write('1st line\n')
	file.write('2nd line\n')
	file.write('3rd line\n')


# see help, which is clearly written, for more details
#help(open)