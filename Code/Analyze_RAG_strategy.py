#!usr/bin/env python

import csv
import os


def calculate_accuracy_per_subject(csv_reader, config):
    subject_accuracies = {}
    for row in csv_reader:
        subject = row[0].split("/")[0]
        predicted_answer = row[3]
        gold_answer = row[2]

        if subject not in subject_accuracies:
            subject_accuracies[subject] = {"correct": 0, "total": 0}

        subject_accuracies[subject]["total"] += 1
        if predicted_answer == gold_answer:
            subject_accuracies[subject]["correct"] += 1

    # return as csv file
    with open(f"{config}_subject_accuracy.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Subject", "Accuracy", "Total Examples", "Correct Examples"])

        # calculate overall accuracy
        overall_correct = sum(counts["correct"] for counts in subject_accuracies.values())
        overall_total = sum(counts["total"] for counts in subject_accuracies.values())
        overall_accuracy = overall_correct / overall_total if overall_total > 0 else 0
        print(f"Overall Accuracy: {overall_accuracy:.2f}")
        csv_writer.writerow(["Overall", overall_accuracy, overall_total, overall_correct])

        for subject, counts in subject_accuracies.items():
            accuracy = counts["correct"] / counts["total"]
            csv_writer.writerow([subject, accuracy, counts["total"], counts["correct"]])
            print(f"Subject: {subject}, Accuracy: {accuracy:.2f}, total examples: {counts['total']}, correct examples: {counts['correct']}")

def open_csv_file(folder_path):
    for file in os.listdir(folder_path):
        with open(os.path.join(folder_path, file), 'r', encoding="utf-8") as csvfile:
            config = file.split(".")[0]
            csv_reader = csv.reader(csvfile)

            calculate_accuracy_per_subject(csv_reader, config)
        print("_" * 50)

def main():
    csv_folder = "./Results/RetrievalStrategy/csv"
    open_csv_file(csv_folder)
    pass


if __name__ == "__main__":
    main()