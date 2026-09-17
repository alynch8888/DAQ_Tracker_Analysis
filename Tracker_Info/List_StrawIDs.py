from tracker_info import Tracker
import math
##Need to edit this one. I asked Claude to reverse my StrawID_to_PPS_Convert.py but I don't care for the way it is done.
d16 = "0000000000000000"


for slot in range(len(Tracker)):
    print("="*50)#00)
    for plane_key in Tracker[slot]:
        # print("Min:",)
        print("-"*50)
        Plane_bits = format(plane_key, "06b")
        # print("Plane",format(i, "06b"))
        for panel_idx in range(len(Tracker[slot][plane_key])):
            entry = Tracker[slot][plane_key][panel_idx]
            # print(range(len(Tracker[slot][plane_key])))
            # print("Range",Tracker[slot][plane_key])
            print("Station",entry["Station"],f"({slot})")
            print("     Plane",entry["PPID"])
            Panel_bits = format(panel_idx, "03b")
            print("         Panel","MN"+str(Tracker[slot][plane_key][panel_idx]["MNID"]),f"({panel_idx})")
            # for Straw in range(96):
            #     straw_bin = format(Straw, "07b")
            #     strawid_bits = Plane_bits + Panel_bits + straw_bin
            #     strawid_0d = int(strawid_bits,2)
            #     print("             StrawID", strawid_0d, f"({strawid_bits})")
            straw_bin_min = format(0, "07b")
            straw_bin_max = format(95, "07b")
            strawid_bits_min = Plane_bits + Panel_bits + straw_bin_min
            strawid_bits_max = Plane_bits + Panel_bits + straw_bin_max
            strawid_0d_min = int(strawid_bits_min,2)
            strawid_0d_max = int(strawid_bits_max,2)
            print("             StrawID", strawid_0d_min)#, f"({strawid_bits_min})")
            print("             StrawID", strawid_0d_max)#, f"({strawid_bits_max})")
        print("-"*50)