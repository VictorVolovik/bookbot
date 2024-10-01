def count_words(str: str):
  words = str.split()
  return len(words)

def count_characters(str: str):
  result = {}
  for i in range(0, len(str)):
    char = str[i].lower()

    if char in result:
      result[char] += 1
    else:
      result[char] = 1
    
  return result

def main():
  with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    words_count = count_words(file_contents)
    chars = count_characters(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    print("\n")

    for char in chars:
      print(f"The {char} character was found {chars[char]} times")

    print("--- End report ---")

main()
