# Daily Coding Problem: Problem #2 [Hard]
#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?


def productList(list):

    newArray = []
    for index in range(0,len(list)):
        value = 1
        for i in range(0,len(list)):
            if index != i:
                value *= list[i]
        newArray.append(value)
    return newArray

def divisionList(list):

    newArray = []
    for index in range(0,len(list)):
        value = 0
        for i in range(0,len(list)):
            if index != i:
                if value == 0:
                    value = list[i]
                else:
                    value /= list[i]
        newArray.append("%.4f" % value)
    return newArray



if __name__ == '__main__':

    inputList = [1,2,3,4,5]
    print("Input array: ",inputList)
    newArray = productList(inputList)
    print("Product array:",newArray)
    newArray = divisionList(inputList)

    print("Division array:",newArray)
    print()

    inputList = [3, 2, 1]
    print("Input array: ", inputList)
    newArray = productList(inputList)
    print("Product array:", newArray)
    newArray = divisionList(inputList)
    print("Division array:", newArray)
    print()

