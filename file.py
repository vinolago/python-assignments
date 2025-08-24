#Write into file 5 times
with open("input.txt", "w") as file:
    content = file.write(("I am a software developer\n") *5)

#Read file content
with open("input.txt", "r") as file:
    content = file.read()
    print(content)

#Split content into whitespace/words
words = content.split() 
word_count = len(words)
print(word_count)

#Convert all text to uppercase
upper_case_text = content.upper()
print(upper_case_text)

#Write processed text and word count to new file
try:
    with open("output.txt", "w") as new_file:
        new_file.write(upper_case_text + "\n")
        new_file.write("Word count: " + str(word_count))
    print('File output.txt was created and written successfuly.')

except IOError as e:
    print("An I/O eror ocurred: ", e)

except FileNotFoundError as e:
    print("File not found", e)



