# *******************************************************
# Ege Ozguroglu (eo2464)
# effects_tester file (includes main function)
# Midterm
# ENGI E1006
# *******************************************************

#import methods from effects.py; no need for the utility functions that aid the main functions. 

from effects import object_filter, shades_of_gray, horizontal_flip

def main():
    """ main function """
    print("Welcome to the Portable Pixmap (PPM) Editor!")
    functionSelection  = input("Please enter 1 for object filtering, 2 for grayscale conversion, and 3 to horizontally flip an image: ") 
    
    #flexibly find the effect number in substrings of the user input. 
    if "1" in functionSelection:
        #prompt user for 3 input files.
        filename_1 = input("Please enter name of file 1: ")
        filename_2 = input("Please enter name of file 2: ")
        filename_3 = input("Please enter name of file 3: ")
        output = input("Please enter output file name: ")
        
        object_filter(filename_1, filename_2, filename_3, output)
        
    elif "2" in functionSelection:
        filename_1 = input("Please enter file name: ")
        output = input("Please enter output file name: ")
        
        shades_of_gray(filename_1, output)
        
    elif "3" in functionSelection:
        filename_1 = input("Please enter file name: ")
        output = input("Please enter output file name: ")
        
        horizontal_flip(filename_1, output)
    else:
        print("Please enter a valid selection: ")
    
    print(output + " was created. Thanks for using the Portable Pixmap (PPM) Editor!")
        
if __name__ == "__main__":
    main()

#calling the main function.
main()

