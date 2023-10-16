import csv

def some_math_function(a:float, b:float):
    return (a ** b) + (a % b)

def some_file_operation_function(path:str, upper_case=False) -> str:
    """
    Returns the last line of the file on given path.

    Args:
        path (str): path of the file to check.
        upper_case (bool, optional): makes the returned line uppercase. Defaults to False.

    Returns:
        str: last line of the file
    """
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            pass
        else:
            if upper_case:
                line = line.upper()
    return line
        
            
if __name__ == '__main__':
    some_file_operation_function("resources/some_file.txt")
    print(some_math_function(5,10))
    print(some_math_function(5,5))
    print(some_math_function(1,5))