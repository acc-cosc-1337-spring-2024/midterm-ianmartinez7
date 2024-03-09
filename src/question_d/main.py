#add import
from question_d import get_assessment_value, get_tax_assessement_value


def program():
    while True:
        print("Assessment value & Tax Assessment value calculator")
        user_input = float(input('Input the value of the property: '))

        assessment_value = get_assessment_value(user_input)
        tax_assessment = get_tax_assessement_value(assessment_value)

        print ('Assessment value: ', assessment_value)
        print ('Tax Assessment value: ', tax_assessment)

        end_question = input ('Want to enter a new value? (yes/no): ')
        if end_question != 'yes':
            print ('exiting program')
            break

        




program()


