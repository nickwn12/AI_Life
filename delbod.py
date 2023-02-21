import os
os.system("rm summerbod.urdf")
os.system("rm brain.nndf")
os.system("python3 generatebody.py")
os.system("python3 search.py")
# os.system("python3 run.py")
