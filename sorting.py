import time
import random
import sys
import generatingTests

sys.setrecursionlimit(2147483647)

def insertionSort(arr):
    t1 = time.perf_counter()
    for i in range(1,len(arr)):
        k = arr[i]
        j=i-1
        while j>0 and arr[j]>k:
            stats[0]=stats[0]+1
            stats[1] = stats[1]+1
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=k
    t2=time.perf_counter()
    return t2-t1

def bubbleSort(arr):
    t1 = time.perf_counter() 
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            stats[0]+=1
            if arr[j]>arr[j+1]:
                stats[1]+=1
                a=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=a
    t2=time.perf_counter()
    return t2-t1

def improvedBubbleSort(arr):
    t1 = time.perf_counter() 
    swapped = 1
    i = len(arr)-1
    while i>=0 and swapped !=0:
    #for i in range(len(arr)-1,0,-1):
        swapped = 0
        for j in range(0,i):
            stats[0]+=1
            if arr[j]>arr[j+1]:
                stats[1]+=1
                a=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=a
                swapped =1
        i-=1
    t2=time.perf_counter()
    return t2-t1

def quickSort(arr,left,right):
    if left<right:
    #    mid = partition(arr,left,right)
    #    quickSort(arr,left,mid-1)
    #    quickSort(arr,mid+1,right)
        pivot=arr[right]
        i = left -1
        j = right
        while True:
            while arr[i+1] <pivot:
                i+=1
            i += 1
            while arr[j-1]> pivot:
                j-=1
            j -= 1
            if i>=j:
                break
            (arr[i],arr[j]) = (arr[j],arr[i])
        (arr[i],arr[right]) = (arr[right],arr[i])
        quickSort(arr,left,i-1)
        quickSort(arr,i+1,right)




def randomQuickSort(arr,left,right):
    if left<right:
    #    mid = partition(arr,left,right)
    #    quickSort(arr,left,mid-1)
    #    quickSort(arr,mid+1,right)
        r=random.randint(left,right)
        (arr[r],arr[right]) = (arr[right],arr[r])
        pivot = arr[right]
        i = left -1
        j = right
        while True:
            while arr[i+1] <pivot:
                i+=1
            i+=1
            while arr[j-1]> pivot:
                j-=1
            j-=1
            if i>=j:
                break
            (arr[i],arr[j]) = (arr[j],arr[i])
        (arr[i],arr[right]) = (arr[right],arr[i])
        randomQuickSort(arr,left,i-1)
        randomQuickSort(arr,i+1,right)

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], sep=None)
   # print()
    print()


def selectionSort(arr):
    t1 = time.perf_counter()
    for i in range(len(arr)-1):
        min =i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j
        temp = arr[min]
        arr[min]=arr[i]
        arr[i]=temp
    t2=time.perf_counter()
    return t2-t1

def mergeSort(arr,temp,left,right):
    #t1= time.perf_counter()
    if right>left:
        
        mid = (right+left)//2
        mergeSort(arr,temp,left,mid)
        mergeSort(arr,temp,mid+1,right)
        merge(arr,temp,left,mid+1,right)
    #else:
        #return time.perf_counter()-t1

def merge(arr,temp,left,mid,right):
    leftEnd = mid-1
    tempPos = left  
    size = right-left+1
    while left<=leftEnd and mid<=right:
        if arr[left]<=arr[mid]:
            temp[tempPos] = arr[left]
            tempPos+=1
            left+=1
        else:
            temp[tempPos]= arr[mid]
            tempPos +=1
            mid+=1
    while left<=leftEnd:
        temp[tempPos] = arr[left]
        left+=1
        tempPos+=1
    while mid<= right:
        temp[tempPos]= arr[mid]
        mid+=1
        tempPos+=1
    for i in range(size+1):
        arr[right] = temp[right]
        right-=1

stats=[0,0]

#def readFromFile(filename):
#    with open(filename, "r") as f:
#        l = f.readlines()
#        l2 = [eval(i) for i in l]
#        f.close()
#   runTest(l2,filename)

def countingSort(arr):
    t1 = time.perf_counter()
    max = 0
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]

    c=[ 0 for i in range(max+1)]
    for i in range(len(arr)):
        c[arr[i]]+=1
    for i in range(1,max+1):
        c[i]+=c[i-1]
    o = [0 for i in range(len(arr))]
    for i in range(len(arr)-1,0,-1):
        o[c[arr[i]]-1] =arr[i]
        c[arr[i]]-=1
    for i in range(len(arr)):
        arr[i]=o[i]
    return time.perf_counter()-t1

def specialCountingSort(arr,e):
    c=[0 for i in range(11)]
    for i in range(len(arr)):
        c[(arr[i]//e)%10]+=1
    for i in range(1,10):
        c[i]+=c[i-1]
    o=[0 for i in range(len(arr))]
    for i in range(len(arr)-1,0,-1):
        o[c[(arr[i]//e)%10]-1] = arr[i]
        c[(arr[i]//e)%10]-=1
    for i in range(len(arr)):
        arr[i]=o[i]

def radixSort(arr):
    t1 = time.perf_counter()
    max =arr[0]
    for i in range(1,len(arr)):
        if max<arr[i]:
            max = arr[i]
    e =1
    while max/e>0:
        specialCountingSort(arr,e)
        e*=10
    return time.perf_counter()-t1



def runTest(min,max,step):

    pref = ["BubbleSort","SelectionSort","InsertionSort","ImprovedBubbleSort","MergeSort","QuickSort","RandomQuickSort","CountingSort","RadixSorts"]

    mid = ["Random","Ascending", "Descending"]
    
    #i = 100
    p = 0
    switch = 1
    if max>10000:
        switch =0
        p=4
    while p<9:
        m=0
        while m<3:
            filename = pref[p]+mid[m]+f"{min}_"+f"{max}"+".csv"
            with open(filename,"w+") as f:
                f.write("Length,Time\n")
                if(p ==0 and switch):
                    if(m==0):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generatRandom(i)
                            r1 = bubbleSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==1):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateAscending(i)
                            r1 = bubbleSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==2):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateDescending(i)
                            r1 = bubbleSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                if(p ==1 and switch):
                    if(m==0):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generatRandom(i)
                            r1 = selectionSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==1):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateAscending(i)
                            r1 = selectionSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==2):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateDescending(i)
                            r1 = selectionSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                if(p ==2 and switch):
                    if(m==0):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generatRandom(i)
                            r1 = insertionSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==1):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateAscending(i)
                            r1 = insertionSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==2):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateDescending(i)
                            r1 = insertionSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                if(p ==3 and switch):
                    if(m==0):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generatRandom(i)
                            r1 = improvedBubbleSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==1):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateAscending(i)
                            r1 = improvedBubbleSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==2):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateDescending(i)
                            r1 = improvedBubbleSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                if(p ==4):
                    if(m==0):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generatRandom(i)
                            t1 = [0 for i in range(i)]
                            time1= time.perf_counter()
                            mergeSort(l1,t1,0,len(l1)-1)
                            r1 = time.perf_counter()- time1
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==1):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateAscending(i)
                            t1 = [0 for i in range(i)]
                            time1= time.perf_counter()
                            mergeSort(l1,t1,0,len(l1)-1)
                            r1 = time.perf_counter()- time1
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==2):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateDescending(i)
                            t1 = [0 for i in range(i)]
                            time1= time.perf_counter()
                            mergeSort(l1,t1,0,len(l1)-1)
                            r1 = time.perf_counter()- time1
                            f.write(f"{i},{r1}\n")
                            i=i+step
                if(p ==5):
                    if(m==0):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generatRandom(i)
                            t1 = time.perf_counter()
                            quickSort(l1,0,len(l1)-1)
                            r1 = time.perf_counter()-t1
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==1):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateAscending(i)
                            t1 = time.perf_counter()
                            quickSort(l1,0,len(l1)-1)
                            r1 = time.perf_counter()-t1
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==2):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateDescending(i)
                            t1 = time.perf_counter()
                            quickSort(l1,0,len(l1)-1)
                            r1 = time.perf_counter()-t1
                            f.write(f"{i},{r1}\n")
                            i=i+step
                if(p ==6):
                    if(m==0):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generatRandom(i)
                            t1 = time.perf_counter()
                            randomQuickSort(l1,0,len(l1)-1)
                            r1 = time.perf_counter()-t1
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==1):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateAscending(i)
                            t1 = time.perf_counter()
                            randomQuickSort(l1,0,len(l1)-1)
                            r1 = time.perf_counter()-t1
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==2):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateDescending(i)
                            t1 = time.perf_counter()
                            randomQuickSort(l1,0,len(l1)-1)
                            r1 = time.perf_counter()-t1
                            f.write(f"{i},{r1}\n")
                            i=i+step
                if(p ==7):
                    if(m==0):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generatRandom(i)
                            r1 = countingSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==1):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateAscending(i)
                            r1 = countingSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==2):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateDescending(i)
                            r1 = countingSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                if(p ==8):
                    if(m==0):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generatRandom(i)
                            r1 = radixSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==1):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateAscending(i)
                            r1 = radixSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
                    if(m==2):
                        i =min
                        while i<=max:
                            l1 = generatingTests.generateDescending(i)
                            r1 = radixSort(l1)
                            f.write(f"{i},{r1}\n")
                            i=i+step
            f.close()
            m+=1
        p+=1
 


def runTest3():
    x = int(input())
    resfilename = "resSize"+f"{x}"
    f1 =resfilename+"Random.csv"
    with open(f1,"w+") as f:
        i =0
        while i<7:
            if(i ==0):
                l1 = generatingTests.generatRandom(x)
                r1 = bubbleSort(l1)
                f.write(f"BubbleSort,{r1}\n")
            if(i ==1):
                l1 = generatingTests.generatRandom(x)
                r1 = selectionSort(l1)
                f.write(f"SelectionSort,{r1}\n")
            if(i ==2):
                l1 = generatingTests.generatRandom(x)
                r1 = insertionSort(l1)
                f.write(f"InsertionSort,{r1}\n")
            if(i ==3):
                l1 = generatingTests.generatRandom(x)
                r1 = improvedBubbleSort(l1)
                f.write(f"ImprovedBubbleSort,{r1}\n")
            if(i ==4):
                l1 = generatingTests.generatRandom(x)
                t1 = [0 for i in range(x)]
                time1= time.perf_counter()
                mergeSort(l1,t1,0,len(l1)-1)
                r1 = time.perf_counter()- time1
                f.write(f"MergeSort,{r1}\n")
            if(i ==5):
                l1 = generatingTests.generatRandom(x)
                t1 = time.perf_counter()
                quickSort(l1,0,len(l1)-1)
                r1 = time.perf_counter()-t1
                f.write(f"QuickSort,{r1}\n")
            if(i ==6):
                l1 = generatingTests.generatRandom(x)
                t1 = time.perf_counter()
                randomQuickSort(l1,0,len(l1)-1)
                r1 = time.perf_counter()-t1
                f.write(f"RandomQuickSort,{r1}\n")
            i+=1
        f.close()

def runTest2():
    #filename = input
    resfilename = "resSize"
    x =int(input())
    resfilename+=f"{x}"
    with open(resfilename, "w+") as f:
        i =0
        while i<7:
            #les = l.copy()
            if(i ==0):
                l1 = generatingTests.generatRandom(x)
                r1 = bubbleSort(l1)
                f.write(f"BubbleSort with random numbers,{r1}\n")

                l2 = generatingTests.generateAscending(x)
                r2 = bubbleSort(l2)
                f.write(f"BubbleSort with ascending numbers,{r2}\n")

                l3 = generatingTests.generateDescending(x)
                r3 = bubbleSort(l3)
                f.write(f"BubbleSort with descending numbers,{r3}\n")

            if(i ==1):

                l1 = generatingTests.generatRandom(x)
                r1 = selectionSort(l1)
                f.write(f"SelectionSort with random numbers,{r1}\n")

                l2 = generatingTests.generateAscending(x)
                r2 = selectionSort(l2)
                f.write(f"SelectionSort with ascending numbers,{r2}\n")

                l3 = generatingTests.generateDescending(x)
                r3 = selectionSort(l3)
                f.write(f"SelectionSort with descending numbers,{r3}\n")

                #r = selectionSort(les)
                #f.write(f"SelectionSort,{r}\n")
            if(i ==2):
                l1 = generatingTests.generatRandom(x)
                r1 = insertionSort(l1)
                f.write(f"InsertionSort with random numbers,{r1}\n")

                l2 = generatingTests.generateAscending(x)
                r2 = insertionSort(l2)
                f.write(f"InsertionSort with ascending numbers,{r2}\n")

                l3 = generatingTests.generateDescending(x)
                r3 = insertionSort(l3)
                f.write(f"InsertionSort with descending numbers,{r3}\n")
            if(i ==3):
                l1 = generatingTests.generatRandom(x)
                r1 = improvedBubbleSort(l1)
                f.write(f"improvedBubbleSort with random numbers,{r1}\n")

                l2 = generatingTests.generateAscending(x)
                r2 = improvedBubbleSort(l2)
                f.write(f"improvedBubbleSort with ascending numbers,{r2}\n")

                l3 = generatingTests.generateDescending(x)
                r3 = improvedBubbleSort(l3)
                f.write(f"improvedBubbleSort with descending numbers,{r3}\n")

            if(i ==4):
                l1 = generatingTests.generatRandom(x)
                t1 = [0 for i in range(x)]
                time1= time.perf_counter()
                mergeSort(l1,t1,0,len(l1)-1)
                r1 = time.perf_counter()- time1
                f.write(f"MergeSort with random numbers,{r1}\n")

                l2 = generatingTests.generateAscending(x)
                t2 = [0 for i in range(x)]
                time2 = time.perf_counter()
                mergeSort(l2,t2,0,len(l2)-1)
                r2 = time.perf_counter()-time2
                f.write(f"MergeSort with ascending numbers,{r2}\n")

                l3 = generatingTests.generateDescending(x)
                t3 = [0 for i in range(x)]
                time3 = time.perf_counter()
                mergeSort(l3,t3,0,len(l3)-1)
                r3 = time.perf_counter() - time3
                f.write(f"MergeSort with descending numbers,{r3}\n")


                #t = [0 for i in range(len(les))]
                #t1 = time.perf_counter()
                #mergeSort(les,t,0,len(les)-1)
                #print(les)
                #r = time.perf_counter() - t1
                #f.write(f"MergeSort,{r}\n")
            if(i ==5):
                l1 = generatingTests.generatRandom(x)
                t1 = time.perf_counter()
                quickSort(l1,0,len(l1)-1)
                r1 = time.perf_counter()-t1
                f.write(f"QuickSort with random numbers,{r1}\n")

                l2 = generatingTests.generateAscending(x)
                t2 = time.perf_counter()
                quickSort(l2,0,len(l2)-1)
                r2 = time.perf_counter()-t2
                f.write(f"QuickSort with ascending numbers,{r2}\n")

                l3 = generatingTests.generateDescending(x)
                t3 = time.perf_counter()
                quickSort(l3,0,len(l3)-1)
                r3 = time.perf_counter()-t3
                f.write(f"QuickSort with descending numbers,{r3}\n")

                #print(les)
            if(i ==6):
                l1 = generatingTests.generatRandom(x)
                t1 = time.perf_counter()
                randomQuickSort(l1,0,len(l1)-1)
                r1 = time.perf_counter()-t1
                f.write(f"RandomQuickSort with random numbers,{r1}\n")

                l2 = generatingTests.generateAscending(x)
                t2 = time.perf_counter()
                randomQuickSort(l2,0,len(l2)-1)
                r2 = time.perf_counter()-t2
                f.write(f"randomQuickSort with ascending numbers,{r2}\n")

                l3 = generatingTests.generateDescending(x)
                t3 = time.perf_counter()
                randomQuickSort(l3,0,len(l3)-1)
                r3 = time.perf_counter()-t3
                f.write(f"randomQuickSort with descending numbers,{r3}\n")
            i+=1
        f.close()
            
runTest(100000,1000000,100000)


#print(insertionSort(arr1,stats[0],stats[1]))
#rintArray(arr1)
#print(bubbleSort(arr2,stats[0],stats[1]))
#rintArray(arr2)
#quickSort(arr3, 0,len(arr3)-1)
#rintArray(arr3)
#randomQuickSort(arr4,0,len(arr4)-1)
#rintArray(arr4)
#print(improvedBubbleSort(arr5,stats[0],stats[1]))
#rintArray(arr5)
#selectionSort(arr6)
#rintArray(arr6)
#mergeSort(arr7,l,0,len(arr7)-1)
#print(insertionSort(arr,stats[0],stats[1]),stats[0],bubbleSort(arr,stats[0],stats[1]))