inputString = input("Test: ")

predicates = list(set(filter(lambda x: x.isalpha(), inputString)))
print(inputString)
print("Detected predicates:",predicates)
tautology = True
for testNo in range(2**len(predicates)):
    values = list("{0:b}".format(testNo).zfill(len(predicates)))
    testString = inputString
    for test_predicate in range(len(predicates)):
        testString = testString.replace(predicates[test_predicate]," "+values[test_predicate]+ " ")
    fixedInputString = testString.replace("∨"," or ").replace("∧"," and ").replace("¬"," not ").replace("→"," != True or ").replace("↔", " == ").replace("⊕","!=")
    result = eval(fixedInputString)
    print(fixedInputString+" = ",result)
    tautology = tautology and result
print(tautology)
