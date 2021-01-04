import matplotlib.pyplot as plt

cv_stat = {
    'CV': 10621,
    'CVC': 3460,
    'CCV': 2623,
    'V': 1660,
    'CCVC': 598,
    'VC': 405,
    'CVCC': 372,
    'CCCV': 40,
    'VCC': 38,
    'CCVCC': 34,
    'CCCVC': 21,
    'CVCCC': 8,
    'CCCVCC': 6,
    'VCCC': 1,
    'CCCCVC': 1,
}


left = [x for x in range(15)]
height = list(cv_stat.values())
tick_label = list(cv_stat.keys())

plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=plt.cm.get_cmap('Blues_r', len(tick_label))(range(len(tick_label))))
plt.gcf().set_size_inches(35, 5)
plt.xlabel('CV structures')
plt.ylabel('frequency')
plt.title('Distribution of CV structures')

plt.show()
