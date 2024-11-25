def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    salary = float(line.strip())
                    salaries.append(salary)
                except ValueError:
                    continue

            total = sum(salaries)
            average = total / len(salaries) if salaries else 0

            return total, average
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0
    
result = total_salary("main.txt")
print(result)

