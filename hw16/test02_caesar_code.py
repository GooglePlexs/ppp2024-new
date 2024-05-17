def caesar_encode(text: str, shift: int = 3) -> str:

  input_text = ""

  for word in text:

    if word.isalpha():
      
      if word.isupper():
        lock_text = ord(word) + shift
        if lock_text > ord('Z'):
          lock_text -= 26

      else:
        lock_text = ord(word) + shift
        if lock_text > ord('z'):
          lock_text -= 26
      input_text += chr(lock_text)

    else:
      input_text += word

  return input_text


def caesar_decode(text: str, shift: int = 3) -> str:
  
  trans_shift = -shift

  return caesar_encode(text, trans_shift)  


def main():
  
  original_text = input("암호화가 필요한 영단어를 입력하시오 : ")
  encoded_text = caesar_encode(original_text)
  decoded_text = caesar_decode(encoded_text)

  print(f"원본 텍스트: {original_text}")
  print(f"암호화된 텍스트: {encoded_text}")
  print(f"복호화된 텍스트: {decoded_text}")

if __name__ == "__main__":
  main()