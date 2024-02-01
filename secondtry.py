def sum_of_products(list1, list2):
    score = 0
    if len(list1) != len(list2):
       print("Error")
    else:
        for i in range(0, len(list1)):
                score += list1(i) * list2(i)
                print(score)


if __name__ == '__main__':
   list1 = int(input()).split()
   list2 = int(input()).split()
   print(sum_of_products(list1, list2))