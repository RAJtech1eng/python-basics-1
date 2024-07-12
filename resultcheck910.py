resultset= {
    '0090207A':'3',
    '0090208B':'3.5',
    '0090209C':'2.8',
    '0090210D':'3.2'
}
symbol_no = input('Enter symbol no : ')
result = ''

for i in resultset.keys():
    if symbol_no == i:
        result = resultset[i]
    else:
        result = ''
    break    

if result != '':
    print(f'your result is {result}')

else:
    print('youor symbol njmber not found')
