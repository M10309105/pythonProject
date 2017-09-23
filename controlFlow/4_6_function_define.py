# 4.6 function define


def fin(n):
	a,b = 0,1
	while a < n :
		print(a,end=" ")
		a,b=b,a+b
	print()

fin(5000)

print("document example")

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return "Y"
        if ok in ('n', 'no', 'nop', 'nope'):
            return "N"
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
		
print(ask_ok('Do you really want to quit?'))
print(ask_ok('OK to overwrite the file?', 2))
print(ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!'))