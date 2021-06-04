import os;
import shutil;

A = input("Plz enter the path of file")
B = os.listdir(A)

for i in B:
    C,D = os.path.splitext(i)
    if D == "":
        continue
    if os.path.exists(A + "/" + D):
        shutil.move(A + "/" + i, A + "/" + D + "/" + i)
    else:
        os.makedirs(A + "/" + D)
        shutil.move(A + "/" + i, A + "/" + D + "/" + i)



