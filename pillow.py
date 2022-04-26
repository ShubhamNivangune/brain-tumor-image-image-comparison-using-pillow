from fileinput import filename
from PIL import Image
import glob
from heapq import nlargest
from operator import itemgetter

i1 = Image.open("TCGA_DU_7294_19890104_15.tif")

path = "brain/*"
# dir_list = os.listdir(path)
list_1=[]
# for x in os.listdir(path):
for x in glob.iglob(path):
    i2 = Image.open(x)
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."
    
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
    
    ncomponents = i1.size[0] * i1.size[1] * 3
    diff =(dif / 255.0 * 100) / ncomponents
    g = 100 - diff
    print ("File :", x)
    ans = float("{:.2f}".format(g))
    ok = (ans, x)
    list_1.append(ok)
    print ("Matches: ", ans,"%")

var = nlargest(5, list_1, key=itemgetter(0))
print(nlargest(5, list_1, key=itemgetter(0)))
for a in var:
    print("-------------------------------------------------------------------------------")
    print(f'Patient Name : {a[1]}     Matches : {a[0]}%')
print("-------------------------------------------------------------------------------")



# Matches = max(list_1)[0]
# Per = max(list_1)[1]
# # person = (Per.rsplit('/',1)[1])
# # person2 = (person.rsplit('.',1)[0])
# print("----------------------------------------------------")
# print(f'Patient Name : {Per}     Matches : {Matches}%')
# print("----------------------------------------------------")