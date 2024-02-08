def sum_of_products(list1, list2):
    score = 0
    if len(list1) != len(list2):
       print("Error")
    else:
        for i in range(0, len(list1)):
             score += int(list1[i]) * int(list2[i])
        return score

if __name__ == '__main__':
   list1 = input().split()
   list2 = input().split()
   print(sum_of_products(list1, list2))
#test