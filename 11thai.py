class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, var, assignment, value):
        for constraint in self.constraints:
            if var in constraint:
                other_var = constraint[0] if var != constraint[0] else constraint[1]
                if other_var in assignment:
                    if not self.constraint_satisfied(value, assignment[other_var]):
                        return False
        return True

    def constraint_satisfied(self, value1, value2):
        return value1 != value2

    def backtracking_search(self):
        return self.backtrack({})

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        var = self.select_unassigned_variable(assignment)

        for value in self.domains[var]:
            if self.is_consistent(var, assignment, value):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]

        return None

    def select_unassigned_variable(self, assignment):
        unassigned = [var for var in self.variables if var not in assignment]
        return unassigned[0]

# Example usage:

variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domains = {v: ['Red', 'Green', 'Blue'] for v in variables}
constraints = [('WA', 'NT'), ('WA', 'SA'), ('NT', 'SA'), ('NT', 'Q'), ('SA', 'Q'), ('SA', 'NSW'),
               ('SA', 'V'), ('Q', 'NSW'), ('NSW', 'V')]

map_coloring_csp = MapColoringCSP(variables, domains, constraints)
solution = map_coloring_csp.backtracking_search()

if solution is not None:
    print("Solution found:")
    for var, color in solution.items():
        print(f"{var}: {color}")
else:
    print("No solution found.")
