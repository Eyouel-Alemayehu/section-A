
README 

1. str.lstrip()

The lstrip() method removes leading whitespace (spaces, tabs, newlines) or specified characters from the beginning (left side) of a string.

2. str.rstrip()

The rstrip() method removes trailing whitespace (spaces, tabs, newlines) or specified characters from the end (right side) of a string.

3. str.split()
The split() method in Python splits a string into a list of substrings based on a specified delimiter. If no delimiter is provided, it splits at whitespace by default.

4. str.join()

The join() method in Python joins elements of an iterable (like a list or tuple) into a single string, using the given string as a separator.
2.
text = "   Hello, World!   "
print(text.rstrip())

3.
text = "apple,banana,orange"
print(text.split(","))

4.
words = ["apple", "banana", "orange"]
print(", ".join(words))