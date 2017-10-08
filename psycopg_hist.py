from secret_open_connection import secret_connection
import numpy as np
import seaborn as sns

conn = secret_connection()
cur = conn.cursor()

cur.execute("select length(title) from movies;")
num_titles = cur.rowcount
title_lengths = cur.fetchall()

length_array = np.empty(num_titles)

i=0
for length in title_lengths:
    length_array[i] = length[0]
    i += 1

ax = sns.distplot(length_array, kde=False)
ax.set_title("Histogram of title lengths in movie dataset")
ax.set_xlabel("Length of title")
sns.plt.show()