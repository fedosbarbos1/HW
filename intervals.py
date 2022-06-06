from scipy.stats import t, norm, binom, beta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem, t

dataset_iris=pd.read_csv("data/iris.csv", sep=',')

petal_length=dataset_iris[["petal_length", "species"]]
setosa_subset = petal_length[petal_length["species"]=="setosa"]
versicolor_subset = petal_length[petal_length["species"]=="versicolor"]
virginica_subset = petal_length[petal_length["species"]=="virginica"]


setosa_petal_length = t(scale=sem(setosa_subset.petal_length), loc=setosa_subset.petal_length.mean(), df=len(setosa_subset))
versicolor_petal_length = t(scale=sem(versicolor_subset.petal_length), loc=versicolor_subset.petal_length.mean(), df=len(versicolor_subset))
virginica_petal_length = t(scale=sem(virginica_subset.petal_length), loc=virginica_subset.petal_length.mean(), df=len(virginica_subset))


ci_lower_setosa, ci_upper_setosa = setosa_petal_length.interval(alpha=0.95)
ci_lower_versicolor, ci_upper_versicolor = versicolor_petal_length.interval(alpha=0.95)
ci_lower_virginica, ci_upper_virginica = virginica_petal_length.interval(alpha=0.95)

fig, ax = plt.subplots()

means = setosa_subset.petal_length.mean(), versicolor_subset.petal_length.mean(), virginica_subset.petal_length.mean()
ci = np.array([[ci_upper_setosa, ci_upper_versicolor, ci_upper_virginica], [ci_lower_setosa, ci_lower_versicolor, ci_lower_virginica]])

y_r = [means[i] - ci[i][1] for i in range(len(ci))]

means = setosa_subset.petal_length.mean(), versicolor_subset.petal_length.mean(), virginica_subset.petal_length.mean()
ci = [ci_lower_setosa, ci_lower_versicolor, ci_lower_virginica]
y_r = [means[i] - ci[i] for i in range(len(ci))]

plt.bar(range(len(means)), means, yerr=y_r, alpha=0.2, align="center", color="magenta", ecolor="blue", capsize=10)
plt.tick_params(bottom=False, labelbottom=False)

ax.set_title("Bar plot with 95% confidence intervals", fontweight="bold")
ax.set_ylabel("Medium petal length")

plt.text(0.12, -0.1, "Setosa", color="black", transform=ax.transAxes)
plt.text(0.43, -0.1, "Versicolor", color="black", transform=ax.transAxes)
plt.text(0.76, -0.1, "Virginica", color="black", transform=ax.transAxes)

plt.show