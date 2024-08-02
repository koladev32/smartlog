import argparse

def main():
    parser = argparse.ArgumentParser(description='Example CLI')
    parser.add_argument('-n', '--name', help='Your name')
    parser.add_argument('--age', type=int, help='Your age')

    args = parser.parse_args()

    print(f"Hello, {args.name}! You are {args.age} years old.")

if __name__ == '__main__':
    main()
