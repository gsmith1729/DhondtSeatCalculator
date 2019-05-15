seats=7
parties={
    "CON":[50,0],
    "LAB":[20,0],
    "BRX":[15,0],
    "UKIP":[2,0],
    "CHUK":[3,0],
    "LBD":[8,0],
    "GRN":[2,0]
}
for i in range(0,seats-1):
    lp=""
    mv=0
    for i in parties:
        if (parties[i][0]/(parties[i][1]+1)>mv):
            mv=parties[i][0]/(parties[i][1]+1)
            lp=i
    parties[lp][1]+=1
