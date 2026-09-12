#!/usr/bin/env python3


import argparse

import pandas as pd
import matplotlib.pyplot as plt
import ROOT


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("rootfile", help="Path to the .root file to analyze")
    p.add_argument("--tree", default="MakeDigiNtuple/digis",
                   help="Tree name, including subdirectory (default: %(default)s)")
    p.add_argument("--out", default="subrun_duration.png",
                   help="Output image filename (default: %(default)s)")
    p.add_argument("--csv", default=None,
                   help="Optional: also write the per-subrun duration table to this CSV path")
    return p.parse_args()


def main():
    args = parse_args()

    df = ROOT.RDataFrame(args.tree, args.rootfile)
    n = df.Count().GetValue()
    print(f"Loaded '{args.tree}' from {args.rootfile}: {n:,} entries")

 
    df = df.Define(
        "evt_time",
        "sh.time.empty() ? std::numeric_limits<float>::quiet_NaN() : Min(sh.time)"
    )

    data = df.AsNumpy(["srn", "evt_time"])
    pdf = pd.DataFrame(data)
    pdf = pdf.dropna(subset=["evt_time"])

 
    per_srn = pdf.groupby("srn")["evt_time"].agg(["min", "max", "count"])
    per_srn["duration"] = per_srn["max"] - per_srn["min"]
    per_srn = per_srn.reset_index()

    print(f"Subruns found: {len(per_srn)}")
    print(f"Duration range: {per_srn['duration'].min():.1f} to "
          f"{per_srn['duration'].max():.1f} (units match sh.time, likely ns)")
    print(per_srn.head(10).to_string(index=False))

    if args.csv:
        per_srn.to_csv(args.csv, index=False)
        print(f"Wrote per-subrun table to {args.csv}")
    ns_to_min = (10E-6)*60
    plt.figure(figsize=(10, 6))
    plt.scatter(per_srn["srn"], per_srn["duration"]*ns_to_min, marker=".", linestyle="-", linewidth=0.8)
    plt.xlabel("Subrun number")
    plt.ylabel("Subrun duration [min]")
    plt.grid()
    plt.title("Duration of each subrun")
    plt.tight_layout()
    plt.savefig(args.out, dpi=150)
    print(f"Saved plot to {args.out}")


if __name__ == "__main__":
    main()