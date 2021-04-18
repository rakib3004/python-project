def count_substring(string, sub_string):
     i=0
     j=0
     count =0
     intSub=len(sub_string)
     pos=-2
     a = string

     while(pos<=len(string) or pos!=-1):
         pos =a.find(sub_string)
         print(pos)
         a = a[pos+1:]
         count= count+1

     return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)