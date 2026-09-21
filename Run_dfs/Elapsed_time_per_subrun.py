#!/usr/bin/env python3
"""
subrun_duration.py

Estimates each subrun's duration from the span of event numbers (evn) it
covers, assuming a fixed per-event readout time -- an alternative to the
straw-hit-time-based version, for files/branches where sh.time isn't
what you want to key off of.
"""

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

    # evn is a per-event scalar (global monotonically increasing event
    # counter) -- no Min()/.empty() needed, unlike array-valued branches.
    df = df.Define("evt_time", "evn")

    data = df.AsNumpy(["srn", "evt_time"])
    pdf = pd.DataFrame(data)
    pdf = pdf.dropna(subset=["evt_time"])

    per_srn = pdf.groupby("srn")["evt_time"].agg(["min", "max", "count"])
    per_srn["duration"] = per_srn["max"] - per_srn["min"]   # event-number span
    per_srn = per_srn.reset_index()

    print(f"Subruns found: {len(per_srn)}")
    print(f"Duration range: {per_srn['duration'].min():.1f} to "
          f"{per_srn['duration'].max():.1f} events")
    print(per_srn.head(10).to_string(index=False))

    if args.csv:
        per_srn.to_csv(args.csv, index=False)
        print(f"Wrote per-subrun table to {args.csv}")

    sec_per_event = 100e-6   # 100 us/event -- confirm this is your actual DAQ readout period
    plt.figure(figsize=(10, 6))
    plt.scatter(per_srn["srn"], per_srn["duration"] * sec_per_event, marker=".")
    plt.xlabel("Subrun number")
    plt.xlim(0,451)
    plt.ylim(49.98,50)
    plt.ylabel("Subrun duration [sec]")
    plt.grid()
    plt.title("Duration of each subrun")
    plt.tight_layout()
    plt.savefig(args.out, dpi=150)
    print(f"Saved plot to {args.out}")


if __name__ == "__main__":
    main()