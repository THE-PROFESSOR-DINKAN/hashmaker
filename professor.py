from pyfiglet import Figlet
import hashlib



def banner(text):
	custom_fig = Figlet(font='graffiti')
	print(custom_fig.renderText(text))

banner("hashmaker")
text = ""
print("""availabe encodings are:\n.
            1.MD5\n.
            2.SHA256\n.
            3.ShA512\n.
            4.Exit """  )
while True:
	choice = int(input("Enter an option u need: "))
	if choice == 4:
		print("have a nice day")
		banner("quiting")
		exit()
	else:
		string = input("Enter the text to encode:")

	def md5(string):
		hash_object = hashlib.md5(string.encode())
		print("MD5: " + hash_object.hexdigest() + "\n")

	def sha512(string):
        	hash_object = hashlib.sha512(string.encode())
        	print("SHA512: " + hash_object.hexdigest() + "\n")

	def sha256(string):
        	hash_object = hashlib.sha256(string.encode())
        	print("SHA256: " + hash_object.hexdigest() + "\n")
	


	if choice == 1:
		md5(text)
	elif choice == 2:
		sha512(text)
	elif choice == 3:
		sha256(text)
	else:
		print("Sorry wrong input....!")
		banner("Exiting")
		exit()
