def swap_case(s):
    new_string = ""
    for i in range (0,len(s)):
        if s[i].islower():
            new_letter = s[i].upper()
            new_string = new_string + new_letter
        else:
            new_letter = s[i].lower()
            new_string = new_string + new_letter
    return new_string

