import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('directory', help='Path to directory with log files')
parser.add_argument('--text', help='Text for search')
args = parser.parse_args()


def read_log_file(file_path):
    with open(file_path, 'r') as log_file:
        for line in log_file.readlines():
            yield line


def find_searched_phrase(text, target_text):
    result_text = []
    words_list = text.split()
    for i, word in enumerate(words_list):
        if target_text in word:
            start_index = max(0, i - 5)
            end_index = min(len(words_list), i + 6)
            result_text = ' '.join(words_list[start_index:end_index])
    return result_text


found_log_list = []
files = [f for f in os.listdir(args.directory) if os.path.isfile(os.path.join(args.directory, f))]

for file in files:
    log_file_path = os.path.join(args.directory, file)
    for i, log_line in enumerate(read_log_file(log_file_path)):
        if args.text in log_line:
            found_log_list.append(log_line)
            print(f'Text to search: "{args.text}" found in file "{file}", line: {i + 1}')
            print(f'5 words before and after "{args.text}": ')
            print(find_searched_phrase(log_line, args.text))
            print('-------------------------------------------------------------------')
