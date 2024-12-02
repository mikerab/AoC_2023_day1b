masterCalibration = 0
numberOfLines = 0

# Open a document
doc = open('input.txt', 'rt')

for line in doc:
    # Read a line
    # This is wrong, line has already been read // currLine = doc.readline()
    numberOfLines = numberOfLines + 1
    print(line)

    firstNumber = 0
    calibrationNumber = 0
    listOfFirstLetters = ['o','t','f','s','e','n']

    # Start reading each character in order and if it's a number
    for curr_index, char in enumerate(line):

        if char.isnumeric():
            # multiply by 10, store it and stop
            firstNumber = int(char) * 10
            print(f'firstNumber is {firstNumber}')
            break
        # if it's not numeric, check for a spelled out one.
        elif char in listOfFirstLetters:
            match char:
                case 'o':
                    # check for 'one' by using the current index
                    if line[curr_index:curr_index + 3] == 'one':
                        firstNumber = 1 * 10
                        break
                case 't':
                    # check for 'two' and 'three'
                    if line[curr_index:curr_index + 3] == 'two':
                        firstNumber = 2 * 10
                        break
                    elif line[curr_index:curr_index + 5] == 'three':
                        firstNumber = 3 * 10
                        break
                case 'f':
                    # check for 'four' and 'five'
                    if line[curr_index:curr_index + 4] == 'four':
                        firstNumber = 4 * 10
                        break
                    elif line[curr_index:curr_index + 4] == 'five':
                        firstNumber = 5 * 10
                        break
                case 's':
                    # check for 'six' and 'seven'
                    if line[curr_index:curr_index + 3] == 'six':
                        firstNumber = 6 * 10
                        break
                    elif line[curr_index:curr_index + 5] == 'seven':
                        firstNumber = 7 * 10
                        break
                case 'e':
                    # check for 'eight'
                    if line[curr_index:curr_index + 5] == 'eight':
                        firstNumber = 8 * 10
                        break
                case 'n':
                    # check for 'nine'
                    # print(line[curr_index:curr_index+4])
                    if line[curr_index:curr_index + 4] == 'nine':
                        firstNumber = 9 * 10
                        break
    if firstNumber == 0:
        print('ERROR!!!! firstNumber is still zero')

    # Now start from the end of the line and reverse order and find that number.

    for rev_index, char in enumerate(reversed(line)):
        # print(f'curr_index is {len(line) - curr_index}')
        curr_index = (len(line) - 1) - rev_index
        if char.isnumeric():
            calibrationNumber = firstNumber + int(char)
            print(f'calibrationNumber is {calibrationNumber}')
            break
        # if it's not numeric, check for a spelled out one.
        elif char in listOfFirstLetters:
            match char:
                case 'o':
                    # check for 'one' by using the current index
                    if line[curr_index:curr_index + 3] == 'one':
                        calibrationNumber = firstNumber + 1
                        break
                case 't':
                    # check for 'two' and 'three'
                    if line[curr_index:curr_index + 3] == 'two':
                        calibrationNumber = firstNumber + 2
                        break
                    elif line[curr_index:curr_index + 5] == 'three':
                        calibrationNumber = firstNumber + 3
                        break
                case 'f':
                    # check for 'four' and 'five'
                    if line[curr_index:curr_index + 4] == 'four':
                        calibrationNumber = firstNumber + 4
                        break
                    elif line[curr_index:curr_index + 4] == 'five':
                        calibrationNumber = firstNumber + 5
                        break
                case 's':
                    # check for 'six' and 'seven'
                    if line[curr_index:curr_index + 3] == 'six':
                        calibrationNumber = firstNumber + 6
                        break
                    elif line[curr_index:curr_index + 5] == 'seven':
                        calibrationNumber = firstNumber + 7
                        break
                case 'e':
                    # check for 'eight'
                    if line[curr_index:curr_index + 5] == 'eight':
                        calibrationNumber = firstNumber + 8
                        break
                case 'n':
                    # check for 'nine'
                    # print(line[curr_index:curr_index+4])
                    if line[curr_index:curr_index + 4] == 'nine':
                        calibrationNumber = firstNumber + 9
                        break

    # Add the calibration number to the master number
    masterCalibration = masterCalibration + calibrationNumber
    print(f'masterCalibration is {masterCalibration}')
    # Read the next line and repeat until end of document

# Close the document
doc.close()

# print the master number
print(f'Master Calibration Number is {masterCalibration} based on {numberOfLines} lines')