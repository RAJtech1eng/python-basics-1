atm_pin ='1234'
usere_pin =''
attempt=0
while atm_pin!= usere_pin:
    if attempt>0:
        print(f"invalid pincode.Total attempt {attempt}")
    
    

    
    
    usere_pin =input('enter atmpin : ')
    attempt = attempt + 1
print('Access granted.How much you want to withdraw?')
