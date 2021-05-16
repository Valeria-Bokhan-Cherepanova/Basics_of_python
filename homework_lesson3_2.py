

def my_func(name, surname, year, city, email, telephone):
     return f'Name - {name}; Surname - {surname}; Year - {year}; City - {city}; Email - {email}; Telephone - {telephone};'

name = input('State the name - ')
surname = input('State the surname - ')
year = input('State the year you were born- ')
city = input('State the city - ')
email = input('State the email - ')
telephone = input('State the phone number - ')


print(my_func(name=name, surname=surname, year=year, city=city, email=email, telephone=telephone))
