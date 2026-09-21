if __name__ == '__main__':
    students=[]
    scores=set()
    lowest=float('inf')
    second_lowest=float('inf')
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        new_list= [name,score]
        students.append(new_list)
        
    students1=sorted(students)
        
    for j in range(len(students1)):
        if students1[j][1]< lowest:
            second_lowest= lowest
            lowest=students1[j][1]
        elif students1[j][1]<second_lowest and students1[j][1]!=lowest:
            second_lowest=students1[j][1]
    for k in range(len(students1)):
        if students1[k][1]==second_lowest:
            print(students1[k][0])
        
        
        
        
        
        
