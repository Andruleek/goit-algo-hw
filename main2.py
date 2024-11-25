def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    try:
                        cat_id = int(parts[0])
                        name = parts[1].strip()
                        age = int(parts[2])
                        cats_info.append({
                            'id': cat_id,
                            'name': name,
                            'age': age
                        })
                    except ValueError:
                        print(f"Помилка в рядку: {line.strip()} (невалідні дані)")
                else:
                    print(f"Пропущений рядок: {line.strip()} (недостатньо даних)")
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Невідома помилка: {e}")
    
    return cats_info


cats = get_cats_info('cats.txt')
print(cats)
