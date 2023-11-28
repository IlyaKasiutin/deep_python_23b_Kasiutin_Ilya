# Тестирование производительности
С помощью faker сделано 20000 json-файлов следующего типа:
```json
{
"password": "password@123", 
"email": "nicholas14@example.com", 
"username": "Hayley", 
"first_name": "Hayley", 
"last_name": "Ortiz", 
"phone": 9734795598, 
"city": "Lorishire", 
"about": "This_is_a_sample_text_about"
}
```
Каждый файл открывался методом json.load(), к нему применялся метод dumps(), а к полученному результату применялся метод loads().
В итоге вот, что получилось:
![Alt text](readme_files/image.png)

# Генерация тестовых JSON
```bash
python3 generator.py
```
Будет создана папка jsons с 20000 файлами.