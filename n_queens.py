def n_queens(n):
    fer = []
    def safe(row,col):
        for r in range(row):
            c = fer[r]
            if c == col or abs(c - col)==abs(r - row):
                return False
        return True
            
    def place(row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if safe(row, col):
                fer.append(col)
                count += place(row + 1)
                fer.pop()
        return count
    return place(0)
