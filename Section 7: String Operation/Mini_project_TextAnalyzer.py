print("========================================")
print("           TEXT ANALYSER                ")
print("========================================")

# Get text from user
print("Enter your text below.")
print("Press Enter twice when done.\n")

text = input("Enter text: ")

print("\n========================================")
print("           ANALYSIS RESULTS             ")
print("========================================")

total_chars=len(text)
total_char_no_spaces=len(text.replace(" ",""))
total_words=len(text.split())
total_sen=text.count(".")+text.count("!")+text.count("?")

print(f"Total Characters    : {total_chars}")
print(f"Characters (no space): {total_char_no_spaces}")
print(f"Total Words         : {total_words}")
print(f"Total Sentences     : {total_sen}")

# #count vowels and consonants

vowels="aeiouAEIOU"
vowel_count=0
const_count=0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count+=1
        else:
            const_count+=1
print(f"Total Vowels        : {vowel_count}")
print(f"Total Consonants    : {const_count}")

#word frequency

words=text.lower().split()
word_count={}

for word in words:
    word=word.strip(".,!?")
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
most_common=max(word_count,key=word_count.get)
print(f"Most Common Word     : '{most_common}' ({word_count[most_common]} times)")


# Text properties
print("----------------------------------------")
print(f"Is Uppercase         : {text.isupper()}")
print(f"Is Lowercase         : {text.islower()}")
print(f"Starts With          : '{text[0]}'")
print(f"Ends With            : '{text[-1]}'")

if total_words > 0:
    avg_word_length = total_char_no_spaces / total_words
    print(f"Avg Word Length      : {avg_word_length:.1f} characters")

print("========================================")
print("         ANALYSIS COMPLETE!")
print("========================================")
    