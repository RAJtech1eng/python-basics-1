def password_gen():
    import random
    password="nswjndmbfjesbdcmnbvjhsdbcjzx0p138927498329%$$@$%^%&*^%#"
    a="".join(random.sample(password,9))
    print(f"Your password is  : {a}")
password_gen()
