# name = "Ali"
#
# age = 100
#
# actual_age = 105.25
#
# math = 5 + 3 * 32 / 4
#
# results = age + actual_age + math
#
# print(name)
# print(age)
#
# print(type(name))
# print(type(age))
# print(type(actual_age))
# print(math)
# print(results)

price = 8

print("Hello, welcome to Ali's coffee")
name = input("What is your name?\n")

print("Hello " + name + " ,thank you for coming in today!" + "What would you like to order?\n" + "Here's our menu:\n" + "Flat White\n" + "Latte\n" + "Hot Choc\n")
order = input()

# print("Great, how many " + order + " would you like?")
amount = input("How many would you like\n")
total = int(amount) * price
print("Thanks " + name + ", that will be " + amount + " coffees, totalling " + "$" + str(total))