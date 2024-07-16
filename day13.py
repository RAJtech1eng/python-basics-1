#create a function that reverse string;
def reverse_string(text):
    name=text
    reverse_string=''
    for i in range(len(name)-1,-1,-1):
        reverse_string = reverse_string + name[i]
    print(f'Reverse  is {reverse_string}')
    
reverse_string('hello')
reverse_string('clear')

    

