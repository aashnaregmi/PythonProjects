char="abcdefghijklmnopqrstuvwxyz"

wish="yes"
print("")
print("================Caesar Cipher Encoder / Decoder================")

while wish=="yes":
  encrypted = ""
  decrypted = ""


  request = input("\nEnter your choice (encode / decode): ").lower()
  if request !="encode" and request !="decode":
      print("ERROR: Please type only 'encode' or 'decode'")
      continue
  msg = input("Enter msg : ").lower()
  shiftkey = int(input("Enter shift number: "))




  if request=="encode":
     for letter in msg:
         charindex=char.index(letter)
         finalindex=(charindex+shiftkey)%26
         encrypted+=char[finalindex]
     print("Encrypted message:", encrypted)

  else:
      for letter in msg:
          charindex=char.index(letter)
          finalindex=(charindex-shiftkey)%26
          decrypted+=char[finalindex]
      print("Decrypted message:", decrypted)

  wish=input("\nContinue? (yes / no): ").lower()