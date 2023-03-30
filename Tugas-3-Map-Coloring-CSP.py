import copy

# Graph definition
variables = ['Western Australia', 'Northern Territory', 'South Australia', 'Queensland', 'New South Wales', 'Victoria', 'Tasmania']
domains = {
    'Western Australia': ['red', 'green', 'blue'],
    'Northern Territory': ['red', 'green', 'blue'],
    'South Australia': ['red', 'green', 'blue'],
    'Queensland': ['red', 'green', 'blue'],
    'New South Wales': ['red', 'green', 'blue'],
    'Victoria': ['red', 'green', 'blue'],
    'Tasmania': ['red', 'green', 'blue']
}
neighbors = {
    'Western Australia': ['Northern Territory', 'South Australia'],
    'Northern Territory': ['Western Australia', 'South Australia', 'Queensland'],
    'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
    'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
    'New South Wales': ['Queensland', 'South Australia', 'Victoria'],
    'Victoria': ['South Australia', 'New South Wales', 'Tasmania'],
    'Tasmania': ['Victoria']
}

# Constraint function to check if neighboring nodes have different colors
def constraint(var, value, assignment):
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

# Backtracking algorithm
def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(assignment)
    for value in order_domain_values(var, assignment):
        if constraint(var, value, assignment):
            assignment[var] = value
            result = backtrack(assignment)
            if result is not None:
                return result
            del assignment[var]
    return None

# Helper function to select an unassigned variable
def select_unassigned_variable(assignment):
    for variable in variables:
        if variable not in assignment:
            return variable

# Helper function to order the domain values
def order_domain_values(var, assignment):
    return domains[var]

# Helper function to check if the solution is valid
def check_solution(solution):
    for variable in solution:
        for neighbor in neighbors[variable]:
            if neighbor in solution and solution[variable] == solution[neighbor]:
                return False
    return True

# Main function
if __name__ == '__main__':
    solution = backtrack({})
    if solution is None:
        print('No solution found')
    else:
        print(solution)
