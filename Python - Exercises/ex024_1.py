city = input('Em que cidade você nasceu? ').strip().lower().replace(' ', '')
if city[0:5] == 'santo' or city[0:5] == 'santa':
    print(f'A cidade {city} começa com "Santo" ou "Santa"? True ')
else:
    print(f'A cidade {city} começa com "Santo" ou "Santa"? False ')