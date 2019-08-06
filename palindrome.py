
wrd = input("Enter a word: ")
wrd = str(wrd)

rvs = wrd[::-1]

while rvs != wrd:
    print("This word is not a palindrome")
    wrd = input("Enter a word: ")
    wrd = str(wrd)

    rvs = wrd[::-1]
if rvs == wrd:
    print("This word is a palindrome")
