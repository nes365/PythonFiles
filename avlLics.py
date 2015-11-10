#!/usr/bin/python
from subprocess import call
def print_menu():
	print('==================================')
	print('======= AVL License Status =======')
	print('')
	print('1. Show all license usage')
	print('2. Show excite gui license usage')
	print('3. Show aws impress license usage')
	print('4. Show license server status')
	print('5. Exit')
	print('')
	print('==================================')
numbers = {}
menu_choice = 0
print_menu()

while menu_choice != 5:

		menu_choice = int(input("Enter 1-5 (or 0 for menu): "))
		if menu_choice == 1:
			call(["/lustre/apps/flexlm/lmutil", "lmstat",  "-c", "27100@brx-els-001:27100@brx-els-002:27100@brx-els-003", "-a"])
		elif menu_choice == 2:
			call(["/lustre/apps/flexlm/lmutil", "lmstat",  "-c", "27100@brx-els-001:27100@brx-els-002:27100@brx-els-003", "-f", "excite_gui"])
		elif menu_choice == 3:
			call(["/lustre/apps/flexlm/lmutil", "lmstat",  "-c", "27100@brx-els-001:27100@brx-els-002:27100@brx-els-003", "-f", "aws_impress"])
		elif menu_choice == 4:
			call(["/lustre/apps/flexlm/lmutil", "lmstat",  "-c", "27100@brx-els-001:27100@brx-els-002:27100@brx-els-003"])
		elif menu_choice == 0:
			print_menu()
		elif menu_choice != 5:
			print_menu()	
