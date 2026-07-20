def totalcalc(bill_amnt, tip_perc): #this is the func
    total = bill_amnt + bill_amnt*tip_perc/100
    total = round(total, 2)
    print("Pay us $", total, sep="")

    totalcalc(150, 20)

