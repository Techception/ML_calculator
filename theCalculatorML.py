#project for ML to figure ways to calculate a total of 8 via a combinations of mathematical operators 

#the program will attempt random combintions of numbers and operators 
#the program will adjust considering previous attempts e.g. was the total too large or too small and adjust accordingly 
#successful combinations will be included into a list of combinations 
#program should avoid repeating combinations and avoid non trivial combinations / unsimplified form 
#program should vary the number of operations used creatively 

# can use truth operator == 
# program will need to imagine combinations to be tested 

import random
#from colorama import Force

def imagine():
    # NUMBER OF OPERATIONS 
    OPERATIONS = int(random.choice(range(1, 4))) 
    #OPERATIONS = 1
    # program decides how many operations to try e.g. 1 = x + y (1 addition), 2 = x + y * z (1 additiona 1 multiply) 
    # wouldnt expect same operator in the same operatin level e.g. x + y + z (not ok if all real numbers as it could be simplified) 
    # however program might be able to benefit by telling non simplified forms 

    #WHAT NUMBERS TO OPERATE ON 
    NUM_OF_VALUES = OPERATIONS + 1 
    # e.g if 1 addition operation, there should be 2 values to add, x + y 
    ## todo: consider single number functions e.g. factorials.
    # we just need an array equal to this size
    # then ill just add a random number 
    # ill begin with positive real numbers for now but consider extending later 
    values = [int(random.choice(range(0, 9))) for i in range(NUM_OF_VALUES)]

    #SPECIFIC MATHEMATICAL OPERATORS TO TRY 
    SET_OF_OPERATORS = ['+','-','*','/','**','%']
    chosen_operators = random.choices(SET_OF_OPERATORS, k=OPERATIONS)

    #FORMULA
    # formula = [] 
    # I want the formula to obey order of operations 
    # Will explore creating the formula as a string that is comiled and executed 
    # could just turn the list into a string now 
    # turns out turning this to a string required turning the int into string first 
    #as noted via #formula = '.'.join(formula)
    # so better to use str throughout 
    formula = f"{values.pop()} "
    for i in range(NUM_OF_VALUES):
        #this loop will fail if OPERATIONS = 0 

        #print(f"values are now: {values}")
        formula = formula + f"{chosen_operators.pop()} "
        formula = formula + f"{values.pop()} "

        #would like to see the formula presented to the user in a more conventional fasion 
        #eg superscript powers, divide sign for divide, simplification 
        #print(len(values))
        if len(values) == 0:
            break
    #formula.rstrip()
    #print(formula)

    return formula.strip()

def testFormula(formula, ANSWER):
    loc = {} #the exec functions local variables produced 
    try: 
        exec(f"calculation = {formula}", None, loc)
        calculation = loc['calculation']
    except: 
        calculation = None

    test = (ANSWER == calculation)

    return test



def main():
    
    ANSWER = 8
    validFormulas = []
    for i in range(500):
        print(i)
        formula = imagine()
        TEST_QUESTION = f'{formula} = {ANSWER}'
        #print(TEST_QUESTION)

        if formula in validFormulas:
            continue 

        #TEST_QUESTION = f'{formula} = {ANSWER}'
        #test = testFormula(formula, ANSWER)
        if not(testFormula(formula, ANSWER)):
            continue 

        validFormulas.append(formula)
        #TEST_QUESTION = f'{formula} = {ANSWER}'
        print(TEST_QUESTION)
        #print(validFormulas)


print(__name__)
if __name__ == '__main__':
    main()
    #testFormula(imagine())
    #print(globals())
    #print(locals())
