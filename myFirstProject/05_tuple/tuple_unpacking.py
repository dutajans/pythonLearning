from scipy import stats
from statistics import mean

male_group = [55, 65, 87, 100, 77]
female_group = [44, 100, 88, 55, 45]

male_ave = mean(male_group)
female_ave = mean(female_group)

print(f"Male Average: {male_ave}\nFermale Average: {female_ave}")

ttest_result = stats.ttest_ind(male_group, female_group)
print(type(ttest_result))

len(ttest_result)
ttest_result[1]

.....