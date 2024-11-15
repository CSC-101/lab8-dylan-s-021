# Task 2

def main():
    try:
        filename = input("Enter complete file name of file whose contents you want to see: ")
        infile = open(filename, 'r')
        sums = []
        for line in infile:
            line = line.rstrip("\n")
            numbers = line.split()
            sum = float(numbers[0]) + float(numbers[1])
            sums.append(sum)
        print(sums)
        infile.close()
    except IOError as e:
        print("Error - ", e)

main()
