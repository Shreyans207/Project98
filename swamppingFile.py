def SwapFileData() : 
    swapFileName = input('Enter The File Name - ')
    swapFileName2 = input('Enter The Second File Name Which You Want To Swap With - ')

    openedFile = open('sample1.txt')
    data_a = openedFile.read()

    openedFile2 = open('sample2.txt')
    data_b = openedFile2.read()

    openedFile3 = open(swapFileName , 'w')
    openedFile3.write(data_b)

    openedFile4 = open(swapFileName2 , 'w')
    openedFile4.write(data_a)
    print('Challange Completed!!')

SwapFileData()
