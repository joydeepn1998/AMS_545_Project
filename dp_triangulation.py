import numpy as np
import matplotlib.pyplot as plt
import ear_clipping

#The weight function computes the length of only the first diagonal in the triangulation
# to avoid duplication

def weight(a, b, c):
    return np.linalg.norm(np.array(b) - np.array(a))

def display_minimum_weight_triangulation(polygon):
    n = len(polygon)
    dp = [[0] * n for _ in range(n)]
    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + weight(polygon[i], polygon[j], polygon[k])
                dp[i][j] = min(dp[i][j], cost)
    triangulation = []
    construct_triangulation(dp, triangulation, 0, n - 1, polygon)

    total_weight_dp = 0
    cnt = 0
    for triangle in triangulation:
        plt.plot([polygon[triangle[0]][0], polygon[triangle[1]][0]], [polygon[triangle[0]][1], polygon[triangle[1]][1]], 'b-')
        plt.plot([polygon[triangle[1]][0], polygon[triangle[2]][0]], [polygon[triangle[1]][1], polygon[triangle[2]][1]], 'b-')
        plt.plot([polygon[triangle[2]][0], polygon[triangle[0]][0]], [polygon[triangle[2]][1], polygon[triangle[0]][1]], 'b-')
        total_weight_dp += weight(polygon[triangle[0]], polygon[triangle[1]], polygon[triangle[2]])
        cnt += 1

    print("DP : " , cnt)
    plt.plot([p[0] for p in polygon], [p[1] for p in polygon], 'ro')

    # Ear clipping algorithm
    total_weight_ear_clipping = ear_clipping.ear_clipping_triangulation(polygon)
    
    plt.title(f'Minimize diagonal length triangulation (Weight={total_weight_dp:.2f})')
    plt.show()

def construct_triangulation(dp, triangulation, i, j, polygon):
    if j == i + 1:
        return
    k = dp[i][j]
    for l in range(i + 1, j):
        if dp[i][l] + dp[l][j] + weight(polygon[i], polygon[j], polygon[l]) == k:
            triangulation.append((i, l, j))
            construct_triangulation(dp, triangulation, i, l, polygon)
            construct_triangulation(dp, triangulation, l, j, polygon)
            return

def dp_triangulation(polygon):
    display_minimum_weight_triangulation(polygon)