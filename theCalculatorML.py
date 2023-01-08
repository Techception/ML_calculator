#project for ML to figure ways to calculate a total of 8 via a combinations of mathematical operators 

#the program will attempt random combintions of numbers and operators 
#the program will adjust considering previous attempts e.g. was the total too large or too small and adjust accordingly 
#successful combinations will be included into a list of combinations 
#program should avoid repeating combinations and avoid non trivial combinations / unsimplified form 
#program should vary the number of operations used creatively 

# can use truth operator == 
# program will need to imagine combinations to be tested 

import random

def imagine():
    # NUMBER OF OPERATIONS 
    OPERATIONS = int(random.random()*10) 
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
    values = [int(random.random()*10) for i in range(NUM_OF_VALUES)]
    #print(f"values are: {values}")
    #print(f"popped value is {values.pop(0)}")
    #print(f"values are now: {values}")
    # this will return non unique values.  
    # this could affect the simplification requirement 

    #SPECIFIC MATHEMATICAL OPERATORS TO TRY 
    SET_OF_OPERATORS = ['+','-','*','/','**']
    chosen_operators = random.choices(SET_OF_OPERATORS, k=OPERATIONS)

    #FORMULA
    # formula = [] 
    # I want the formula to obey order of operations 
    # Will explore creating the formula as a string that is comiled and executed 
    # could just turn the list into a string now 
    # turns out turning this to a string required turning the int into string first 
    #as noted via #formula = '.'.join(formula)
    # so better to use str throughout 
    formula = str() #'formula ='
    for i in range(NUM_OF_VALUES):
        #this loop will fail if OPERATIONS = 0 

        #print(f"values are now: {values}")
        #formula.append(values.pop()) # what values getting popped again? 
        formula = formula + f"{values.pop()} "

        if len(values) != 0:
            #formula.append(chosen_operators.pop())
            formula = formula + f"{chosen_operators.pop()} "
        
        #formula.strip()
        #print(formula)
        #would like to see the formula presented to the user in a more conventional fasion 
        #eg superscript powers, divide sign for divide, simplification 
        #print(len(values))
        if len(values) == 0:
            break
    #formula.rstrip()
    #print(formula)

    return formula.strip()


calculation = imagine()
ANSWER = 8
TEST_QUESTION = f'True or False, \n\t{calculation} = {ANSWER}\n'
test = compile(f"print(TEST_QUESTION, {ANSWER} == {calculation})", 'mulstring', 'exec')
# should have a variable string that is the code for the test condition 
# e.g. 8 == test.  
# where answer = 8. 
# so this should have arguments to allow for different answers at a future stage 
#print(test)
#calculation = compile()
answer = 8 
exec(test)
#print(test.strip())

#todo: consider this: 
#exec(calculation)
#print(_)  #not defined here 