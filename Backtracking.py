def backtrack(solution, options):
    if is_complete(solution):
        process_solution(solution)
        return
    
    for option in options:
        if is_valid(option, solution):
            solution.append(option)
            backtrack(solution, options)
            solution.pop()
            
TARGET_LENGTH =5
def is_complete(solution):
    return len(solution) == TARGET_LENGTH  

def process_solution(solution):
    print(solution)

def is_valid(option, solution):
    return True  

# Example Usage
if __name__ == "__main__":
    initial_solution = [] 
    options = [1, 2, 3]    
    backtrack(initial_solution, options)
