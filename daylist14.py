# # names = [1,2,3,4,5,6,7,8]
# # even_num=[x for x in names if x%2==0]
# # print(even_num)
# #find all names starting with A
# names=['Anish','Binod','Ratna','Suman','Aryan','Bibek']
# start=[name for name in names if name[0].lower() =='a']
# print(start)

#ask user to enter todo and orint all todo

total_todo=int(input('Enter total todo : '))
todos=[]

#ask
for i in range(0,total_todo):
    todo=input(f'Enter  todo{i+1} : ')
    todos.append(todo)
#display
for todo in todos:
    print(todo)




