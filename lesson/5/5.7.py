#/usr/bin/python3
#
#condition

print("=" * 100)
print("5.7 condition")
print("=" * 100)

 #A and not B or C equals (A and (not B)) or C
 #if B is false, --> if A and B or C  will return false in (A and B) and not to C
 
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
#return string2
print(non_null)

#在運算式裡進行指派必須外顯地使用海象運算子 :=。
# while chunk := fp.read(200):
#    print(chunk)