import pytest

def filter_lines(input_file, keyword, output_file="filtered.txt"):
    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                if keyword in line:
                    outfile.write(line)
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    input_filename = input("Введіть ім'я вхідного файлу: ")
    search_keyword = input("Введіть ключове слово: ")
    result = filter_lines(input_filename, search_keyword)
    if result is True:
        print(f"Рядки з ключовим словом '{search_keyword}' записані у файл 'filtered.txt'.")
    elif result is False:
        print("Файл не знайдено. Перевірте правильність шляху.")
    else:
        print(f"Сталася помилка: {result}")

@pytest.fixture
def sample_file(tmp_path):
    file_path = tmp_path / "test_input.txt"
    content = "Це тестовий рядок\nІнший рядок\nКлючове слово тут\nЩе один тестовий рядок\n"
    file_path.write_text(content, encoding="utf-8")
    return file_path

@pytest.mark.parametrize("keyword, expected_lines", [
    ("Ключове", "Ключове слово тут\n"),
    ("тестовий", "Це тестовий рядок\nЩе один тестовий рядок\n"),
    ("немає", "")
])
def test_filter_lines(sample_file, tmp_path, keyword, expected_lines):
    output_file = tmp_path / "filtered_output.txt"
    result = filter_lines(sample_file, keyword, output_file)
    assert result is True
    assert output_file.read_text(encoding="utf-8") == expected_lines