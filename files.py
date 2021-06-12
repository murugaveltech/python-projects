import os 

for i in range(1,21):
    os.mkdir("/home/murugavel/Music/test/project/hi"+str(i))
    for h in range(1,21):
        with open("/home/murugavel/Music/test/project/hi"+str(i)+"/hi"+str(h)+"txt",'w')as f:
            for k in range(10):
                f.write("%d\n" %(k+1))