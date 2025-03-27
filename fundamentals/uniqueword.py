sentence = "hello world hello python world administer"

words = sentence.split()

unique_word = set(words)

word_count = {}
for word in words:
  word_count[word] = word_count.get(word, 0) + 1

print(f"{word_count}")