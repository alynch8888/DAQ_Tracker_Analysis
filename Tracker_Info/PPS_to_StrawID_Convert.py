from tracker_info import Tracker
import math
##Need to edit this one. I asked Claude to reverse my StrawID_to_PPS_Convert.py but I don't care for the way it is done.
d16 = "0000000000000000"

# pln0d = int(input("What Plane(0d) are you converting? "))
# pnl0d = int(input("What Panel(0d) are you converting? "))
# stw0d = int(input("What Straw(0d) are you converting? "))
# print("Plane", pln0d)
# print("Panel", pnl0d)
# print("Straw", stw0d)
# print("-"*10)
# # Plane = Tracker[math.floor(pln0d/2)][pln0d][pnl0d]
# # print(Plane)
# # print("Station "+str(Plane["Station"]))
# # print("Plane "+str(Plane["PPID"]))
# # print("MN"+str(Plane["MNID"]))
# # print("-"*10)

# pln0b = format(pln0d, "06b")   # 6 bits
# pnl0b = format(pnl0d, "03b")   # 3 bits
# stw0b = format(stw0d, "07b")   # 7 bits
# print("Plane(0b):", pln0b)
# print("Panel(0b):", pnl0b)
# print("Straw(0b):", stw0b)
# print("-"*10)

# d = pln0b + pnl0b + stw0b
# print("16d Binary StrawID:", d)
# print("-"*10)

# strawid_0d = int(d, 2)
# print("StrawID(0d)", strawid_0d)
# print("-"*10)
for slot in range(len(Tracker)):
    for plane_key in range(len(Tracker[slot])):
        Plane_bits = format(plane_key, "06b")
        # print("Plane",format(i, "06b"))
        for panel_idx in range(len(Tracker[slot][plane_key])):
            entry = Tracker[slot][plane_key][panel_idx]
            print(range(len(Tracker[slot][plane_key])))
            print("Range",Tracker[slot][plane_key])
            print("Station",entry["Station"])
            print("     Plane",entry["PPID"])
            Panel_bits = format(panel_idx, "03b")
            print("         Panel","MN"+str(Tracker[slot][plane_key][panel_idx]["MNID"]),f"({panel_idx})")
            for Straw in range(10):
                straw_bin = format(Straw, "07b")
                strawid_bits = Plane_bits + Panel_bits + straw_bin
                strawid_0d = int(strawid_bits,2)
                print("             StrawID", strawid_0d, f"({strawid_bits})")

        