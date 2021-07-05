import pandas as pd

f1name = "log-at-202105221637"
# f1name = "log-at-202105091555"
# log-at-
f2name = "tmp3.csv"
f2 = open(f2name, "w")
cols = ['Date', "is_tdd","MCC", "MNC", "CID", "PCI","earfcn", "freq_band_ind","UL_bandwidth","DL_bandwidth","TAC","RSRP","RSRQ","RSSI","SINR","CQI","tx_power","srxlev",
    "MCC_5g","MNC_5g","PCI_5g","RSRP_5g","SINR_5g","RSRQ_5g","ARFCN_5g","band_5g",
    "mode1","earfcn1","PCI1","RSRQ1","RSRP1",
    "mode2","earfcn2","PCI2","RSRQ2","RSRP2",
    "mode3","earfcn3","PCI3","RSRQ3","RSRP3",
    "mode4","earfcn4","PCI4","RSRQ4","RSRP4",
    "mode5","earfcn5","PCI5","RSRQ5","RSRP5",
    "mode6","earfcn6","PCI6","RSRQ6","RSRP6",
    "mode7","earfcn7","PCI7","RSRQ7","RSRP7",
    "mode8","earfcn8","PCI8","RSRQ8","RSRP8",
    ] 

earfcn = None
is_5g = False
filled_5g = False
f2.write(",".join(cols))
with open(f1name) as f1:
    l = f1.readline()
    l2 = []
    l3 = []
    while l:
        l = l.replace('\n', '')
        # print(l)
        if "neighbourcell" not in l and '+QENG' in l and 'LTE' in l:
            """
                In LTE mode: 
                +QENG:  "servingcell",<state>,"LTE",<is_tdd>,<MCC>,<
                MNC>,<cellID>,<PCID>,<earfcn>,<freq_band_ind>,<UL_b
                andwidth>,<DL_bandwidth>,<TAC>,<RSRP>,<RSRQ>,<R
                SSI>,<SINR>,<CQI>,<tx_power>,<srxlev>   
                In WCDMA mode: 
                +QENG:  "servingcell",<state>,"WCDMA",<MCC>,<MN
                C>,<LAC>,<cellID>,<uarfcn>,<PSC>,<RAC>,<RSCP>,<eci
                o>,<phych>,<SF>,<slot>,<speech_code>,<comMod>   


                In EN-DC mode:
                    +QENG: "LTE",<is_tdd>,<MCC>,<MNC>,<cellID>,<PCID>,<earfcn>,<freq_band_ind>,
                    <UL_bandwidth>,<DL_bandwidth>,<TAC>,<RSRP>,<RSRQ>,<RSSI>,<SINR>,<CQI>,<tx_power>,<srxlev>
            """
            # print(l)
            # print(l.split(","), len(l.split(",")))
            # l = l[2:]
            l = l.split(",")
            # print("l", l)
            # print("len(l)", len(l))

            if len(l) == 18:
                l2 += l[1:]
                earfcn = l[6]
            else:
                # print("LTE?", l)
                l2 += l[2:]
                earfcn = l[8]
            # print(earfcn)
            # print("l2", l2)
        elif "neighbourcell" not in l in l and '+QENG' in l and 'NR5G-NSA' in l:
            """
                "OK":+QENG: "NR5G-NSA",<MCC>,<MNC>,<PCID>,<RSRP>,<SINR>,<RSRQ>,<ARFCN>,<band>
                "FAIL":+QENG: "NR5G-NSA",<MCC>,<MNC>,<RSRP>,<SINR>,<RSRQ>,<ARFCN>,<band>
            """
            l = l.split(",")
            is_5g = True
            # print( "5g len",len(l[2:]), l)
            # print(len(l))
            if (len(l) == 7):
                l2 += l[1:3]
                l2.append("-1")
                l2 += l[3:]
                l2.append("0")
            else:
                l2 += l[1:]
        elif "neighbourcell" in l and '+QENG' in l:

            """
            In LTE mode:   
            [+QENG:  "neighbourcell  intra",1"LTE",2<earfcn>,3<PCID>,4<
            RSRQ>,5<RSRP>,6<RSSI>,7<SINR>,<srxlev>,<cell_resel_pri
            ority>,<s_non_intra_search>,<thresh_serving_low>,<s_i
            ntra_search> 
            …] 
            [+QENG:  "neighbourcell  inter",1"LTE",2<earfcn>,3<PCID>,4<
            RSRQ>,5<RSRP>,6<RSSI>,7<SINR>,<srxlev>,<cell_resel_pri
            ority>,<threshX_low>,<threshX_high> 
            …] 
            [+QENG:"neighbourcell",1"WCDMA",2<uarfcn>,<cell_resel
            _priority>,<thresh_Xhigh>,<thresh_Xlow>,<PSC>,<RSC
            P><ecno>,<srxlev> 
            …] 
            """

            # print(l)
            l = l.replace("\"" , "")
            l = l.split(",")

            if "LTE" in l and earfcn == l[2]:
                l3.append(l[1])
                l3.append(l[2])
                l3.append(l[3])
                l3.append(l[4])
                l3.append(l[5])
            
        elif "QLTS" in l:
            # print("-"*10)
            # print(l)
            x = l.find("\"")
            y = l.find("\"", x+1)
            # print(x,  y)
            ctime = l[x+1:y-5]
            ctime = ctime.replace(",", "-")
            # print(ctime)
            # print(l2)
            if not is_5g:
                l2 += ['0'] * 7
            if len(l2):
                # print("l2", l2)
                # print("l3", l3)
                f2.write(",".join(l2+l3)+"\n")
            l3 = []
            l2 = [ctime]
            # print(l2)
            pass
            is_5g = False

        l = f1.readline()

f2.close()