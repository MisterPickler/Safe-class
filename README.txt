# Safe-class
This repository contains a python program that models a Safe which can be brute-forced and might be trapped

Class documentation:
    description of class
        The Safe class creates a safe with a PIN number, color, and contents inside of the safe. This class includes functions to get and set the color and contents,
        as well as a code breaker function and a trapped safe function. The code breaker is brute-forcing its way to finding the PIN number that the user inputted. 
        The trapped safe function is a function that happens at random, stating that the safe was trapped and counting down until the explosion. 

    description of each of the class and data variables
        Class variables
        -count adds 1 to the current iterated pin in the code breaker function
        -start_num is a class variable that the code breaker function uses as the beginning number to start iterating from
        -rand_num is a random interger between 1 and 2. If rand_num is 2, the trapped safe function occurs.
        -second_rand_num is a random interger between 1 and 2. If second_rand_num is 1, the function returns a string that says "BOOM!" If second_rand_num is 2, 
        the function returns a string that says "Just kidding!"

        Data variables
        -self.__color is a data variable which represents the color of the safe. 
        -self.__pin is the PIN number which the user inputs in the demo program. 
        -self.__code_range is the highest number for the code breaker method to iterate to. It is calculated by the length of self.__pin being the number of 0's, with a 1 in the front
        -self.__contents is the items stored within the safe.

    description of each of the methods
        -The __init__ function is the constructor method. Arguments to input are pin, color, and contents. Inputting arguments is recommended, but not required as each argument has a default value. 
        If user doesn't input a safe color, the default value is "Black". If user doesn't input a PIN number, the default value is "1234". If user doesn't input any contents, the default value is "nothing".
        -The get_color function returns the color of the safe. This requires no arguments to be input.
        -The set_color function sets the color of the safe to the input color. Only requires one argument: color.
        -The get_contents function returns the contents of the safe. This requires no arguments to be input.
        -The set_contents function sets the contents of the safe to what the user inputs. This only requires the contents to be input.
        -The code_breaker function iterates through all possible number combinations from 0 to self.__code_range, adding 1 to the iterated pin after every iteration until the iterated pin equals the 
        input pin. When the iterated pin is equal to the input pin, the iterated pin is returned with the time it took for the function to complete. 
        -The trapped_safe function occurs at random, depending on the value of rand_num. When it occurs, a text is printed saying that the safe was trapped and a countdown appears to count until explosion.
        Whether this function returns the string "BOOM!" or "Just kidding!" is determined by the value of second_rand_num.
        No input arguments necessary. 


Demo program documentation:
    description of demo program
        In the demo program, there are two variables that call the Safe class: color_call and call_class. Color_call is used solely for setting and getting the color of the safe. Call_class is used for
        everything else. Next, the demo program asks the user to input a PIN number. Before anything else is called, try-except statements are used to handle any errors; specifically, any errors where 
        the user's pin cannot be casted as an interger. If an error occurs, an error statement is printed and None is returned. The demo program also checks if the user's PIN is an interger 
        greater than or equal to zero, if it is not then an error statement is printed and None is returned. If the PIN number is valid, then the call_class variable is created, which calls the Safe class
        with the PIN number as the argument. Then the code_breaker method is called and printed. Then the program checks if the rand_num variable is 2. If it is, then the trapped safe function is called
        and printed. If rand_num is not 2, then the contents are accessed. The set_contents method is called, with a list of items as the argument. Then the program asks if the contents are a string,
        which would occur if either the user didn't input anything, resulting in "nothing", the default value of contents, or the user input a string instead of a list. If it is a string, then 
        the get_contents method is called and printed. If it is a list, the get_contents method is called and each list entry is added to a string, separated by ", " and that string is returned. 
        If it is neither a string nor list, an error statement is printed and None is returned.

    instructions on how to run the demo program:
        To run the demo program, you need to first enter a PIN number when the program asks for one. This can be any number greater than or equal to zero. In other words, you can input as big of a number
        as you want, but you might be limited by your computer's power and you may have to wait a while for the code to be cracked. You can use the get-set methods for color and contents to access or 
        change either's values. 
