#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
<<<<<<< HEAD
        num = 0
        for i in my_list:
            if num < x:
                print("{}".format(i), end='')
                num += 1
        print('')
        return num
    except SyntaxError:
        print("Error Syntax")
=======
        for i in range(x):
            print(my_list[i], end='')
            count += 1
    except IndexError:
        pass
    finally:
        print()  # Add a new line after printing elements
    return count
>>>>>>> 457f2b82613f6c52176e15c14c97e7029dd7f37d
