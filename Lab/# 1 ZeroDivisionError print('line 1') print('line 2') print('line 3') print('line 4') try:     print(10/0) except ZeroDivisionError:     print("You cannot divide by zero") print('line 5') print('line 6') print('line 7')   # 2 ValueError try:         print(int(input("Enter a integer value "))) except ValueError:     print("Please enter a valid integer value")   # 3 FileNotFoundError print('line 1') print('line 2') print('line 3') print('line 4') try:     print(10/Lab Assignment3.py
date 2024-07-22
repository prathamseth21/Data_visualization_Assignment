# 1 ZeroDivisionError
print('line 1')
print('line 2')
print('line 3')
print('line 4')
try:
    print(10/0)
except ZeroDivisionError:
    print("You cannot divide by zero")
print('line 5')
print('line 6')
print('line 7')


# 2 ValueError
try:    
    print(int(input("Enter a integer value ")))
except ValueError:
    print("Please enter a valid integer value")


# 3 FileNotFoundError
print('line 1')
print('line 2')
print('line 3')
print('line 4')
try:
    print(10/0)

except ZeroDivisionError:
    print("You cannot divide by zero")
try:
  open("abc.txt")
except FileNotFoundError:
    print("File not found")
print('line 5')
print('line 6')
print('line 7')

# 4 Type Error
try:    
    print(int(input("Enter first integer value ")))
    print(int(input("Enter second integer value ")))
except ValueError:
    print("Please enter a valid integer value")
