#/usr/bin/python3
#
#Class
print("=" * 100)
print("11.2 Templating")
print("=" * 100)

#templating
from string import Template
#${variable}, $$=>$

template = Template("This is tamplate one, name:${name} and price is $$${price}")

out = template.substitute(name="Hakunamatata", price=9487)
print(out)
print("=" * 100)

# out = template.substitute(name="hakunamatata")
# print(out)

try:
    out = template.substitute(name="hakunamatata")
    print("try:",out)
except Exception as e:
    #key error
    print("err:",e)
print("=" * 100)

#or use safe_substitute
out = template.safe_substitute(name="hakunamatata",aaa='123')
print(out)


#Template subclasses can specify a custom delimiter.
import os.path, time

class SubTemplate(Template):
    delimiter = '%'

str = input('please input your format(%d:date, %f:format, %i:sequence):')
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

t = SubTemplate(str)
date = time.strftime('%Y%m%d')
print("date:",date)
for i,fileName in enumerate(photofiles):
    base, ext = os.path.splitext(fileName)
    out = t.substitute(d=date,i=i, f=ext)
    print("{0}==>{1}".format(fileName, out))

"""
KonoDioda_%d-%i%f
please input your format(%d:date, %f:format, %i:sequence):KonoDioda_%d-%i%f 
date: 20210902
img_1074.jpg==>KonoDioda_20210902-0.jpg
img_1076.jpg==>KonoDioda_20210902-1.jpg
img_1077.jpg==>KonoDioda_20210902-2.jpg
"""
