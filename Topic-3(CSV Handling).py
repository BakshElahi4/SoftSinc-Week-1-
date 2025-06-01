
# Task

# import csv
# import datetime
# import os

# def parse_csv(file_path):
#     with open(file_path, 'r', newline='', encoding='utf-8') as file:
#         reader = list(csv.DictReader(file))
#     return reader

# def find_missing_rows(data):
#     return [row for row in data if any(value.strip() == '' for value in row.values())]

# def count_unique_per_column(data):
#     unique_counts = {}
#     for key in data[0]:
#         unique_counts[key] = len(set(row[key] for row in data if row[key].strip() != ''))
#     return unique_counts

# def generate_report(data, missing_rows, unique_counts, report_path):
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     with open(report_path, 'w', encoding='utf-8') as report:
#         report.write(f"CSV Analysis Report\n")
#         report.write(f"Timestamp: {timestamp}\n")
#         report.write(f"Total Rows: {len(data)}\n")
#         report.write(f"Rows with Missing Values: {len(missing_rows)}\n\n")

#         report.write("🧮 Unique Entries per Column:\n")
#         for col, count in unique_counts.items():
#             report.write(f"  - {col}: {count} unique values\n")

#         report.write("\n🔍 Sample Row with Missing Data:\n")
#         if missing_rows:
#             report.write(str(missing_rows[0]) + "\n")
#         else:
#             report.write("None found.\n")

#     print(f"Report saved to {report_path}")


# # ------------------ Run the Parser ------------------ #
# if __name__ == "__main__":
#     csv_path = input("Enter CSV file path: ").strip()
#     if not os.path.exists(csv_path):
#         print("File not found.")
#     else:
#         data = parse_csv(csv_path)
#         missing_rows = find_missing_rows(data)
#         unique_counts = count_unique_per_column(data)

#         report_file = "csv_report.txt"
#         generate_report(data, missing_rows, unique_counts, report_file)



#####################################     Challenge #########################



# import os
# import datetime

# # Keywords to identify error messages
# ERROR_KEYWORDS = ['ERROR', 'Exception', 'CRITICAL', 'FAIL']

# def scan_logs(directory):
#     summary = {}
    
#     for filename in os.listdir(directory):
#         if filename.endswith('.log') or filename.endswith('.txt'):
#             file_path = os.path.join(directory, filename)
#             error_count = 0

#             with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
#                 for line in file:
#                     if any(keyword in line for keyword in ERROR_KEYWORDS):
#                         error_count += 1

#             summary[filename] = error_count

#     return summary

# def write_report(summary, output_path):
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open(output_path, 'w', encoding='utf-8') as report:
#         report.write(f"Weekly Log Summary Report\n")
#         report.write(f"Generated on: {timestamp}\n\n")
        
#         if not summary:
#             report.write("No .log or .txt files found.\n")
#         else:
#             for file, count in summary.items():
#                 report.write(f"{file}: {count} error(s) found\n")

#     print(f"Report saved to: {output_path}")


# # ------------ MAIN -------------- #
# if __name__ == "__main__":
#     folder_path = input("Enter the log directory path: ").strip()
#     if not os.path.exists(folder_path):
#         print("Directory not found.")
#     else:
#         results = scan_logs(folder_path)
#         report_name = "weekly_log_report.txt"
#         write_report(results, report_name)
