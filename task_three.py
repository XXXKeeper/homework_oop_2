def read_file(local_path: str):
    with open(local_path, encoding='utf-8') as f:
        file_text = ''
        count_line = 0
        for line in f:
            count_line += 1
            file_text += line
    return [file_text, count_line, local_path]


def write_result_file(list_all_file_info: list):
    list_all_file_info.sort(key=lambda x: x[1])
    print(list_all_file_info)
    with open('result_task_three.txt', 'w', encoding='utf-8') as f:
        for file_info in list_all_file_info:
            f.write(str(file_info[2]) + '\n')
            f.write(str(file_info[1]) + '\n')
            f.write(file_info[0] + '\n')


def main():
    list_file1_info = read_file('1.txt')
    list_file2_info = read_file('2.txt')
    list_file3_info = read_file('3.txt')
    write_result_file([list_file1_info, list_file2_info, list_file3_info])


if __name__ == '__main__':
    main()
