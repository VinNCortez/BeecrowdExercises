while True:
    try:
        sentence = input()
        new_sentence = ''
        last_was_lower = True
        for char in sentence:
            if char.isalpha():
                new_sentence += char.upper() if last_was_lower else char.lower()
                last_was_lower = not last_was_lower
            else:
                new_sentence += char
        print(new_sentence)
    except EOFError:
        break