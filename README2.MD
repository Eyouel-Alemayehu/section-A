# String Manipulation Functions in Python

# 1. str.swapcase()
text = "Hello World!"
swapped_text = text.swapcase()
print(swapped_text)  # Output: hELLO wORLD!

text2 = "MiXeD CaSe"
swapped_text2 = text2.swapcase()
print(swapped_text2) # Output: mIxEd cAsE

# 2. str.find()
text = "Hello World!"
index = text.find("World")
print(index)  # Output: 6

index2 = text.find("Python")
print(index2) #Output: -1

index3 = text.find("o", 5, 8)
print(index3) # Output: 7

# 3. str.index()
text = "Hello World!"
index = text.index("World")
print(index)  # Output: 6

try:
    index2 = text.index("Python")
    print(index2)
except ValueError:
    print("Substring not found.") # Output: Substring not found.

index3 = text.index("o", 5, 8)
print(index3) #Output: 7

# 4. str.startswith()
text = "Hello World!"
starts_with_hello = text.startswith("Hello")
print(starts_with_hello)  # Output: True

starts_with_world = text.startswith("World")
print(starts_with_world)  # Output: False

starts_with_o = text.startswith("o", 4)
print(starts_with_o) #Output: True

starts_with_tuple = text.startswith(("Hel","Wel"))
print(starts_with_tuple) #Output: True