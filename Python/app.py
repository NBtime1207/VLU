from matplotlib import pyplot as plt
from matplotlib_venn import venn2

venn2( subset=(0.5, 0.5, 0), set_labels=('Head', 'Tail'))
plt.show()