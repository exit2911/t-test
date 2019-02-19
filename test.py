
from scipy import stats

# level of significance = .1 (alpha)
# claim: there is a difference between before and after sample data
# H0: difference between hypothesized sample means is zero
# H1: difference between hypothesized sample means is not zero

before = [210,235,208,190,172,244]
after = [190,170,210,188,173,228]


print(stats.ttest_rel(before,after))

# result is 1.61
# with alpha = .1, critical values are plus,minus 2.015
# fail to reject null hypothesis since the result is in noncritical region
