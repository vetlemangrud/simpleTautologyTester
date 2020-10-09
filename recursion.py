import re #Regex library
regexPattern = re.compile('a(\d+)')

print("Recursion relation (with variables 'a1' for a_-1, 'a2' for a_-2 etc)")
print("Example: an = a1 + 12 * a2")
print("Use multiplication sign '*'")
relation = input("an = ")
givenA = input("Given values separated by comma (a_0, a_1 ...): ").split(",")

def a(n):
    if int(n) < len(givenA):
        return int(givenA[int(n)])
    else:
        expression = regexPattern.sub("a("+str(n)+"-\g<1>)", relation)
        return eval(expression)

while True:
    userN = input("(Empty to exit) n: ")
    if userN.strip() == "":
        break
    else:
        print(a(userN))

