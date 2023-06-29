'''TASK
For a given number n print square of the positive numbers less then n in separate lines.
The list of non-negative integers that are less than 3 is [0,1,2]. Print the square of each number on a separate line.
OUTPUT:
0
1
4'''

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i*i)
