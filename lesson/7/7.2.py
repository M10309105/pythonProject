#/usr/bin/python3
#
#file I/O
print("=" * 100)
print("7.2 file I/O")
print("=" * 100)

#r:read, default
#w:write
#a:append end
#r+: read& write
#mode use b will open in binary mode
#open(filename, mode)
#use with is good
value = ('the answer', 42)
s = str(value)
with open("lesson/7/test.txt",'a') as f:
    f.write("{}\r\n".format(s))
    f.close()

with open("lesson/7/test.txt",'r') as f:
    data = f.read()
    f.close()
    print(data)

#   read size, if size not give, read all.
#   if had read end, read() again will return ''
#f.read(size)

#   read single line till \n
#f.readline() 

with open("lesson/7/test.txt",'r') as f:
    for data in f:
        print(f"tell:{f.tell},read=>{data}",end='')
    f.close()

#change point
#whence:
#  0: start
#  1: current place
#  2: the end of file
#offset: shift value
# f.seek(offset, whence) 

#在文字檔案（開啟時模式字串未加入 b 的檔案）中，只允許以檔案開頭為參考點進行尋找（但 seek(0, 2) 尋找檔案最末端是例外），且只有從 f.tell() 回傳的值，或是 0，才是有效的 offset 值。其他任何 offset 值都會產生未定義的行為。
# 檔案物件還有一些附加的 method，像是較不常使用的 isatty() 和 truncate()；檔案物件的完整指南詳見程式庫參考手冊。

print("=" * 100)
print("7.2.2 save json")
print("=" * 100)
import json
x = [1,2,3,4,5]
#dump json obj to serialization text
with open("lesson/7/test.json",'r+') as f:
    # json.dump(x,f)
    print(json.load(f))
    f.close()
