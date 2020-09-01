# Написать генератор, который принимает путь к файлу. 
# При каждой итерации возвращает md5 хеш каждой строки файла.


import hashlib
import json

class HashGenerator:
    def __init__(self, file):
        self.file = file


    def generate_hash(file):
        with open(file, encoding='utf-8') as countries_info:
            info = countries_info.read()
            str = json.loads(info)
            start = 0
            end = len(str)
            for item in range(start, end):
                data = hashlib.md5(str[item]['name']['common'].encode()).hexdigest()
                yield data
                start += 1

    
    for item in generate_hash('countries.json'):
        print(item)


    