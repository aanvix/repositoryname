inf_volume = 1.44
c = 1024 # TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
symbols = 25
one_ement= 4
inf_volume *= (c ** 2)
identical_books = inf_volume //(one_ement * symbols * lines * pages)
identical_books=int(identical_books)
print("Количество книг, помещающихся на дискету:", identical_books)
