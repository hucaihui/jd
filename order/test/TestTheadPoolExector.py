from concurrent.futures import ThreadPoolExecutor,as_completed

executor = ThreadPoolExecutor(max_workers=5)
def writeToFile(fileName, content):
    with open(fileName, 'w') as f:
        f.write(content)
    return True

def subThread():

    print("subThread")
    executor.submit(writeToFile,("a1.txt","aaa"))
    executor.submit(writeToFile,("a2.txt","bbb"))
    with open("a3.txt",'w' ) as f:
        f.write("cccc")
    print("over")

if __name__=='__main__':


    allTask = []
    # allTask.append(executor.submit(writeToFile,"test.txt","aaa"))
    #
    # allTask.append(executor.submit(writeToFile,"test2.txt","bbb"))
    #
    # for future in as_completed(allTask):
    #     ret = future.result()
    #     print(ret)
    #
    # executor.shutdown()
    executor.submit(subThread)