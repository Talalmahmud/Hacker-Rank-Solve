# Enter your code here. Read input from STDIN. Print output to STDOUT

r_date = list(map(int, input().rstrip().split()))
due_date = list(map(int, input().rstrip().split()))
fine = 0

if due_date[2] < r_date[2]:
    fine =10000
elif r_date[2] == due_date[2]:
    if due_date[1] < r_date[1]:
        fine = 500*(r_date[1]-due_date[1])
    elif due_date[0] < r_date[0]:
        fine = 15*(r_date[0]-due_date[0])


print(fine)
