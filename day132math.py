names = [
    ('mahesh','math'),
    ('Rohan','physics'),
    ('Bigyan','graph theory'),
    ('Ajay','math'),
    ('Bijay','physics'),
    ('Mandip','IT'),
    ('Aryan','math'),
    ('Ravi','IT'),
    ('David','graph theory'),
    ('Rober','abstract algebra')
    ]
IT_names=[name for name in names if name[1]=='graph theory']
for i in IT_names:
    print(i[0])
