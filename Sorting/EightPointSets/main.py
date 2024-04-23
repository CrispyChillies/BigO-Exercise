def main():
    Points = []
    X = []
    Y = []

    for i in range(1,9):
        x,y = map(int, input().split())
        Points.append((x,y))
        if x not in X:
            X.append(x)
        if y not in Y:
            Y.append(y)
    if len(X) != 3 or len(Y) != 3:
        print("ugly")
        return 
    
    Points.sort()
    X.sort()
    Y.sort()

    index = 0
    for i in range(2):
        for j in range(2):
            if i == 1 and j == 1:
                continue
            if Points[index] == (X[i], Y[i]):
                index += 1
                continue
            else:
                print("ugly")
                return
                
        
    print("respectable")

if __name__ == "__main__":
    main()