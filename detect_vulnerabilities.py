import re
import os

# Patterns to detect common vulnerabilities
patterns = {
    "SQL Injection": r".*Statement.*execute.*\+.*",
    "XSS": r".*response\.getWriter\(\).*",
    "Hardcoded Secrets": r".*password\s*=\s*\".*\"",
    "Insecure Deserialization": r".*ObjectInputStream.*",
    "Command Injection": r".*Runtime\.getRuntime\(\).*exec\(.*\+.*\)"
}

def check_vulnerabilities(file_path):
    vulnerabilities = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, 1):
            for vulnerability, pattern in patterns.items():
                if re.search(pattern, line):
                    vulnerabilities.append((vulnerability, line_number, line.strip()))
    return vulnerabilities

def scan_directory(directory):
    all_vulnerabilities = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                vulnerabilities = check_vulnerabilities(file_path)
                if vulnerabilities:
                    all_vulnerabilities[file_path] = vulnerabilities
    return all_vulnerabilities

def main():
    directory = input("Enter the directory path to scan for vulnerabilities: ")
    vulnerabilities = scan_directory(directory)
    
    if not vulnerabilities:
        print("No vulnerabilities found.")
    else:
        print("Vulnerabilities found:")
        for file_path, issues in vulnerabilities.items():
            print(f"\nFile: {file_path}")
            for vulnerability, line_number, line in issues:
                print(f"  [Line {line_number}] {vulnerability}: {line}")

if __name__ == "__main__":
    main()
