# GridTraveler Problem,
# You begin in top left traveler on 2D grid
# and move only bottom-right corner
# No. of ways to reach the goal with deminesion m,n

def gridTraveler(m, n):
    '''
    Time: O(2**(m+n))
    Space:O(m+n)
    '''
    if(m == 1 and n == 1):
        return 1
    if(m == 0 or n == 0):
        return 0
    return gridTraveler(m-1, n)+gridTraveler(m, n-1)


print("Enter the Numbers: m  n ")
m, n = map(int, input().strip().split())
print(f'No. of ways are {gridTraveler(m, n)}')
