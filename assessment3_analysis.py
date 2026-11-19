"""
MOBILE COMPUTING – ASSESSMENT 3 (CO3)
Python analysis and graph generation for Q1–Q7.

Install: pip install matplotlib numpy
Run:     python assessment3_analysis.py

All numerical values below are taken from the assignment's worked examples
(pages 37–43). They are illustrative/assumed values, not measured testbed data.
The script creates one PNG dashboard per question in the "graphs" folder.
"""
import os
import matplotlib.pyplot as plt
import numpy as np

GRAPH_DIR = "graphs"
os.makedirs(GRAPH_DIR, exist_ok=True)

def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(GRAPH_DIR, name), dpi=160, bbox_inches="tight")
    plt.close(fig)

# Q1 – Wireless network architecture and mobility
# Problem 1: 24 Mbps shared equally by 8 devices = 3 Mbps/device.
fig, ax = plt.subplots(1, 3, figsize=(15, 4.5))
nodes = np.arange(1, 13)
ax[0].plot(nodes, 24/nodes, marker="o")
ax[0].set(title="Q1: Average bandwidth per device", xlabel="Active devices", ylabel="Mbps per device")
ax[0].grid(True)
labels = ["Transmission", "Propagation", "Processing", "Queueing", "Handoff"]
times = [8, 5, 3, 9, 25]
ax[1].bar(labels, times)
ax[1].set(title="Q1: Delay components (total = 50 ms)", ylabel="Delay (ms)")
ax[1].tick_params(axis="x", rotation=35)
ax[1].grid(axis="y")
ax[2].bar(["Received", "Lost"], [960, 40])
ax[2].set(title="Q1: Packet outcome (1000 sent)", ylabel="Packets")
ax[2].text(0, 960, "PDR 96%", ha="center", va="bottom")
ax[2].text(1, 40, "PLR 4%", ha="center", va="bottom")
ax[2].grid(axis="y")
save(fig, "Q1_wireless_mobility.png")

# Q2 – Mobile IP and mobility management
fig, ax = plt.subplots(1, 3, figsize=(15, 4.5))
ax[0].bar(["Original", "Encapsulated"], [1000, 1020])
ax[0].set(title="Q2: Mobile IP packet size", ylabel="Bytes")
ax[0].text(0.5, 1010, "+20-byte outer header", ha="center")
ax[0].grid(axis="y")
stages = ["Agent\ndiscovery", "CoA\nacquisition", "Registration", "Route\nupdate", "Recovery"]
stage_ms = [40, 30, 60, 20, 15]
ax[1].bar(stages, stage_ms)
ax[1].set(title="Q2: Mobility delay (total = 165 ms)", ylabel="Delay (ms)")
ax[1].grid(axis="y")
ax[2].bar(["Triangular", "Direct"], [80, 50])
ax[2].set(title="Q2: Routing path delay", ylabel="One-way delay (ms)")
ax[2].text(0, 80, "+30 ms / +60%", ha="center", va="bottom")
ax[2].grid(axis="y")
save(fig, "Q2_mobile_ip.png")

# Q3 – Cellular versus ad hoc wireless networks
fig, ax = plt.subplots(1, 3, figsize=(15, 4.5))
hops = ["A–B", "B–C", "C–D"]
delays = [12, 15, 18]
ax[0].bar(hops, delays)
ax[0].set(title="Q3: Multi-hop delay (total = 45 ms)", ylabel="Per-hop delay (ms)")
ax[0].grid(axis="y")
rates = [12, 8, 10]
ax[1].bar(hops, rates)
ax[1].axhline(min(rates), linestyle="--", label="Path bottleneck = 8 Mbps")
ax[1].set(title="Q3: Link rates and bottleneck", ylabel="Link rate (Mbps)")
ax[1].legend()
ax[1].grid(axis="y")
ax[2].bar(["Uptime", "Downtime"], [22, 2])
ax[2].set(title="Q3: Cellular availability (24 hours)", ylabel="Hours")
ax[2].text(0, 22, "91.67% available", ha="center", va="bottom")
ax[2].grid(axis="y")
save(fig, "Q3_cellular_vs_adhoc.png")

# Q4 – Mobile IP application: ambulance / mobile healthcare
fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))
ax[0].bar(["Received", "Lost"], [485, 15])
ax[0].set(title="Q4: Ambulance packets (500 sent)", ylabel="Packets")
ax[0].text(0, 485, "PDR 97%", ha="center", va="bottom")
ax[0].text(1, 15, "PLR 3%", ha="center", va="bottom")
ax[0].grid(axis="y")
packet_delays = [40, 45, 50, 55, 60]
ax[1].plot(range(1, 6), packet_delays, marker="o")
ax[1].axhline(np.mean(packet_delays), linestyle="--", label="Average = 50 ms")
ax[1].set(title="Q4: Packet end-to-end delay", xlabel="Packet number", ylabel="Delay (ms)")
ax[1].legend()
ax[1].grid(True)
save(fig, "Q4_mobile_ip_application.png")

# Q5 – Proactive routing (DSDV)
fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))
ax[0].bar(["Old route\nD-20", "New route\nD-22"], [2, 3])
ax[0].set(title="Q5: DSDV route to D", ylabel="Hop count")
ax[0].text(1, 3, "Selected: newer sequence number", ha="center", va="bottom")
ax[0].grid(axis="y")
seconds = np.arange(0, 61, 5)
updates = (seconds // 5) * 10
ax[1].step(seconds, updates, where="post")
ax[1].set(title="Q5: Cumulative periodic DSDV updates", xlabel="Time (seconds)", ylabel="Update transmissions")
ax[1].text(60, 120, "120 per minute", ha="right", va="bottom")
ax[1].grid(True)
save(fig, "Q5_dsdv.png")

# Q6 – Reactive routing (AODV)
fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))
ax[0].bar(["DSDV lookup", "AODV discovery"], [5, 75])
ax[0].set(title="Q6: Initial route setup delay", ylabel="Delay (ms)")
ax[0].text(1, 75, "15×", ha="center", va="bottom")
ax[0].grid(axis="y")
ax[1].bar(["Control packets", "Data packets"], [30, 270])
ax[1].set(title="Q6: AODV packet-count overhead example", ylabel="Packets")
ax[1].text(0, 30, "11.11 per 100 data", ha="center", va="bottom")
ax[1].grid(axis="y")
save(fig, "Q6_aodv.png")

# Q7 – Emergency mobile network validation
fig, ax = plt.subplots(2, 2, figsize=(12, 8))
stages = ["Discovery", "Address", "Registration", "Route update", "Recovery"]
stage_ms = [25, 20, 45, 15, 10]
ax[0,0].bar(stages, stage_ms)
ax[0,0].set(title="Q7: Emergency mobility delay (total = 115 ms)", ylabel="Delay (ms)")
ax[0,0].tick_params(axis="x", rotation=25)
ax[0,0].grid(axis="y")
ax[0,1].bar(["Received", "Lost"], [1960, 40])
ax[0,1].set(title="Q7: Emergency packets (2000 sent)", ylabel="Packets")
ax[0,1].text(0, 1960, "PDR 98%", ha="center", va="bottom")
ax[0,1].text(1, 40, "PLR 2%", ha="center", va="bottom")
ax[0,1].grid(axis="y")
emergency_delays = [35, 40, 45, 60]
ax[1,0].plot(range(1,5), emergency_delays, marker="o")
ax[1,0].axhline(np.mean(emergency_delays), linestyle="--", label="Average = 45 ms")
ax[1,0].set(title="Q7: Emergency packet delay", xlabel="Packet number", ylabel="Delay (ms)")
ax[1,0].legend()
ax[1,0].grid(True)
ax[1,1].bar(["Routing overhead", "Gateway availability"], [6, 95.83])
ax[1,1].set(title="Q7: Network performance percentages", ylabel="Percent (%)")
ax[1,1].set_ylim(0, 105)
ax[1,1].text(0, 6, "6%", ha="center", va="bottom")
ax[1,1].text(1, 95.83, "95.83%", ha="center", va="bottom")
ax[1,1].grid(axis="y")
save(fig, "Q7_emergency_network.png")

print("Created 7 graph files in:", GRAPH_DIR)
print("Q1–Q7 graphs use the assignment's illustrative worked-example values.")
