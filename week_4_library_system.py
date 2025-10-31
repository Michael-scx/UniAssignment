def calc_borrow_vol(mat, items, mem):     
    if mat == "books":
        if mem == "basic":
            rate = 3
        elif mem == "standard":
            rate = 5
        else:
            rate = 8
    elif mat == "media":
        if mem == "basic":
            rate = 2
        elif mem == "standard":
            rate = 4
        else:
            rate = 6
    else:   
        if mem == "basic":
            rate = 1
        elif mem == "standard":
            rate = 2
        else:
            rate = 3
    vol = items * rate
    return vol


def calc_usage_freq(yrs, base, act):
    exp = 1000 + yrs*100
    capa = exp - base
    freq = (act - base) / capa * 100
    return freq


def get_user_cat(freq):
    if freq < 50:
        return "Occasional User"
    elif freq < 60:
        return "Regular User"
    elif freq < 70:
        return "Frequent User"
    elif freq < 85:
        return "Power User"
    else:
        return "Super User"


def calc_late_fee(vol, items, red):
    base = vol*0.05 + items*2
    fee = base * red
    return round(fee, 1)


def need_renew(weeks, total, freq):
    if weeks >= 6 and freq < 50:
        return True
    elif total < 100 and freq < 60:
        return True
    elif weeks >= 4 and freq < 40:
        return True
    else:
        return False


def show_report(name, mat, items, mem, yrs, base, act, weeks):
    print("="*40)
    print("Circulation Report for:", name)
    print("-"*40)
    print("Material Type:", mat)
    print("Items Borrowed:", items)
    print("Membership Tier:", mem)

    vol = calc_borrow_vol(mat, items, mem)
    print("Borrowing Volume:", vol)

    freq = calc_usage_freq(yrs, base, act)
    print("Usage Analysis:")
    print("   Experience:", yrs, "years,", "Baseline:", base, ", Actual Checkouts:", act)
    print("   Frequency:", round(freq, 1), "%")

    cat = get_user_cat(freq)
    print("   Patron Category:", cat)

    if cat == "Occasional User":
        red = 0.5
    elif cat == "Regular User":
        red = 1.0
    elif cat == "Frequent User":
        red = 1.2
    elif cat == "Power User":
        red = 1.5
    else:
        red = 1.8

    fee = calc_late_fee(vol, items, red)
    print("Late Fees: $", fee)
    print("Borrowing Weeks:", weeks)

    renew = need_renew(weeks, items, freq)
    if renew:
        print("Renewal Reminder Needed: Yes")
    else:
        print("Renewal Reminder Needed: No")
    print()


print("LIBRARY CIRCULATION SYSTEM")
record1 = ("Ashton", "books", 45, "premium", 3, 800, 1150, 3)
record2 = ("Bailey", "media", 60, "standard", 5, 900, 1300, 5)
record3 = ("Casey", "journals", 30, "basic", 8, 850, 950, 7)

show_report(*record1)
show_report(*record2)
show_report(*record3)
