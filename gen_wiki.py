import sys

color = {
    'NOV': '#63a',
    'ADV': '#ec0',
    'EXH': '#f33',
    'MXM': '#9ac',
    'INF': '#e2a',
    'GRV': '#f60',
    'HVN': '#08f',
    'VVD': '#f19'
}

level_color = {
    'NOV': '#ddf',
    'ADV': '#ffc',
    'EXH': '#fdd',
    'MXM': '#eef',
    'INF': '#fce',
    'GRV': '#fdc',
    'HVN': '#cef',
    'VVD': '#fdf'
}

def genLine(n, title, rank, level):
    return '|{n}|{title}|BGCOLOR({color}):''{rank}''|BGCOLOR({lcolor}):{level}|'.format(
        n=n, 
        title=title,
        color=color[rank], 
        rank=rank,
        lcolor=level_color[rank],
        level=level
    )

if (len(sys.argv) != 2):
    print('usage: python3 code_gen.py songs.txt')
    exit(1)

filename = sys.argv[1]
# try:
f = open(filename, encoding='utf-8')
line = f.readline()
while line:
    info = line.split('|')
    if len(info) != 4:
        print()
    else:
        print(genLine(info[0], info[1], info[2], info[3].strip()))
    line = f.readline()
# except:
#     print('failed')
#     exit(2)
