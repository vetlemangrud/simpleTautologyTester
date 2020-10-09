while True:

    inputString = input("(Empty to exit) Test: ")
    if inputString.strip() == "":
        break

    predicates = list(set(filter(lambda x: x.isalpha(), inputString)))
    print("Detected predicates:",predicates)
    tautology = True
    for testNo in range(2**len(predicates)):
        values = list("{0:b}".format(testNo).zfill(len(predicates)))
        testString = inputString
        for test_predicate in range(len(predicates)):
            testString = testString.replace(predicates[test_predicate]," "+values[test_predicate]+ " ")
        fixedInputString = testString.replace("∨"," or ").replace("∧"," and ").replace("¬"," not ").replace("→"," != True or ").replace("↔", " == ").replace("⊕","!=")
        result = eval(fixedInputString)
        tautology = tautology and result
    print(tautology)
