'''def hanoi(disks, source, helper, destination):
    if disks == 1:
        print('disk {} moved from tower {} to tower {}' .format(disks, source, destination))
        return
    hanoi(disks-1,source,destination,helper)
    print('disk {} moved from tower {} to tower {}'.format(disks, source, destination))
    hanoi(disks-1,helper,source, destination)

disks = int (input('enter the size of disks : '))
hanoi(disks, 'A','B','C')'''

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        # If there is only one disc, move it directly to the target pole
        print("Move disc",n, " from source", source, "to target", target)
        return
    else:
        # Move all discs except the bottom one to the auxiliary pole
        tower_of_hanoi(n - 1, source, target, auxiliary)
        # Move the bottom disc to the target pole
        print("Move disc", n, "from source", source, "to target", target)
        # Move the discs from the auxiliary pole to the target pole
        tower_of_hanoi(n - 1, auxiliary, source, target)

# Test the function with 3 discs
tower_of_hanoi(3, 'A', 'B', 'C')