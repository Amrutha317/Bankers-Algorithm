def main():
    pr = int(input("Enter the No. of processes : "))
    resources = int(input("Enter the No. of resources : "))
    max_r= [int(i) for i in input("Enter maximum resources : ").split()] #

    print("\n-*-*-*-- Enter the allocated resources for processes p1 to pn --*-*-*-*--")
    currently_allocated = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(pr)]

    print("\n-*-*-*-*-- Enter maximum resources for processes p1 to pn *-*-*-*-*- --")
    max = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(pr)]

    alloc = [0] * resources
    running = [True] * pr

    for i in range(pr):
        for j in range(resources):
            alloc[j] += currently_allocated[i][j]
    print(f"\nTotal allocated resources : {alloc}")

    available = [max_r[i] - alloc[i] for i in range(resources)]##Initially available
    print(f"Total available resources : {available}\n")

    count = pr
    while count != 0:
        safe = False
        for i in range(pr):
            if running[i]:
                executing = True
                for j in range(resources):
                    if max[i][j] - currently_allocated[i][j] > available[j]:##Need matrix
                        executing = False
                        break
                if executing:
                    print(f"P {i + 1} is executing")
                    running[i] = False
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("Processes are in unsafe state!")
            break

        print(f"Processes are in Safe state .\n Available resources are : {available}\n")
if __name__ == '__main__':
    main()