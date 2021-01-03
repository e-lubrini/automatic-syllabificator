import matplotlib.pyplot as plt

num_stat = {
    '3': 2923,
    '2': 2190,
    '4': 1159,
    '1': 407,
    '5': 257,
    '6': 64,
    '7': 3,
    '8': 1
}

left = [x for x in range(8)]
height = list(num_stat.values())
tick_label = list(num_stat.keys())

plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=plt.cm.get_cmap('PuRd_r', len(tick_label))(range(len(tick_label))))
plt.gcf().set_size_inches(35, 5)
plt.xlabel('number of syllables per word')
plt.ylabel('frequency')
plt.title('Distribution of the number of syllables per word')
plt.tick_params(labelsize=10)

plt.show()
