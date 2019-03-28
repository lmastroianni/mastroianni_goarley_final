#Chart 1
import numpy as np
import matplotlib.pyplot as plt


n_groups = 3


Fish = (38, 47, 49)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.55

opacity = 0.8

ax.bar(index + bar_width, Fish, bar_width, alpha=opacity, color='#53652b', label='fish')

ax.set_xlabel('Years')
ax.set_ylabel('Fish Cought')
ax.set_title('About Of Rainbow Trout Cought With Electrofishing In Komoka, Oxbow, And Dingman Creek')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('2016', '2017', '2018'))
ax.legend()

fig.tight_layout()
plt.show()

#CHART 2 - pie chart
import matplotlib.pyplot as plt

labels = 'Rainbow Trout', 'Brown Trout'
sizes = [61, 39]
explode = (0.1, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()

#CHART 3
import numpy as np
import matplotlib.pyplot as plt


n_groups = 17


memberships = (52, 48, 67, 45, 45, 45, 55, 67, 65, 70, 60, 60, 55, 60, 65, 75, 80)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.55

opacity = 0.8

ax.bar(index + bar_width, memberships, bar_width, alpha=opacity, color='#53652b', label='years')

ax.set_xlabel('Years')
ax.set_ylabel('Memberships')
ax.set_title('TRAA Memberships')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'))
ax.legend()

fig.tight_layout()
plt.show()
