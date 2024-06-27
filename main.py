def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')

        if not start < end and (start.isalpha() and end.isalpha()):
            print("Input Error")
            continue
        result.clear()

        for i in range(ord(start), ord(end) + 1):
            result.append(chr(i))

        print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
        return result


if __name__ == '__main__':
    main()
