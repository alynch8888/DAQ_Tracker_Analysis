d16="0000000000000000"
strawid_0d=int(input("What StrawID(0d) are you converting? "))
# strawid_0d=13334
print("StrawID(0d)",strawid_0d)
int_stwid=bin(strawid_0d)
strawid_0b=str(int(int_stwid[2:]))
print("Strawid(0b):",strawid_0b)
strawid=strawid_0b
if len(strawid)<len(d16):
    b=len(d16)-len(strawid)
    d="0"*b+strawid
    print("Adding",b,"zeros to",strawid)
    # print("len(d)=",len(d))
else:
    d=strawid
    print(len(d),"digits, no additional zeros needed")
    # print("len(d)=",len(d))
print("16d Binary StrawID:",d)
pln0b, pnl0b, stw0b = d[0:6], d[6:9], d[9:16]
print("Plane",str(pln0b))
print("Panel",str(pnl0b))
print("Straw",str(stw0b))
pln0d, pnl0d, stw0d = int(d[0:6],2), int(d[6:9],2), int(d[9:16],2)
print("Plane",str(pln0d))
print("Panel",str(pnl0d))
print("Straw",str(stw0d))
