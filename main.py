from parsing import parse

input_file_name = 'inputs/a_an_example.in.txt'
with open(input_file_name) as file:
    input_text = file.read()

contributors, projects = parse(input_text)
