# import pyperclip

# text = input('input your string here : ')


def reverse_string(input_string):
    newtext = input_string[::-1]
    # newtextlist = list(newtext.split())
    # # newtextlist = list(newtext)
    # newtextlist.sort(reverse=True)
    # print(text)
    # print(newtextlist)
    return newtext
user_input = input("Enter a string: ")

# Call the function and print the reversed string
newtext = reverse_string(user_input)
print("Reversed string:", newtext)