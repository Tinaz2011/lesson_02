season = {
    'Winter': [12, 1, 2],
    'Spring': [3, 4, 5],
    'Summer': [6, 7, 8],
    'Autumn': [9, 10, 11]
}
month = int(input('input month nummber'))
for key, value in season.items():
    if month in value:
        print(key)
        break
else:
    print('error')