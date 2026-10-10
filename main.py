
import numpy as np
import pandas as pd


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def analyze_students():
    # Read student data
    df = pd.read_csv("students.csv")

    subjects = ["Python", "Mathematics", "AI"]

    # Calculate total and average using Pandas
    df["Total"] = df[subjects].sum(axis=1)
    df["Average"] = df[subjects].mean(axis=1).round(2)

    # Assign grades using a reusable function
    df["Grade"] = df["Average"].apply(calculate_grade)

    # Pass only if each subject mark is at least 40
    df["Result"] = np.where(
        (df[subjects] >= 40).all(axis=1),
        "Pass",
        "Fail"
    )

    print("\nSTUDENT PERFORMANCE ANALYTICS")
    print("=" * 70)
    print(df.to_string(index=False))

    print("\nCLASS STATISTICS")
    print("-" * 30)
    print("Number of students:", len(df))
    print("Class average:", round(df["Average"].mean(), 2))
    print("Highest average:", df["Average"].max())
    print("Lowest average:", df["Average"].min())

    print("\nSUBJECT-WISE AVERAGES")
    print(df[subjects].mean().round(2))

    print("\nPASS/FAIL SUMMARY")
    print(df["Result"].value_counts())

    print("\nTOP-PERFORMING STUDENT(S)")
    highest = df["Average"].max()
    print(df.loc[df["Average"] == highest,
                 ["Name", "Average", "Grade"]].to_string(index=False))

    # Save analysis results
    df.to_csv("student_performance_report.csv", index=False)
    print("\nReport saved to student_performance_report.csv")


if __name__ == "__main__":
    analyze_students()
