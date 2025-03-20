import argparse
import json
from pathlib import Path

import pandas as pd


def main(pr_name: str, pr_number: int, pr_author: str, timestamp: str, pr_sha: str):
    with open("results.json", "r") as f:
        results = json.load(f)

    results["pr_name"] = pr_name
    results["pr_number"] = pr_number
    results["pr_author"] = pr_author
    results["timestamp"] = timestamp
    results["pr_sha"] = pr_sha

    if not Path("results.csv").exists():
        df = pd.DataFrame(results)
    else:
        df = pd.read_csv("results.csv")
        # Update the entry which has the same pr_author and pr_number
        if (df["pr_author"] == pr_author) & (df["pr_number"] == pr_number):
            df.loc[
                (df["pr_author"] == pr_author) & (df["pr_number"] == pr_number), :
            ] = results
        else:
            df = pd.concat([df, pd.DataFrame(results)], ignore_index=True)

    # Sort by image_score then by pixel_score in descending order
    df = df.sort_values(by=["image_score", "pixel_score"], ascending=False)
    df.to_csv("results.csv", index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr_name", type=str, required=True)
    parser.add_argument("--pr_number", type=int, required=True)
    parser.add_argument("--pr_author", type=str, required=True)
    parser.add_argument("--timestamp", type=str, required=True)
    parser.add_argument("--pr_sha", type=str, required=True)
    main()
