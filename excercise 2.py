def maximum(lst) :
    max_num = None
    for num in lst :
        if max_num == None or max_num < num :
            max_num = num
    return max_num   

def main() :
    lst1 = [1,2,3,4,20,80,124,190]
    print('The Maximum Number is : ' , maximum(lst1))
main()