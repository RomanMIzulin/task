# Написать программу, которая генерирует непустой файл, (содержащий произвольные данные), произвольного размера в произвольной директории.
# На вход программа должна принимать следующие аргументы:
# имя файла,
# размер файла как в обычном виде (в виде количества байт) так и в «human readable» виде (например, 10MB),
# полный путь до каталога, где этот файл должен быть создан. 
# Программа будет запускаться под ОС Windows.
# Примеры запуска программы:
# create_custom_file.py my_test_file 100MB C:\test_folder
# create_custom_file.py my_test_file 1024 C:\test_folder
# create_custom_file.py my_test_file 1KB C:\test_fol

# python3.5 1024byte =1KB
import sys

def create(name,way):
	print("creating new  file")
	file=open(way+"/"+name,'a')
	file.close()

def fullfill(file,size):
	f = open(file,"w")
	for x in range(size): 
		f.write("a")
	f.close() 

def correct_size(size):
	if size[-2] == "K":
		tmp = int(size[0:-2]) *1024
	elif size[-2] == "M":
		tmp = int(size[0:-2]) *1024**2
	elif size[-2] == "G":
		tmp = int(size[0:-2]) *1024**3
	else:
		tmp = int(size);
	return tmp;		

f = input();
s = f;
listik = tuple(s.split());
name = listik[0];
size = correct_size(listik[1]);
way = listik[2];

create(name,way);
fullfill(way+"/"+name,size);

