def to_jaden_case(text):
    words = text.split(" ")
    jaden_words = []
    for word in words:
        if word:
            jaden_words.append(word[0].upper() + word[1:])
        else:
            jaden_words.append("")
    return " ".join(jaden_words)

a = input("User insert a: ")
print("Result:", to_jaden_case(a))
