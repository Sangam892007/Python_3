import os;
import shutil;

#os.system("Date");
print(os.getcwd())

os.mkdir("C:\Desktop\Coding\PYTHON\Dummy")

A = os.listdir("C:\Desktop\Coding\PYTHON")

#print(A)
B = "TripleX.cpp"
a,b = os.path.splitext("C:\Desktop\Coding\TripleX.cpp")
print(a)
print(b)

path1 = "C:\Desktop\Coding\TripleX(C++)\TripleX.cpp"
path2 = "C:\Desktop\YouTube Video Material\TripleX.cpp"

shutil.copy(path1,path2)


