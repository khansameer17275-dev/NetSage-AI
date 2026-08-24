import re
import pandas as pd

def check_cli_rules(show_output: str) -> list:
    issues = []
    # Check 1: Admin down
    if re.search(r'administratively down', show_output, re.IGNORECASE):
        issues.append("[Rule L1-01] Interface is administratively shutdown. Run 'no shutdown'.")

    # Check 2: Missing Gateway
    if re.search(r'gateway of last resort is not set', show_output, re.IGNORECASE):
        issues.append("[Rule L3-01] Default route missing. Run 'ip route 0.0.0.0.0.0.0.0 <next-hop>'.")

    # Check 3: ACL Deny Hit
    if re.search(r'deny .* matches', show_output, re.IGNORECASE):
        issues.append("[Rule L4-01] Packets actively dropping due to ACL Deny entry.")

    # Check 4: Mismatch conditions
    if re.search(r'mismatch', show_output, re.IGNORECASE):
        issues.append("[Rule L2/L3-02] Configuration mismatch detected (VLAN/Timers/AS-Number).")

    # Check 5: Err-disabled 
    if re.search(r'err-disabled', show_output, re.IGNORECASE):
        issues.append("[Rule L2-03] Port in err-disabled state (Check Port-Security / BPDUGuard).")

    return issues

if __name__ == "__main__":
    df = pd.read_csv("data/cases.csv")
    print("--- Running Deterministics Rule Checker on Lab Dataset ---\n")
    for idx, row in df.head(6).iterrows():
        print(f"Checking {row['Case_ID']} - Symptom: {row['Symptom']}")
        detections = check_cli_rules(row['Show_Outputs'])
        if detections:
            for d in detections:
                print(f"  --> DETECTED: {d}")
            else:
                print("  --> No simple rule triggered. (Needs LLM deep analysis)")
            print("-" * 60)