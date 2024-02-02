def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def write_file(file_name, lines):
    with open(file_name, 'w') as file:
        file.writelines(lines)

def generate_case_combinations(word):
    # 生成全小写和首字母大写两种组合
    lowercase_combination = ''.join(c.lower() for c in word)
    titlecase_combination = word.capitalize()
    return [lowercase_combination, titlecase_combination]
    
def main():
    # 读取1.txt、2.txt和3.txt的内容
    file1_lines = read_file('./dict/name.txt')
    file2_lines = read_file('./dict/symbol.txt')
    file3_lines = read_file('./dict/num.txt')

    # 拼接1、2、3的内容
    merged_lines_1_2_3 = set()  # 使用集合来存储唯一的密码组合
    for line1 in file1_lines:
        line1 = line1.strip()

        # 对每个单词的全小写和首字母大写两种组合
        words = line1.split()
        combinations_list = [generate_case_combinations(word) for word in words]

        # 将全小写和首字母大写的两种组合进行拼接
        for line2 in file2_lines:
            line2 = line2.strip()
            for line3 in file3_lines:
                line3 = line3.strip()
                for combinations in zip(*combinations_list):
                    word_combination = ''.join(combinations)
                    merged_lines_1_2_3.add(f"{word_combination}{line2}{line3}\n")

    # 对最终结果按照规则排序
    sorted_merged_lines_1_2_3 = sorted(merged_lines_1_2_3, key=lambda x: (x.islower(), x.istitle(), x), reverse=True)

    # 拼接1和3的内容
    merged_lines_1_3 = set()  # 使用集合来存储唯一的密码组合
    for line1 in file1_lines:
        line1 = line1.strip()

        # 对每个单词的首字母大写进行组合
        words = line1.split()
        titlecase_combinations = [word.capitalize() for word in words]

        for line3 in file3_lines:
            line3 = line3.strip()
            
            # 原始拼接规则
            for titlecase_combination in titlecase_combinations:
                merged_lines_1_3.add(f"{titlecase_combination}{line3}\n")
            
            # 新的拼接规则 1+3+！
            for titlecase_combination in titlecase_combinations:
                merged_lines_1_3.add(f"{titlecase_combination}{line3}!\n")
            
            # 新的拼接规则 1+3+.
            for titlecase_combination in titlecase_combinations:
                merged_lines_1_3.add(f"{titlecase_combination}{line3}.\n")

    # 对最终结果按照规则排序
    sorted_merged_lines_1_3 = sorted(merged_lines_1_3, key=lambda x: (x.islower(), x.istitle(), x), reverse=True)


    # 拼接全小写和3的内容
    merged_lines_lowercase_3 = set()  # 使用集合来存储唯一的密码组合
    for line1 in file1_lines:
        line1 = line1.strip()

        words = line1.split()
        for line3 in file3_lines:
            line3 = line3.strip()
            for word in words:
                lowercase_word = word.lower()
                merged_lines_lowercase_3.add(f"{lowercase_word}{line3}\n")

    # 对最终结果按照规则排序
    sorted_merged_lines_lowercase_3 = sorted(merged_lines_lowercase_3, key=lambda x: (x.islower(), x.istitle(), x), reverse=True)

    # 合并并去重所有结果
    unique_combined_lines = set(sorted_merged_lines_1_3 + sorted_merged_lines_1_2_3 + sorted_merged_lines_lowercase_3)

    # 对最终结果按照规则排序
    sorted_combined_lines = sorted(unique_combined_lines, key=lambda x: (x.islower(), x.istitle(), x), reverse=True)

    # 写入到文件
    write_file('mini.txt', sorted_combined_lines)

if __name__ == "__main__":
    main()
