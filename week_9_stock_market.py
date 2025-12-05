

def strength_level(s):
    
    if s == "HOLD":
        return 1
    elif s == "BUY":
        return 2
    elif s == "STRONG_BUY":
        return 3
    return 0

def filter_signals(signals, min_strength):
    result = []
    min_level = strength_level(min_strength)

    for line in signals:
        
        if len(line) == 0:
            continue

        parts = line.split("|")

        if len(parts) < 3:
            continue
        left = parts[0]  
        time = parts[1]  
        note = parts[2].strip()

        
        open_br = left.index("[")
        close_br = left.index("]")

        signal = left[open_br+1:close_br]
        ticker = left[close_br+2:].strip()
        if strength_level(signal) >= min_level:
            summary = signal + " (" + ticker + "): " + note
            result.append(summary)

    return result


market_data = [
    "[HOLD] AAPL | 09:30:00 | Awaiting earnings report.",
    "[BUY] TSLA | 09:35:15 | Breaking resistance levels.",
    "[HOLD] GOOGL | 10:00:00 | Market undecided.",
    "",
    "[STRONG_BUY] NVDA | 10:15:00 | AI demand surging.",
    "[STRONG_BUY] AMD | 10:20:00 | Competitor weakness.",
    "[BUY] MSFT | 11:00:45 | Cloud revenue up."
]

#test1
actionable_signals = filter_signals(market_data, "BUY")
print(actionable_signals)

#test2
urgent_signals = filter_signals(market_data, "STRONG_BUY")
print(urgent_signals)