### Whale Optimization Algorithm

##### Reference: Mirjalili S, Lewis A. The whale optimization algorithm[J]. Advances in Engineering Software, 2016, 95: 51-67.

| Variables  | Meaning                                                  |
| ---------- | -------------------------------------------------------- |
| pop        | The number of population                                 |
| lb         | List, the lower bound of the i-th component is lb[i]     |
| ub         | List, the upper bound of the i-th component is ub[i]     |
| iter       | The maximum number of iterations                         |
| dim        | The dimension, dim = len(lb) = len(ub)                   |
| pos        | List, the position of each wolf                          |
| score      | List, the score of each wolf                             |
| iter_best  | List, the best so-far score of each iteration            |
| prey_score | The score of the prey (the best-so-far score)            |
| prey_pos   | List, the position of the prey                           |
| con_iter   | The last iteration number when the prey_score is updated |

#### Test problem: Pressure vessel design

![](https://github.com/Xavier-MaYiMing/Whale-Optimization-Algorithm/blob/main/Pressure%20vessel%20design.png)
$$
\begin{align}
&\text{min}\ f(x)=0.6224x_1x_3x_4+1.7781x_2x_3^2+3.1661x_1^2x_4+19.84x_1^2x_3,\\
&\text{s.t.} \\
&-x_1+0.0193x_3\leq0,\\
&-x_3+0.0095x_3\leq0,\\
&-\pi x_3^2x_4-\frac{4}{3}\pi x_3^3+1296000\leq0,\\
&x_4-240\leq0,\\
&0\leq x_1\leq99,\\
&0\leq x_2 \leq99,\\
&10\leq x_3 \leq 200,\\
&10\leq x_4 \leq 200.
\end{align}
$$


#### Example

```python
if __name__ == '__main__':
    pop = 200
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    iter = 100
    print(main(pop, lb, ub, iter))
```

##### Output:
![](https://github.com/Xavier-MaYiMing/Whale-Optimization-Algorithm/blob/main/convergence%20curve.png)

```python
{
    'best solution': [1.3042606802575338, 0.6485023104593771, 67.38602116115652, 10.0], 
    'best score': 8111.232881473693, 
    'convergence iteration': 9907
}
```

