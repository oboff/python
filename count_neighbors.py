def checkio(data):
    for i in range(3):
        for j in range(5):
            print "cell:", data[i][j]
            if i < 1:
                if j < 1:
                    #print data[i-1][j-1]
                    #print data[i-1][j]
                    #print data[i-1][j+1]
                    #print data[i][j-1]
                    print data[i][j+1]
                    #print data[i+1][j-1]
                    print data[i+1][j]
                    print data[i+1][j+1]
                if j >= 1 and j < 4:
                    #print data[i-1][j-1]
                    #print data[i-1][j]
                    #print data[i-1][j+1]
                    print data[i][j-1]
                    #print data[i][j+1]
                    print data[i+1][j-1]
                    print data[i+1][j]
                    print data[i+1][j+1]
                if j == 4:
                    #print data[i-1][j-1]
                    #print data[i-1][j]
                    #print data[i-1][j+1]
                    print data[i][j-1]
                    #print data[i][j+1]
                    print data[i+1][j-1]
                    print data[i+1][j]
                    #print data[i+1][j+1]
            if i >= 1 and i < 2:
                if j < 1:
                    #print data[i-1][j-1]
                    print data[i-1][j]
                    print data[i-1][j+1]
                    #print data[i][j-1]
                    print data[i][j+1]
                    #print data[i+1][j-1]
                    print data[i+1][j]
                    print data[i+1][j+1]
                if j >= 1 and j < 4:
                    print data[i-1][j-1]
                    print data[i-1][j]
                    print data[i-1][j+1]
                    print data[i][j-1]
                    print data[i][j+1]
                    print data[i+1][j-1]
                    print data[i+1][j]
                    print data[i+1][j+1]
                if j == 4:
                    #print data[i-1][j-1]
                    #print data[i-1][j]
                    #print data[i-1][j+1]
                    print data[i][j-1]
                    #print data[i][j+1]
                    print data[i+1][j-1]
                    print data[i+1][j]
                    #print data[i+1][j+1]
            if i == 2:
                if j < 1:
                    #print data[i-1][j-1]
                    print data[i-1][j]
                    print data[i-1][j+1]
                    #print data[i][j-1]
                    print data[i][j+1]
                    #print data[i+1][j-1]
                    #print data[i+1][j]
                    #print data[i+1][j+1]
                if j >= 1 and j < 4:
                    print data[i-1][j-1]
                    print data[i-1][j]
                    print data[i-1][j+1]
                    print data[i][j-1]
                    print data[i][j+1]
                    #print data[i+1][j-1]
                    #print data[i+1][j]
                    #print data[i+1][j+1]
                if j == 4:
                    print data[i-1][j-1]
                    print data[i-1][j]
                    #print data[i-1][j+1]
                    print data[i][j-1]
                    #print data[i][j+1]
                    #print data[i+1][j-1]
                    #print data[i+1][j]
                    #print data[i+1][j+1]
