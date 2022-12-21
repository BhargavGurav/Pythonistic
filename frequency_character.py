def findFrequency(char, string):
    freq = 0
    for ch in string:
        if ch == char:
            freq += 1
    return freq


phrase = "Hello and Welcome all dear my freinds to this program"
print(f"The frequency of 'e' in phrase is {findFrequency('e', phrase)}")
