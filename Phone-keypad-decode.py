# python3
# author : 6ued

keypad = {
	"1":"",
	"2":"ABC",
	"3":"DEF",
	"4":"GHI",
	"5":"JKL",
	"6":"MNO",
	"7":"PQRS",
	"8":"TUV",
	"9":"WXYZ",
	"*":"*",
	"0":"",
	"#":"#",
}
numbers = "0123456789"


def main():
	print("Option:")
	print("\tinput 1 for input cipher.")
	print("\tinput 2 for read cipher from file.")
		
	option = 0
	while not (option == 1 or option == 2):
		print("\nChoose option: ", end="")
		option = int(input())
		if option == 1:
			print("Input cipher: ", end="")
			cipher = str(input())+"\n\n"
		elif option == 2:
			print("Input file path: ", end="")
			path = input()
			cipher = open(path).read()+"\n\n"
		else:
			print("Select only 1 or 2.")

	msg = ""
	bf = ""
	count = 0
	for i in cipher:
		if i == bf or bf == "":
			count += 1
			bf = i
		else:
			if bf in numbers:
				msg += keypad[bf][(count-1)]
			else:
				msg += bf
			bf = i
			count = 1
	print("\nMessage:", msg)

main()