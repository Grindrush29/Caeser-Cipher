from art import logo
print(logo)

end = False
while end == False:
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  # encodes the message
  def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for letter in plain_text:
  # uses the index to shift the position of the letters
      if letter in alphabet:
        position = alphabet.index(letter)
        check = position + shift
        l = check - 25
        if check > 25:
          cipher_text = cipher_text + alphabet[0 + l]
        else:
          cipher_text = cipher_text + alphabet[position + shift_amount]      
      else:
        cipher_text += letter
    return cipher_text
    print(f"The encoded text is {cipher_text}")
  
  
  # decodes the message
  def decrypt(encrypt, shift_amount):
    decoded_text = ''
    for letter in encrypt:
  # uses the index to shift the position of the letters
      if letter in alphabet:
        position = alphabet.index(letter)
        check = position - shift
    # if check is negative loops through the aphabet list encode
        if check < 0:
          decoded_text = decoded_text + alphabet[25 - (check * -1)]
        else:
          decoded_text = decoded_text + alphabet[position - shift_amount]
      else:
        decoded_text += letter
    return decoded_text
    print(f"The decoded text is {decoded_text}")
  
  
  def ceaser(direction, text, shift):
    ceaser_text = ''
    if direction == "encode":
      ceaser_text = encrypt(plain_text=text, shift_amount=shift)
    else:
      ceaser_text = decrypt(encrypt=text, shift_amount=shift)
    print(f"The {direction} text is {ceaser_text}")
      
  ceaser(direction, text, shift)
  choice = input("Type 'yes' if you want to go again. Otherwise type 'no'").lower
  if choice == "yes":
    end == True
  else: 
    end == False