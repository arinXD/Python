def set_title(text):
    text_lower = text.lower()
    new_text = text_lower.replace(text_lower[0],text[0].upper())
    return new_text

def set_start(text):
    output=''
    text = text.lower()
    text_list = text.split(' ')
    for i in text_list:
        if i!=text_list[-1]:
            upper = i[0].upper()
            new = i.replace(i[0],upper)
            output += new+' '
        else:
            upper = i[0].upper()
            new = i.replace(i[0],upper)
            output += new
    return output
