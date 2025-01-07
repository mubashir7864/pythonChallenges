class mathUtils:
    @staticmethod
    def calculateSum(arrayNums):
        total = sum(arrayNums)
        print(total)

lis = [1,2,4,5,6,8]

mathUtils.calculateSum(lis)

m1 = mathUtils()
m1.calculateSum(lis)
