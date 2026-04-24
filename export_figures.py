"""Regenerate the three EX09 visualizations as PNGs for the personal site.

Run from the comp110 ex09 directory so that `data_utils` and `data/` resolve:

    cd /Users/seanchang/comp110-26s-workspace/exercises/ex09
    python "/Users/seanchang/VSCode Projects/personal-site/export_figures.py"
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns

from data_utils import (
    read_csv_rows,
    columnar,
    concat,
    select,
    convert_columns_to_int,
    group_by,
    mean,
)

OUTPUT_DIR = "/Users/seanchang/VSCode Projects/personal-site/static/imgs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_theme()

izzi_rows = columnar(read_csv_rows("data/survey_izzi.csv"))
alyssa_rows = columnar(read_csv_rows("data/survey_alyssa.csv"))

data = concat(izzi_rows, alyssa_rows)
data = select(
    data,
    [
        "comp_major",
        "prior_exp",
        "prior_time",
        "languages",
        "pace",
        "difficulty",
        "understanding",
        "interesting",
        "valuable",
        "would_recommend",
    ],
)

metrics = [
    "pace",
    "difficulty",
    "understanding",
    "interesting",
    "valuable",
    "would_recommend",
]

data = convert_columns_to_int(data, metrics)


def averages_by(grouped: dict, metrics: list[str]) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for key in grouped:
        out[key] = {}
        for m in metrics:
            out[key][m] = mean(grouped[key][m])
    return out


def long_form(averages: dict[str, dict[str, float]], key_name: str, metrics: list[str]):
    plot_data: dict[str, list[str | float]] = {key_name: [], "metric": [], "value": []}
    for group in averages:
        for m in metrics:
            plot_data[key_name].append(group)
            plot_data["metric"].append(m)
            plot_data["value"].append(averages[group][m])
    return plot_data


# Visualization 1: average metrics by language
grouped_by_language = group_by(data, "languages")
avg_by_language = averages_by(grouped_by_language, metrics)
plot_data = long_form(avg_by_language, "language", metrics)

g1 = sns.catplot(
    data=plot_data,
    kind="bar",
    x="language",
    y="value",
    hue="metric",
    height=6,
    aspect=2,
)
g1.set_xticklabels(rotation=45, ha="right")
g1.figure.suptitle("Average course ratings by language known", y=1.02)
g1.savefig(os.path.join(OUTPUT_DIR, "viz_by_language.png"), dpi=150, bbox_inches="tight")
plt.close(g1.figure)

# Visualization 2: share of responses by language (pie)
language_labels: list[str] = []
language_sizes: list[int] = []
for language in grouped_by_language:
    language_labels.append(language)
    language_sizes.append(len(grouped_by_language[language]["pace"]))

plt.figure(figsize=(8, 8))
plt.pie(
    language_sizes,
    labels=language_labels,
    autopct="%1.1f%%",
    colors=sns.color_palette("tab20", n_colors=len(language_labels)),
)
plt.title("Share of responses by language")
plt.savefig(os.path.join(OUTPUT_DIR, "viz_language_shares.png"), dpi=150, bbox_inches="tight")
plt.close()

# Visualization 3: average metrics by prior experience
grouped_by_exp = group_by(data, "prior_exp")
avg_by_exp = averages_by(grouped_by_exp, metrics)
plot_data = long_form(avg_by_exp, "prior_exp", metrics)

g3 = sns.catplot(
    data=plot_data,
    kind="bar",
    x="prior_exp",
    y="value",
    hue="metric",
    height=6,
    aspect=2,
)
g3.set_xticklabels(rotation=20, ha="right")
g3.figure.suptitle("Average course ratings by prior experience", y=1.02)
g3.savefig(os.path.join(OUTPUT_DIR, "viz_by_prior_exp.png"), dpi=150, bbox_inches="tight")
plt.close(g3.figure)

print(f"Wrote 3 figures to {OUTPUT_DIR}")
