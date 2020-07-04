def main():
    file = open("file2call.txt", "r")
    file1 = file.readlines()
    for x in sorted(file1, key=lambda item: (len(item), item)):
        print(x)


if __name__ == '__main__':
    main()