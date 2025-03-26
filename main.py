def filter_lines(input_file, keyword, output_file="filtered.txt"):
    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                if keyword in line:
                    outfile.write(line)
        print(f"Рядки з ключовим словом '{keyword}' записані у файл '{output_file}'.")
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте правильність шляху.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    input_filename = input("Введіть ім'я вхідного файлу: ")
    search_keyword = input("Введіть ключове слово: ")
    filter_lines(input_filename, search_keyword)