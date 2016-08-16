def load_triangle(input_file):
    with open(input_file) as f:
        tri = [list(map(int,line.strip().split(" "))) for line in f.readlines()]
        return tri

def subtriangle(triangle, x, y):
    triangle[y][x]
    subtri = []
    for i in range(y, len(triangle)):
        subtri += [triangle[i][x:x + i]]

    return subtri

def minimax(triangle):
    if len(triangle) == 80:
        print(triangle[0][0])
    if len(triangle) == 1:
        return triangle[0][0]
    else:
        return triangle[0][0] + max(minimax(subtriangle(triangle,0,1)),minimax(subtriangle(triangle,1,1)))

if __name__ == "__main__":
    triangle = load_triangle("p018_triangle.txt")
    print(minimax(triangle))
