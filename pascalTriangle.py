class PascalTriangle:
    def generate(self, numRows):
        result = []
        
        for i in range(numRows):
            row = [1]  

            for j in range(1, i):
                row.append(result[i - 1][j - 1] + result[i - 1][j])
            
            if i > 0:
                row.append(1)
            
            result.append(row)
        
        return result


pascal = PascalTriangle()

numRows = int(input("Enter the number of rows for Pascal's Triangle: \n"))

triangle = pascal.generate(numRows)

for row in triangle:
    print(row)
