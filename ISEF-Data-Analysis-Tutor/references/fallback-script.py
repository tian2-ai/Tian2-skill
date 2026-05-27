#!/usr/bin/env python3
"""Fallback statistical analysis using scipy/numpy when /statistical-analysis is unavailable.

This is a thin scipy wrapper covering the most common ISEF designs. Not a replacement for
domain-appropriate analysis — when you can, prefer /statistical-analysis which handles
edge cases, assumption checks, and multiple-comparison corrections.

Usage:
    python fallback-script.py --csv data.csv --design two-group --group-col treatment --value-col outcome
"""
import argparse
import csv
import math
import sys


def two_group_paired(a, b):
    """Paired t-test + Cohen's d."""
    from scipy import stats
    diffs = [x - y for x, y in zip(a, b)]
    t, p = stats.ttest_rel(a, b)
    sd_diff = (sum((d - sum(diffs) / len(diffs)) ** 2 for d in diffs) / (len(diffs) - 1)) ** 0.5
    d = (sum(diffs) / len(diffs)) / sd_diff if sd_diff > 0 else 0
    return {
        "test": "paired t-test",
        "n": len(a),
        "t": round(t, 3),
        "p": round(p, 5),
        "cohens_d": round(d, 3),
        "interp_d": _interp_d(d),
    }


def two_group_independent(a, b):
    """Independent t-test (Welch's by default — handles unequal variance) + Cohen's d."""
    from scipy import stats
    t, p = stats.ttest_ind(a, b, equal_var=False)
    pooled_sd = (
        ((len(a) - 1) * _var(a) + (len(b) - 1) * _var(b)) / (len(a) + len(b) - 2)
    ) ** 0.5
    d = (sum(a) / len(a) - sum(b) / len(b)) / pooled_sd if pooled_sd > 0 else 0
    return {
        "test": "Welch's t-test (independent)",
        "n_group1": len(a), "n_group2": len(b),
        "t": round(t, 3),
        "p": round(p, 5),
        "cohens_d": round(d, 3),
        "interp_d": _interp_d(d),
    }


def multi_group_anova(groups):
    """One-way ANOVA + Tukey post-hoc."""
    from scipy import stats
    f, p = stats.f_oneway(*groups)
    # eta-squared (simplified)
    grand_mean = sum(sum(g) for g in groups) / sum(len(g) for g in groups)
    ss_between = sum(len(g) * (sum(g) / len(g) - grand_mean) ** 2 for g in groups)
    ss_total = sum((x - grand_mean) ** 2 for g in groups for x in g)
    eta_squared = ss_between / ss_total if ss_total > 0 else 0
    return {
        "test": "one-way ANOVA",
        "n_groups": len(groups),
        "n_per_group": [len(g) for g in groups],
        "F": round(f, 3),
        "p": round(p, 5),
        "eta_squared": round(eta_squared, 3),
        "interp_eta": _interp_eta(eta_squared),
        "note": "If p<0.05, run Tukey HSD via statsmodels for post-hoc.",
    }


def correlation(x, y, method="pearson"):
    """Pearson or Spearman correlation."""
    from scipy import stats
    if method == "spearman":
        r, p = stats.spearmanr(x, y)
    else:
        r, p = stats.pearsonr(x, y)
    return {
        "test": f"{method} correlation",
        "n": len(x),
        "r": round(r, 3),
        "p": round(p, 5),
        "r_squared": round(r * r, 3),
    }


def _var(xs):
    m = sum(xs) / len(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - 1) if len(xs) > 1 else 0


def _interp_d(d):
    a = abs(d)
    if a < 0.2: return "negligible"
    if a < 0.5: return "small"
    if a < 0.8: return "medium"
    return "large"


def _interp_eta(eta):
    if eta < 0.01: return "negligible"
    if eta < 0.06: return "small"
    if eta < 0.14: return "medium"
    return "large"


def load_csv(path, group_col, value_col):
    groups = {}
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                v = float(row[value_col])
            except (ValueError, KeyError):
                continue
            g = row.get(group_col, "all")
            groups.setdefault(g, []).append(v)
    return groups


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--csv", required=True)
    p.add_argument("--design", required=True,
                   choices=["two-group-paired", "two-group-independent", "multi-group-anova", "correlation"])
    p.add_argument("--group-col")
    p.add_argument("--value-col")
    p.add_argument("--x-col")
    p.add_argument("--y-col")
    p.add_argument("--method", default="pearson")
    args = p.parse_args()

    import json
    if args.design == "correlation":
        with open(args.csv) as f:
            reader = csv.DictReader(f)
            rows = [r for r in reader if r.get(args.x_col) and r.get(args.y_col)]
        xs = [float(r[args.x_col]) for r in rows]
        ys = [float(r[args.y_col]) for r in rows]
        print(json.dumps(correlation(xs, ys, args.method), indent=2))
        return

    groups = load_csv(args.csv, args.group_col, args.value_col)
    if args.design == "two-group-paired":
        gs = list(groups.values())
        print(json.dumps(two_group_paired(gs[0], gs[1]), indent=2))
    elif args.design == "two-group-independent":
        gs = list(groups.values())
        print(json.dumps(two_group_independent(gs[0], gs[1]), indent=2))
    elif args.design == "multi-group-anova":
        print(json.dumps(multi_group_anova(list(groups.values())), indent=2))


if __name__ == "__main__":
    sys.exit(main() or 0)
