hello = "hell0" #string

first,second,third,fourth,fifth = hello

arr = [first,second,third,fourth,fifth]

for i in arr:
    print(i)

#f strings
a = 9
b = 6

print(f"{a}+{b} = {a+b}")

#multiline strings
multiline_string = '''this is a multiline string
so is this enough of a multiline? well it is a multiline string'''
print(multiline_string)

#string concat
first_name = 'Pranaya'
last_name = 'Manandhar'

full_name = first_name  +  ' ' + last_name
print(full_name)

#escape sequences
print('something something.\nready ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t2\t20')
print('Day 3\t9\t23')
print('Day 4\t12\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('\"Hello, World!\"') # to write a double quote inside a single quote

#splicing
test = 'exam'
first_3 = test[0:3]
print(first_3)
last_3 = test[-3:]
print(last_3)

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2]
print(pto)  