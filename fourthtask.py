# Написать скрипт/программу которая должна:
# 1) осуществлять поиск в iplir.conf и определять содержатся ли в указанной секции id, указанные записи(записей не меньше 1го).
# 2) В случае положительного результата просто выводить сообщение о успешном завершении.
# 3) В случае отрицательного результата выводить что именно пошло не так, какую из записей или id не удалось найти.
# 4) Аргументы содержатся в конфигурационном файле:
# path – путь к iplir.conf,
# id – id секция которую будем анализировать,
# 1 или несколько записей –  которые нужно искать в данной секции (указывается регуляркой).

# Пример конфига (conf.txt), для положительного результата:
# path = /tmp/iplir.conf
# id = 0x1620001f
# string = “tunnel.*19.0.0.100-19.0.0.110.*19.0.0.100-19.0.0.110”
# string1 = “tunnel.*19.0.0.1-19.0.0.1.*19.0.0.1-19.0.0.1”
# string2 = “ip.*173.18.0.1”

# пример конфига (badconf.txt) для отрицательного результата
# path = /tmp/iplir.conf
# id = 0x1620001e
# string = “tunnel.*19.0.0.100-19.0.0.110.*19.0.0.100-19.0.0.110”
# string1 = “tunnel.*19.0.0.1-19.0.0.1.*19.0.0.1-19.0.0.1”
# string2 = “ip.*173.18.0.1”

import sys
import re

def calculate_and_output(file_conf,structure_for_notes_by_id):
	mega_flag = 0;
	for line in file_conf:
		flag = 0;
		length =len(line);
		i=0;
		while line[i]!='“' and i<length-1:
			i=i+1;

		
		if line[i] == '“':
			pattern = line[i+1:-2];
			
			p = re.compile(pattern);
			
			for x in structure_for_notes_by_id :
				m = p.search(x)
				
				if m:
					
					flag = 1;
			
			if flag==0 :
				print(line ," seems as a trouble. Here something went wrong. " )
				mega_flag=mega_flag+1;

	if mega_flag ==0:
		print("succes")
	else:
		print("Unmatched notes were found") 

file_conf= open("badconf.txt","r"); #configuration file
path = (file_conf.readline())[7:-1];

file = open(path,"r"); #data file

ID = (file_conf.readline())[5:-1]; 

structure_for_notes_by_id = [];

# If ID found then copy its notes in structure_for_notes_by_id
for line1 in file: 
	if line1[4:14] == ID:
		
		structure_for_notes_by_id.append(line1[0:-1])
		for line1 in file:
			if (line1[0] != "["):
				structure_for_notes_by_id.append(line1[0:-1])
			else:
				break;

file.close();		


#looking for mathes 
if(structure_for_notes_by_id!={}):
	calculate_and_output(file_conf,structure_for_notes_by_id);

file_conf.close();