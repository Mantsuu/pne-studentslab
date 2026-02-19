
text = "  Hello, World! Welcome to Python Programming.  "

space_remove = text.strip()
print("Stripped: ", space_remove)

words = space_remove.split()
n_words = len(words)
print("Word count: ", n_words)

capitalize = space_remove.title()
print("Title case: ", capitalize)

s_start = space_remove.startswith("Hello")
print("Starts with Hello: ", s_start)

s_ends = space_remove.endswith("ing")
print("Ends with ing: ", s_ends)

position = space_remove.find("Python")
print("Python position: ", position)

words_join = " - ".join(words)
print("Joined: ", words_join)