for i in range(256):
    for j in range(256):
        for k in range (256):
            if(trainedData[i][j][k]>0.0014):
                print((i,j,k),float(trainedData[i][j][k]))