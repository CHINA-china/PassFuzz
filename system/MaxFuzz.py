def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def write_file(file_name, lines):
    with open(file_name, 'w') as file:
        file.writelines(lines)

def generate_case_combinations(word):
    # 对单词的每个字母进行大小写组合
    combinations = []
    for i in range(2 ** len(word)):
        combination = ''.join(
            c.upper() if (i >> j) & 1 else c.lower() for j, c in enumerate(word)
        )
        combinations.append(combination)
    return combinations

def main():
    # 读取1.txt、2.txt和3.txt的内容
    file1_lines = read_file('./dict/name.txt')
    file2_lines = read_file('./dict/symbol.txt')
    file3_lines = read_file('./dict/num.txt')

    # 拼接1、2、3的内容
    merged_lines_1_2_3 = []
    for line1 in file1_lines:
        line1 = line1.strip()

        # 对每个单词的每个字母进行大小写组合
        words = line1.split()
        combinations_list = [generate_case_combinations(word) for word in words]

        # 获取所有小写的单词和首字母大写其他字母小写的单词
        lowercase_words = []
        capitalized_words = []
        for combinations in zip(*combinations_list):
            word_combination = ''.join(combinations)
            if word_combination.istitle():
                capitalized_words.append(word_combination)
            else:
                lowercase_words.append(word_combination)

        # 将所有小写的单词放在最前面，首字母大写其他字母小写的单词放在第二
        sorted_combinations = lowercase_words + capitalized_words
        for line2 in file2_lines:
            line2 = line2.strip()
            for line3 in file3_lines:
                line3 = line3.strip()
                for combination in sorted_combinations:
                    merged_lines_1_2_3.append(f"{combination}{line2}{line3}\n")

    # 对最终结果按照规则排序，并将拼接后的内容写入merged_password.txt
    merged_lines_1_2_3.sort(key=lambda x: (x.islower(), x.istitle(), x))
    merged_lines_1_2_3.reverse()  # 反转merged_lines_1_2_3列表


    # 拼接1、3的内容
    merged_lines_1_3 = []
    for line1 in file1_lines:
        line1 = line1.strip()

        # 对每个单词的每个字母进行大小写组合
        words = line1.split()
        combinations_list = [generate_case_combinations(word) for word in words]
        for line3 in file3_lines:
            line3 = line3.strip()
            for combinations in zip(*combinations_list):
                word_combination = ''.join(combinations)
                merged_lines_1_3.append(f"{word_combination}{line3}\n")

    # 对最终结果按照规则排序，并将拼接后的内容写入password_1_3.txt
    merged_lines_1_3.sort(key=lambda x: (x.islower(), x.istitle(), x))
    merged_lines_1_3.reverse()  # 反转merged_lines_1_3列表

    # Print to check if there's any data in the merged_lines_1_3 list

    # Combine both results into a single list while maintaining the order
    combined_lines = merged_lines_1_3 + merged_lines_1_2_3

    # Write the combined result to the password.txt file
    combined_lines.sort(key=lambda x: (x.islower(), x.istitle(), x))
    combined_lines.reverse()  # 反转combined_lines列表
    write_file('max.txt', combined_lines)

if __name__ == "__main__":
    main()
