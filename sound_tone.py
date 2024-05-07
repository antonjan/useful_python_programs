import winsound, time
print("tone")
for freq in range(50, 18000, 100):
    print("Frequency: ", freq)
    winsound.Beep(freq, 200)
