

1.
text = "hello world"
print(text.endswith("world"))  
print(text.endswith("hello"))  
print(text.endswith("o", 0, 5))

2. 
text = "banana banana apple banana"
print(text.count("banana"))  
print(text.count("apple"))   
print(text.count("n", 2, 10))

3.

text = "I like apples. Apples are tasty."
new_text = text.replace("apples", "bananas")
print(new_text)

4.
text = "   Hello, World!   "
print(text.strip())