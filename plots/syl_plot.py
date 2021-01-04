import matplotlib.pyplot as plt

syl_stat = {
    'PlC OralV ': 3521,
    'FrC OralV ': 2133,
    'LiC OralV ': 1857,
    'NasC OralV ': 1389,
    'PlC LiC OralV ': 1236,
    'OralV ': 1157,
    'PlC OralV LiC ': 784,
    'PlC NasalV ': 568,
    'NasalV ': 503,
    'FrC OralV LiC ': 460,
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
plt.xlabel('macro-class structures')
plt.ylabel('frequency')
plt.title('Distribution of macro-class structures')
plt.tick_params(labelsize=5.5)

plt.show()
