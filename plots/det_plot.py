import matplotlib.pyplot as plt

det_stat = {
    'a': 475,
    'de': 454,
    'e': 347,
    'te': 313,
    'ti': 273,
    '@': 272,
    'Ra': 265,
    'Re': 265,
    'm@': 243,
    'li': 235,
    'k1': 223,
    '5': 221,
    'R*': 220,
    'se': 190,
    'ka': 188
}

left = [x for x in range(15)]
height = list(det_stat.values())
tick_label = list(det_stat.keys())

plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=plt.cm.get_cmap('Blues_r', len(tick_label))(range(len(tick_label))))
plt.gcf().set_size_inches(35, 5)
plt.xlabel('structures')
plt.ylabel('frequency')
plt.title('Distribution')
plt.tick_params(labelsize=5.5)

plt.show()
