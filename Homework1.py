# 13 x 16 GridWorld
BD = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
[1, 0 ,0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1]
[1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1]
[1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
[1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
[1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
];

E = [[0,0,0,0,1,1,0,0], [0,0,0,0,0,1,1,0], [0,0,0,0,1,1,1,0], [0,0,0,0,1,1,0,1],
     [0,0,0,0,0,1,1,1], [1,0,0,0,0,1,1,0], [1,0,0,0,1,1,0,0], [0,0,0,0,1,1,1,1],
     [1,0,0,0,1,1,1,0], [0,1,0,0,1,1,1,0], [0,1,0,0,1,1,1,1]
     ]
S = [[0,0,0,0,0,0,1,1], [1,0,0,0,0,0,0,1], [1,0,0,0,0,0,1,1], [1,1,0,0,0,0,0,1],
     [0,1,0,0,0,0,1,1], [0,0,1,0,0,0,1,1], [1,0,1,0,0,0,0,1], [1,1,0,0,0,0,1,1],
     [1,0,1,0,0,0,1,1], [1,0,0,1,0,0,1,1], [1,1,0,1,0,0,1,1]
     ]

W = [[1,1,0,0,0,0,0,0], [0,1,1,0,0,0,0,0], [1,1,1,0,0,0,0,0], [1,1,0,1,0,0,0,0],
     [1,1,0,0,1,0,0,0], [0,1,1,0,1,0,0,0], [0,1,1,1,0,0,0,0], [1,1,1,1,0,0,0,0],
     [1,1,1,0,1,0,0,0], [1,1,1,0,0,1,0,0], [1,1,1,1,0,1,0,0]
     ]

N = [[0,0,1,1,0,0,0,0], [0,0,0,1,1,0,0,0], [0,0,1,1,1,0,0,0], [0,0,1,1,0,1,0,0],
     [0,0,1,1,0,0,1,0], [0,0,0,1,1,1,0,0], [0,0,0,1,1,0,1,0], [0,0,1,1,1,1,0,0],
     [0,0,1,1,1,1,0,0], [0,0,1,1,1,0,1,0], [0,0,1,1,1,1,0,1]
    ]


X = list()
X.extend(E)
X.extend(S)
X.extend(W)
X.extend(N)

