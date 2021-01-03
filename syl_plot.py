import matplotlib.pyplot as plt

syl_stat = {
    'PlC OralV ': 3523,
    'FrC OralV ': 2136,
    'LiC OralV ': 1858,
    'NasC OralV ': 1393,
    'PlC LiC OralV ': 1216,
    'OralV ': 1186,
    'PlC OralV LiC ': 784,
    'PlC NasalV ': 568,
    'NasalV ': 504,
    'FrC OralV LiC ': 459,
    'NasC NasalV ': 330,
    'FrC NasalV ': 322,
    'PlC OralV FrC ': 305,
    'FrC SemiV OralV ': 252,
    'FrC SemiV NasalV ': 231
}


left = [x for x in range(15)]
height = list(syl_stat.values())
tick_label = list(syl_stat.keys())

plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=plt.cm.get_cmap('Greens_r', len(tick_label))(range(len(tick_label))))
plt.gcf().set_size_inches(35, 5)
plt.xlabel('structures')
plt.ylabel('frequency')
plt.title('Distribution')
plt.tick_params(labelsize=5.5)

plt.show()
