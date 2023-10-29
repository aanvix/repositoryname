users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dict_users ={"Общее количество":0 , "Уникальные посещения" : 0}
total_number = len(users)
unique_visits = len(set(users))
dict_users["Общее количество"]=total_number
dict_users["Уникальные посещения"]=unique_visits
print(dict_users)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
