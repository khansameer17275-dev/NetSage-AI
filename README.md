Markdown# NetSage AI - Network Troubleshooting Assistant

A practical troubleshooting copilot built for Cisco Packet Tracer labs. It takes raw network symptoms and CLI `show` outputs, analyzes them across OSI layers, and suggests fixes while always requiring a human engineer to verify before applying.

---

## What Problem Does This Solve?
In networking labs, finding the root cause of an issue is tricky. When a PC can't reach a server, the issue could be anything: a down interface, a wrong VLAN, an empty NAT ACL, or a missing route. 

NetSage AI solves this in two steps:
1. **Deterministic Rule Checks:** A Python script instantly catches obvious mistakes (like shutdown ports or missing routes).
2. **AI-Assisted Diagnosis:** A structured LLM prompt analyzes deeper issues and provides evidence-backed fixes.
3. **Human Review Safety:** Every AI recommendation is marked as Accepted, Edited, or Rejected to prevent misconfigurations in the network.

---

## Project Structure

```text
NetSage_AI/
│
├── data/
│   ├── cases.csv                 # 30 lab scenarios across OSI L1 to L7
│   └── responsible_ai_log.csv    # 5 documented cases where AI was corrected
│
├── prompts/
│   └── diagnose_prompt.md        # Structured JSON prompt for AI diagnosis
│
├── generate_dataset.py           # Script to generate/refresh CSV data
├── rule_checker.py               # Deterministic rule engine for CLI outputs
├── dashboard.py                  # Generates metrics & visual charts
├── dashboard_summary.png         # Exported visual dashboard
└── README.md
How to Set Up and Run

1. RequirementsMake sure Python 3.10+ is installed along with the required libraries:Bashpip install
pandas matplotlib seaborn

2. Generate the DatasetCreate the 30 lab cases and human review logs:  Bashpython generate_dataset.py

3. Run the Rule CheckerScan lab show-command outputs for deterministic faults:  Bashpython rule_checker.py

4. Open the Visual DashboardView the agreement rates, layer breakdown, and export charts:  Bashpython dashboard.py
Responsible AI & Human Review (Key Takeaways)AI can sometimes hallucinate or misdiagnose network faults.

In data/responsible_ai_log.csv, 5 real failure modes are documented:  RoAS Issue (C09): AI blamed the
 switch trunk protocol, but the actual issue was a sub-interface 802.1Q encapsulation mismatch on the router.  NAT Misconfiguration (C06): AI assumed the link was down, but the actual root cause was an empty standard ACL in the NAT pool.  Err-disabled Port (C19): AI suggested changing the physical cable, while the issue was a BPDUGuard violation.  Guest Wi-Fi Isolation (C22): AI tried to fix DHCP, whereas the real fix was adding an inbound ACL rule[cite: 1].L2 Switch Management (C23): AI gave a Layer 3 ip route command instead of ip default-gateway for an L2 switch[cite: 1].Deliverables Status[x] 30 Lab Troubleshooting Cases (cases.csv)[cite: 1][x] Structured JSON Prompt (diagnose_prompt.md)[cite: 1][x] Python Deterministic Checker (rule_checker.py)[cite: 1][x] 5 Responsible AI Logs (responsible_ai_log.csv)[cite: 1][x] Visual Analytics Dashboard (dashboard.py / dashboard_summary.png)[cite: 1]
