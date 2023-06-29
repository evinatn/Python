'''TASK
Given n print numbers 1 to n in the same line. '''

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end='')
