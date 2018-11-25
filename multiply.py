import sys

def multiply_by_two(nums):
    return list(map(lambda num: num*2, nums))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # only takes integers for the sake of simplicity
        print('Usage: python multiply <integers seperated by SPACE>')
    else:
        nums = []
        for arg in sys.argv[1:]:
            nums.append(int(arg))
        print(multiply_by_two(nums))