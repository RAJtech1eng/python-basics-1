
def generate_random_password(length):
    import random
    alphabet='a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,,y,z'
    alphabet_upper=alphabet.upper()
    numbers='1,2,3,4,5,6,7,8,9,0'
    all_combine=alphabet+alphabet_upper+numbers 
    all_combineto_list = all_combine.split(",")

    random_password = ""
    for i in range(length):
       random_password += random.choice(all_combineto_list)
  
    print(f'PASSWORD is : {random_password}')


total_char = int(input("Enter total length: "))
generate_random_password(length=total_char)






    
    


