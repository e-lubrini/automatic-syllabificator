import matplotlib.pyplot as plt

cv_stat = {
    'CV': 10631,
    'CVC': 3457,
    'CCV': 2601,
    'V': 1690,
    'CCVC': 596,
    'VC': 395,
    'CVCC': 365,
    'CCCV': 35,
    'CCVCC': 33,
    'CCCCV': 26,
    'VCC': 18,
    'CCCVC': 13,
    'CCCCVC': 11,
    'CVCCC': 8,
    'CCCVCC': 4
}


left = [x for x in range(15)]
height = list(cv_stat.values())
tick_label = list(cv_stat.keys())

plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=plt.cm.get_cmap('Purples_r', len(tick_label))(range(len(tick_label))))
plt.gcf().set_size_inches(35, 5)
plt.xlabel('structures')
plt.ylabel('frequency')
plt.title('Distribution')
plt.tick_params(labelsize=5.5)

plt.show()
