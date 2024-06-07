import json
import csv
import subprocess

# Step 1: Run Bandit and generate JSON output
# Replace 'your_script.py' with the target script or directory
result = subprocess.run(['bandit', '-r', '/Vulnerable Code Snippets/', '-f', 'json'], capture_output=True, text=True)
bandit_output = result.stdout
print(bandit_output)
# Step 2: Parse the JSON output
bandit_data = json.loads(bandit_output)

# Step 3: Convert parsed data into CSV format
csv_data = []
headers = ['Filename', 'Line Number', 'Issue Severity', 'Issue Confidence', 'Issue Text', 'More Info']

for result in bandit_data['results']:
    csv_data.append([
        result['filename'],
        result['line_number'],
        result['issue_severity'],
        result['issue_confidence'],
        result['issue_text'],
        result['more_info']
    ])

# Step 4: Write the CSV data to a file
csv_filename = 'compliance_report.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(headers)  # Write the header
    csvwriter.writerows(csv_data)  # Write the data

print(f"CSV file '{csv_filename}' has been created successfully.")
