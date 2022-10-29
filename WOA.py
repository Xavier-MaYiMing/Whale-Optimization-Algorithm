#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/28 19:21
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : WOA.py
# @Statement : The whale optimization algorithm
# @Reference : Mirjalili S, Lewis A. The whale optimization algorithm[J]. Advances in Engineering Software, 2016, 95: 51-67.
import random
import math
import matplotlib.pyplot as plt


def obj(x):
    """
    The objective function of reservoir
    :param x:
    :return:
    """
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    g1 = -x1 + 0.0193 * x3
    g2 = -x2 + 0.00954 * x3
    g3 = -math.pi * x3 ** 2 - 4 * math.pi * x3 ** 3 / 3 + 1296000
    g4 = x4 - 240
    if g1 <= 0 and g2 <= 0 and g3 <= 0 and g4 <= 0:
        return 0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3
    else:
        return 1e10


def boundary_check(x, lb, ub, dim):
    """
    Check the boundary
    :param x: a candidate solution
    :param lb: lower bound
    :param ub: upper bound
    :param dim: dimension
    :return:
    """
    for i in range(dim):
        if x[i] < lb[i]:
            x[i] = lb[i]
        elif x[i] > ub[i]:
            x[i] = ub[i]
    return x


def main(pop, lb, ub, iter):
    """
    The main function of WOA
    :param pop: the number of wolves
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :param iter: the iteration number
    :return:
    """
    # Step 1. Initialization
    dim = len(ub)  # dimension
    pos = []
    score = []
    iter_best = []  # the best ever value of each iteration
    for _ in range(pop):
        temp_pos = [random.uniform(lb[i], ub[i]) for i in range(dim)]
        temp_score = obj(temp_pos)
        pos.append(temp_pos)
        score.append(temp_score)
    prey_score = min(score)
    prey_pos = pos[score.index(prey_score)].copy()
    con_iter = 0

    # Step 2. The main loop
    for t in range(iter):
        a = 2 - 2 * (t + 1) / iter
        for i in range(pop):
            A = 2 * a * random.random() - a
            C = 2 * random.random()
            if random.random() < 0.5:
                for j in range(dim):
                    if abs(A) < 1:  # Encircling pray
                        D = abs(C * prey_pos[j] - pos[i][j])
                        pos[i][j] = prey_pos[j] - A * D
                    else:  # Search for prey
                        rand_pos = random.choice(pos)
                        D = abs(C * rand_pos[j] - pos[i][j])
                        pos[i][j] = rand_pos[j] - A * D
            else:  # Bubble-net attacking method
                l = random.uniform(-1, 1)
                for j in range(dim):
                    D = abs(prey_pos[j] - pos[i][j])
                    pos[i][j] = D * math.exp(l) * math.cos(2 * math.pi * l) + prey_pos[j]

            # Update the prey information
            pos[i] = boundary_check(pos[i], lb, ub, dim)
            score[i] = obj(pos[i])
            if score[i] < prey_score:
                prey_score = score[i]
                prey_pos = pos[i].copy()
                con_iter = t
        iter_best.append(prey_score)

    # Step 3. Sort the results
    x = [i for i in range(iter)]
    plt.figure()
    plt.plot(x, iter_best, linewidth=2, color='blue')
    plt.xlabel('Iteration number')
    plt.ylabel('Global optimal value')
    plt.title('Convergence curve')
    plt.ticklabel_format(style='sci', scilimits=(0, 0))
    plt.show()
    return {'best solution': prey_pos, 'best score': prey_score, 'convergence iteration': con_iter}


if __name__ == '__main__':
    pop = 20
    lb = [0, 0, 10, 10]
    ub = [100, 100, 100, 100]
    iter = 2000
    print(main(pop, lb, ub, iter))
