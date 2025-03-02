def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function()
my_function("Brazil")

#To specify that a function can have only positional arguments, add , / after the arguments

#But when adding the , / you will get an error if you try to send a keyword argument

#To specify that a function can have only keyword arguments, add *, before the arguments

#But with the *, you will get an error if you try to send a positional argument:

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)