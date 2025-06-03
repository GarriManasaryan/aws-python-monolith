import os

# for project structure and gpt questions

def print_tree(start_path='.', indent=''):
    for item in sorted(os.listdir(start_path)):
        full_path = os.path.join(start_path, item)
        print(f"{indent}{item}/" if os.path.isdir(full_path) else f"{indent}{item}")
        if os.path.isdir(full_path):
            print_tree(full_path, indent + '  ')

print_tree()

