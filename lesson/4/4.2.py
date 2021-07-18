#/usr/bin/python3
#for
#在 Python 中的 for 陳述式有點不同於在 C 或 Pascal 中的慣用方式。相較於只能疊代 (iterate) 一個等差數列（如 Pascal），或給予使用者定義疊代步驟與終止條件（如 C），Python 的 for 陳述式疊代任何序列（list 或者字串）的元素，順序與它們出現在序列中的順序相同。例如（無意雙關）：
words = ['apple', 'banana', 'cat', 'dog', 'egg']
print("=" * 100)
print("simple for:")
print("=" * 100)
for i in words:
    print(i)

print("=" * 100)
print("using len to get array count")
print("=" * 100)
for i in range(len(words)):
    print("index {}: {}".format(i, words[i]))

print("=" * 100)
print("using enumerate")
print("=" * 100)
# use enumerate to trace list items
for index, value in enumerate(words):
    print("index: {}: {}".format(index, value))

print("=" * 100)
print("using for to change collection value")
print("=" * 100)
#在疊代一個集合的同時修改該集合的內容，很難獲取想要的結果。比較直觀的替代方式，是疊代該集合的副本，或建立一個新的集合：
#it means directory can't change directroy in for iterator..?  you can use copy collect to do it 
#or it will say: RuntimeError: dictionary changed size during iteration
user = {'u1':'tom','u2':'petter','u3':'joy'}
for k,v in user.copy().items():
    if k == 'u2':
        del user[k]
print(user)

#mechod 2
new_user = {}
for k,v in user.items():
    if k != 'u1':
        new_user[k] = v
print(new_user)