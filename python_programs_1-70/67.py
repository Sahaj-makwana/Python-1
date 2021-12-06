#67)Write a Python program to print a specified list after removing the 1st, 2nd and 5th elements.
name = ['Reyna', 'sage', 'skye', 'viper', 'sova', 'brim']
name = [x for (i,x) in enumerate(name) if i not in (1,2,5)]
print(name)