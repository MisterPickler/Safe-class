#Maxwell Parker
#Assignment 10.1: Your Own Class
#This code is a sample script for a class that creates a safe to store your belongings

#importing time module
import time
#importing randint from random module
from random import randint

'''Safe class'''
class Safe:
    #initializing count, which adds 1 to the current pin after every iteration
    count = 0
    #initializing starting number, the beginning number for code_breaker to start iterating from
    start_num = "0"
    #initializing random numbers which determine whether the trapped_safe function occurs and what it returns
    rand_num = randint(1,2)
    second_rand_num = randint(1,2)
    
    #constructor method
    def __init__(self, pin="1234", color="Black", contents="nothing"):
        #initializing color of safe
        self.__color = color
        #initializing pin number for use in code_breaker function
        self.__pin = pin
        #initializing code range, the highest number to iterate to in code_breaker
        self.__code_range = int("1" + (len(self.__pin) * "0"))
        #initializing contents of safe
        self.__contents = contents
    
    #get_color function: returns color of safe
    def get_color(self):
        return self.__color
    #set_color function: sets the color of the safe
    def set_color(self, color):
        self.__color = color
    #get_contents function: returns contents of safe
    def get_contents(self):
        return self.__contents
    #set_contents function: sets the contents of the safe
    def set_contents(self, contents):
        self.__contents = contents
    
    #code_breaker function: takes the pin number, iterates through all possible number combinations of pin length until the pin is found
    def code_breaker(self):
        #creates a start time for the beginning time of the function
        start = time.time()
        #iterates through each number combination in code range
        for i in range(self.__code_range):
            #iterates through each number in starting number
            for num in Safe.start_num:
                #creates a pin number that increases by 1 every iteration, with leading zeros the length of the original pin
                current_pin = str(int(Safe.start_num) + Safe.count).zfill(len(self.__pin))
            #if the iterated pin is the same as the inputted pin
            if current_pin == self.__pin:
                #creates an end time for the end of the function
                end = time.time()
                #total time for function to finish
                total_time = round((end - start), 3)
                #if the total time < 0.001 seconds
                if (end-start) < 0.001:
                    #return string with current pin
                    return f"Safe unlocked! The code is {current_pin}. \ntime taken to crack code: < 0.001 seconds"
                else:
                    #return string with current pin and total time for code to be found
                    return f"Safe unlocked! the code is {current_pin}. \ntime taken to crack code: {total_time} seconds"              
            else:
                #adds 1 to the count
                Safe.count += 1
            #prints each iterated pin on the same line until code is found
            print(f"Current number: {current_pin}", end="\r")
    
    #trapped_safe function: returns string saying the safe was trapped, counts down from 10 to 0, returns string saying "BOOM!" or "Just kidding!" depending on second_rand_num
    def trapped_safe(self):
        print("The safe was trapped...Dear God...")
        #iterates through each number in this range from 10 to -1, counting down
        for i in range(10, -1, -1):
            #prints iterated number denoting time till explosion, is replaced by next iterated number until finished
            print(f"explosion in {i}...", end="\r")
            #stops counting for 1 second
            time.sleep(1)
        #if the second random number is 1
        if Safe.second_rand_num == 1:
            #explosion
            return "\nBOOM!"
        #the second random number is not 1
        else:
            #prank trapped safe
            return "\nJust kidding!"


'''main function'''
def main():
    #calls safe class without pin input argument
    color_call = Safe()
    #calls set_color function to change the safe's color to white
    color_call.set_color("White")
    #returns color of safe
    print(f"Safe color: {color_call.get_color()}")
    #asks user to input PIN number
    pin_prompt = input("Type a PIN number here: ")
    #try statement to handle errors
    try:
        #if pin_prompt can be cast into an int and is greater than or equal to zero
        if int(pin_prompt) >= 0:
            #calls safe class with pin input argument
            call_class = Safe(pin_prompt)
            #prints code_breaker function
            print(call_class.code_breaker())
            #if the random number in the Safe class is 2
            if Safe.rand_num == 2:
                #print the trapped safe function
                print(call_class.trapped_safe())
            #if the random number in the Safe clas isn't 2
            else:
                #calls set_contents function with a list of items as input
                call_class.set_contents(["$3000", "stuffed teddy bear", "3 gold bars", "family photo"])
                #if the type of the contents in safe is a string
                if type(call_class.get_contents()) == str:
                    #prints contents of safe
                    print(f"contents of safe: {call_class.get_contents()}")
                #if the type of contents in safe is a list
                elif type(call_class.get_contents()) == list:
                    #adds each entry in the list of contents to a string, separated by ", "
                    contents_string = ", ".join(call_class.get_contents())
                    #prints contents of safe
                    print(f"contents of safe: {contents_string}")
                #if the contents in the safe are neither list nor string
                else:
                    print("The contents you set is invalid. The contents must be a string or a list containing only strings.")
                    return None
        #pin_prompt is not greater than or equal to zero
        else:
            print("The PIN number you entered is invalid. The PIN number must be a number that is greater than or equal to 0")
            return None
    #an error was raised because pin_prompt couldn't be cast as an int
    except:
        print("The PIN number you entered is invalid. The PIN number must be a number that is greater than or equal to 0")
        return None
    

'''calling main'''
if __name__ == "__main__":
    main()