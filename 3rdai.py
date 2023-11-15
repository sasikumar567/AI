from collections import deque

def water_jug_problem(max_jug1, max_jug2, target):
    visited = set()
    queue = deque([(0, 0)])  
    visited.add((0, 0))

    while queue:
        current = queue.popleft()

        if target in current:
            return current

        jug1, jug2 = current

        if (max_jug1, jug2) not in visited:
            queue.append((max_jug1, jug2))
            visited.add((max_jug1, jug2))

        if (jug1, max_jug2) not in visited:
            queue.append((jug1, max_jug2))
            visited.add((jug1, max_jug2))


        if (0, jug2) not in visited:
            queue.append((0, jug2))
            visited.add((0, jug2))

        if (jug1, 0) not in visited:
            queue.append((jug1, 0))
            visited.add((jug1, 0))

        pour_amount = min(jug1, max_jug2 - jug2)
        if (jug1 - pour_amount, jug2 + pour_amount) not in visited:
            queue.append((jug1 - pour_amount, jug2 + pour_amount))
            visited.add((jug1 - pour_amount, jug2 + pour_amount))

        pour_amount = min(jug2, max_jug1 - jug1)
        if (jug1 + pour_amount, jug2 - pour_amount) not in visited:
            queue.append((jug1 + pour_amount, jug2 - pour_amount))
            visited.add((jug1 + pour_amount, jug2 - pour_amount))

max_jug1 = 4  
max_jug2 = 3  
target = 2    

result = water_jug_problem(max_jug1, max_jug2, target)
if result:
    print(f"Target of {target} achieved with {result}")
else:
    print(f"Target of {target} cannot be achieved with these jug sizes.")
