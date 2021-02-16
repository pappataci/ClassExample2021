def analyze_HDL(HDL):
    if (HDL > 60):
        return 'Normal'
    elif 40 <= HDL < 60:
        return 'Borderline Low'
    else:
        return 'Low'
