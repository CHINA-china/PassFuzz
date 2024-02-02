def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_file(file_name, lines):
    with open(file_name, 'w') as file:
        file.writelines(lines)

def generate_case_combinations(word):
    lowercase_combination = ''.join(c.lower() for c in word)
    titlecase_combination = word.capitalize()
    return [lowercase_combination, titlecase_combination]

def generate_new_combinations(words, birthday_dates):
    all_combinations = []

    for date in birthday_dates:
        for word in words:
            lowercase_word_combination = generate_case_combinations(word)[0]  # 取全小写组合
            titlecase_word_combination = word.capitalize()  # 取首字母大写

            all_combinations.append(f"{lowercase_word_combination}{date}\n")
            all_combinations.append(f"{titlecase_word_combination}{date}\n")

    return all_combinations

def main():
    file1_lines = read_file('./dict/name.txt')
    file2_lines = read_file('./dict/year.txt')
    file3_lines = read_file('./dict/symbol.txt')
    

    birthday_dates = []
    for month in range(1, 13):
        for day in range(1, 32):
            birthday_dates.append(f"{month:02d}{day:02d}")
    
    list2 = []
    for i in file2_lines:
        i= i.replace("\n","")
        list2.append(i)

    all_passwords = []
    weak = ["123", "123123", "12345", "123456", "666", "888", "999", "000", "111", "999999", "666666", "000000", "888888"]
    for line1 in file1_lines:
        line1 = line1.strip()
        words = line1.split()
        
        # 新的组合格式：首字母大写和全小写的1.txt 中的单词与所有日期直接组合
        new_combinations = generate_new_combinations(words, birthday_dates)
        all_passwords.extend(new_combinations)
        #首字母大写和全小写的1.txt 中的单词与2.txt直接组合
        list2_combination = generate_new_combinations(words, list2)
        all_passwords.extend(list2_combination)
        #首字母大写和全小写的1.txt 中的单词与常规弱口令直接组合
        weak_combination = generate_new_combinations(words, weak)
        all_passwords.extend(weak_combination)
        # 原有的组合格式：1.txt 中的单词（全小写和首字母大写）与所有日期直接组合
        combinations_list = [generate_case_combinations(word) for word in words]
        #1.txt 日期 3.txt组合
        for line3 in file3_lines:
            line3 = line3.strip()
            for date in birthday_dates:
                for combinations in zip(*combinations_list):
                    word_combination = ''.join(combinations)
                    all_passwords.append(f"{word_combination}{date}{line3}\n")
        #1.txt 2.txt 3.txt组合           
        for line3 in file3_lines:
            line3 = line3.strip()
            for line2 in file2_lines:
                line2 = line2.strip()
                for combinations in zip(*combinations_list):
                    word_combination = ''.join(combinations)
                    all_passwords.append(f"{word_combination}{line2}{line3}\n")     

        #1.txt 常规弱口令 3.txt组合
        for line3 in file3_lines:
            line3 = line3.strip()
            for w in weak:
                w = w.strip()
                for combinations in zip(*combinations_list):
                    word_combination = ''.join(combinations)
                    all_passwords.append(f"{word_combination}{w}{line3}\n") 
        
        

                    
        

    sorted_all_passwords = sorted(all_passwords, key=lambda x: (x.islower(), x.istitle(), x), reverse=True)

    write_file('UserPass.txt', sorted_all_passwords)

if __name__ == "__main__":
    main()
