from sys import argv
import os
import git
home_dir = '/home/devanshmanu/IIIT/Sem5/ITWS_TA/Assignment3/Repo_Dump'



mylist = open("result.txt", 'r')
for filename in mylist:
	temp= filename.split("https://gitlab.com/",1)[1]
	print("Doing for:",temp)
	folder=temp.split("/",1)[0]
	if not os.path.exists(folder):
		os.makedirs(str(folder))
		os.chdir(str(folder))
		proper_filename= filename.split("\n",1)[0]
		git.Git().clone(proper_filename)
		os.chdir(str(home_dir))



mylist.close()





