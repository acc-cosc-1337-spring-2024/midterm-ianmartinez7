#add import

from question_a import get_sum_of_evens, menu


def menu_logic():
    while True:
        menu()
        user_menu_choice = int(input("Choose a option 1 - 2 please: "))
        if user_menu_choice == 1:
            user_num_choice = int( input('Pick a number to find the sum of all even numbers: '))
            print ('The sum of all even numbers from ', user_num_choice, 'is', get_sum_of_evens(user_num_choice))

            ask_another = input("Return to the main menu? (yes/no) ")
            if ask_another != 'yes':
                print ("goodbye")
                exit()

        elif user_menu_choice == 2:
            print('Exiting program, goodbye')
            exit()


menu_logic()




        
        


