import os
import pandas as pd

os.makedirs('data', exist_ok=True)
os.makedirs('prompts', exist_ok=True)

# 30 Comprehensive Cases Dataset
cases_data = [
    ["C01", "PC cannot ping Default Gateway", "Gig0/0 is administratively down, line protocol is down", "Port shutdown on Router", "Layer 1", "Gateway", "High"],
    ["C02", "PC gets APIPA 169.254.x.x", "DHCP pool exhausted / pool scope misconfigured", "DHCP pool range error", "Layer 7", "DHCP", "High"],
    ["C03", "Inter-VLAN ping fails across Switch", "switchport trunk allowed vlan 10,20 (Missing 30)", "Trunk missing required VLAN", "Layer 2", "VLAN", "High"],
    ["C04", "Router cannot reach remote branch", "Gateway of last resort is not set", "Missing default static route", "Layer 3", "Routing", "Critical"],
    ["C05", "HTTP fails but ICMP ping works", "access-list 101 deny tcp any any eq 80 matches 42", "ACL blocking HTTP port 80", "Layer 4", "ACL", "High"],
    ["C06", "LAN hosts cannot browse internet", "ip nat inside source list 1 int Gig0/1 (ACL 1 empty)", "NAT standard ACL misconfigured", "Layer 3", "NAT", "Critical"],
    ["C07", "OSPF neighbor stuck in INIT", "Hello 10, Dead 40 vs Hello 10, Dead 30 mismatch", "OSPF timer mismatch", "Layer 3", "OSPF", "High"],
    ["C08", "Switch loop and high CPU usage", "Spanning-tree disabled on vlan 10", "STP disabled causing loop", "Layer 2", "STP", "Critical"],
    ["C09", "VLAN 20 PC ping to sub-interface fails", "encapsulation dot1Q 10 on sub-interface g0/0.20", "Dot1Q tag mismatch", "Layer 3", "RoAS", "High"],
    ["C10", "Domain ping fails, IP ping works", "DHCP DNS server option points to 127.0.0.1", "Wrong DNS IP in DHCP pool", "Layer 7", "DNS", "Medium"],
    ["C11", "Wi-Fi client cannot connect", "WPA2 Pre-Shared Key mismatch error in log", "Wi-Fi password mismatch", "Layer 2", "Wireless", "High"],
    ["C12", "SSH to router refused", "show ip ssh: SSH disabled - crypto key zeroize", "Missing RSA crypto key", "Layer 7", "Security", "Medium"],
    ["C13", "Sub-interfaces all down", "Gig0/0 (parent) is administratively down", "Physical parent interface shutdown", "Layer 1", "RoAS", "High"],
    ["C14", "IP collision warning on console", "%IP-4-DUPADDR: Duplicate address 192.168.1.5", "Static IP inside DHCP range", "Layer 3", "IPAM", "Medium"],
    ["C15", "SSH connection closed by remote host", "transport input telnet under line vty 0 4", "VTY allows Telnet only", "Layer 7", "Mgmt", "Medium"],
    ["C16", "OSPF route not received", "network 10.0.0.0 0.0.0.255 area 1 (Expected area 0)", "OSPF Area ID mismatch", "Layer 3", "OSPF", "High"],
    ["C17", "Routing table drops packets", "ip route 0.0.0.0 0.0.0.0 192.168.2.2 (Next-hop unreachable)", "Invalid next-hop address", "Layer 3", "Routing", "High"],
    ["C18", "CDP native vlan mismatch warning", "%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN 1 vs 99", "Trunk Native VLAN mismatch", "Layer 2", "Switching", "Medium"],
    ["C19", "Switch port err-disabled", "show int status err-disabled (BPDU received on portfast)", "BPDUGuard violation", "Layer 2", "STP", "High"],
    ["C20", "PAT translation drops packets", "NAT pool exhausted, missing 'overload' parameter", "Static NAT port exhaustion", "Layer 3", "NAT", "High"],
    ["C21", "VLAN 10 clients receive no DHCP IP", "ip helper-address 10.0.0.99 (DHCP is at 10.0.0.100)", "Wrong DHCP relay helper address", "Layer 3", "DHCP", "High"],
    ["C22", "Guest Wi-Fi accessing internal DB", "access-list Guest_In permit ip any any", "Missing guest isolation ACL", "Layer 4", "Wireless", "Critical"],
    ["C23", "Remote subnet cannot ping Switch IP", "ip default-gateway missing on L2 switch", "Missing switch default gateway", "Layer 3", "Switching", "Medium"],
    ["C24", "Intermittent packet loss on subnet", "Router int mask /28, Client mask configured /24", "Subnet mask mismatch", "Layer 3", "Addressing", "Medium"],
    ["C25", "New host port shuts down immediately", "Port-security violation: MAC count exceeded limit 1", "Port security MAC violation", "Layer 2", "Security", "Medium"],
    ["C26", "EIGRP neighbor not forming", "router eigrp 10 vs router eigrp 20 on peer", "EIGRP AS number mismatch", "Layer 3", "EIGRP", "High"],
    ["C27", "Jumbo frames dropped", "MTU 1500 on Switch1, MTU 9000 on Switch2", "MTU size mismatch", "Layer 2", "Switching", "Low"],
    ["C28", "Ping works outbound, response dropped", "Inbound ACL blocking ICMP echo-reply packets", "Missing stateful/return ACL rule", "Layer 4", "ACL", "High"],
    ["C29", "NTP time out of sync", "NTP server unreachable / stratum 16", "NTP UDP 123 blocked by firewall", "Layer 7", "NTP", "Low"],
    ["C30", "Dual Active HSRP routers", "standby 1 priority 110 on both, hello multicast blocked", "HSRP hello packets dropped", "Layer 3", "HSRP", "High"]
]

cases_columns = ["Case_ID", "Symptom", "Show_Outputs", "Expected_Fault", "OSI_Layer", "Concept", "Severity"]
df_cases = pd.DataFrame(cases_data, columns=cases_columns)
df_cases.to_csv("data/cases.csv", index=False)

# 5 Responsible AI Logs
ai_logs = [
    ["C09", "Dot1Q tag mismatch", "Switch Trunk Encapsulation protocol failure (L2)", "Sub-interface dot1Q encapsulation ID mismatch on Router (L3)", "Edited", "AI confused switch trunking with Router-on-a-Stick sub-interface."],
    ["C06", "NAT standard ACL misconfigured", "ISP Uplink interface is down (L1)", "NAT ACL 1 is empty; traffic is not matched for translation (L3)", "Rejected", "AI hallucinated physical layer fault instead of checking ACL config."],
    ["C19", "BPDUGuard violation", "Defective Ethernet cable / Hardware failure (L1)", "BPDU received on PortFast enabled port triggered BPDUGuard (L2)", "Edited", "AI suggested cable replacement for an err-disabled software state."],
    ["C22", "Missing guest isolation ACL", "Configure separate DHCP pool for guest Wi-Fi", "Apply Layer 4 ACL blocking guest subnet from private RFC1918 range", "Rejected", "AI solved IP addressing instead of resolving security isolation."],
    ["C23", "Missing switch default gateway", "Configure 'ip route 0.0.0.0 0.0.0.0' on Switch", "Configure 'ip default-gateway' command on Layer 2 Switch", "Edited", "AI gave Layer 3 routing command for a Layer 2 switch."]
]

logs_columns = ["Case_ID", "Actual_Fault", "AI_Initial_Diagnosis", "Human_Corrected_Diagnosis", "Review_Status", "Reason_For_Correction"]
df_logs = pd.DataFrame(ai_logs, columns=logs_columns)
df_logs.to_csv("data/responsible_ai_log.csv", index=False)

print("SUCCESS: cases.csv and responsible_ai_log.csv generated successfully!")