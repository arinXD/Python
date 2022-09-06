def reverse_str(tence):
    index = len(tence)
    reverse = ''
    while index > 0:
        reverse += tence[index-1]                      
        index -= 1 
    return reverse

sentence = "Structured Programming for Information Technology"
#sentence = 'oat'
print("Reverse string:",reverse_str(sentence))
