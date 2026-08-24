import pandas as pd

cases_df = pd.read_csv("data/cases.csv")
logs_df = pd.read_csv("data/responsible_ai_log.csv")

total_cases = len(cases_df)
corrected_cases = len(logs_df)
accepted_cases = total_cases - corrected_cases
agreement_rate = (accepted_cases / total_cases) * 100

print("=" * 45)
print("       NETSAGE AI - PROJECT DASHBOARD        ")
print("=" * 45)
print(f"Total Troubleshooting Cases : {total_cases}")
print(f"AI Accepted Directly        : {accepted_cases}")
print(f"Human Corrected/Edited      : {corrected_cases}")
print(f"AI-Human Agreement Rate     : {agreement_rate:.2f}%\n")

print("--- Breakdown by OSI Layer ---")
print(cases_df['OSI_Layer'].value_counts().to_string())

print("\n--- Breakdown by Network Concept ---")
print(cases_df['Concept'].value_counts().to_string())

print("\n--- Breakdown by Severity ---")
print(cases_df['Severity'].value_counts().to_string())
print("=" * 45)