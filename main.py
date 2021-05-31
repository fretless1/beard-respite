import math

print("Mit diesem Rechner kannst du eine beliebige Bedenkzeit vor der Rasur deines Bartes berechnen.")
# Gesamtzeit = Wachstumszeit + Bedenkzeit = Wachstumszeit + (Wachstumszeit/Vorlaufzeit)

print()
# Anzahl der Tage für die Wachstumszeit
g = float(input("Gib hier die Anzahl der Tage ein, die vergangen sind seit du dich das letzte Mal rasiert hast: "))
# Vorlaufzeit bzw. Modul für die Bedenkzeit
v = float(input("Gib hier die Anzahl der Tage für die Vorlaufzeit ein, die für einen Tag Bedenkzeit nötig ist: "))


# "addtime" berechnet die Bedenkzeit c in Abhängigkeit von der Vorlaufzeit b
def addtime(a, b):
    c = a / b
    return c


# unterscheidet beim Output zwischen "Jahr" und "Jahre"
if math.floor(g / 360) == 1:
    y = " Jahr"
else:
    y = " Jahre"
# unterscheidet beim Output zwischen "Monat" und "Monate"
if math.floor(g % 360) == 30:
    m = " Monat"
else:
    m = " Monate"
# unterscheidet beim Output zwischen "Tag" und "Tage"
if v == 1 or math.floor(g % 30) == 1:
    d = " Tag"
else:
    d = " Tage"
# unterscheidet beim Output zwischen "Stunde" und "Stunden"
if math.floor((g * 24) % 24) == 1:
    h = " Stunde"
else:
    h = " Stunden"
# unterscheidet beim Output zwischen "Minute" und "Minuten"
if math.floor((((g * 24) % 24) * 60) % 60) == 1:
    mi = " Minute"
else:
    mi = " Minuten"
# unterscheidet beim Output zwischen "Sekunde" und "Sekunden"
if math.floor((((((g * 24) % 24) * 60) % 60) * 60) % 60) == 1:
    s = " Sekunde"
else:
    s = " Sekunden"

print()
print("Wachstumszeit: ")
print(math.floor(g/360), y)
print(math.floor((g % 360)/30), m)
print(math.floor((g % 360) % 30), d)
print(math.floor(((g % 360) % 30) * 24) % 24, h)
print(math.floor((((((g % 360) % 30) * 24) % 24) * 60) % 60), mi)
print(math.floor((((((((g % 360) % 30) * 24) % 24) * 60) % 60) * 60) % 60), s)

# unterscheidet beim Output zwischen "Jahr" und "Jahre"
if math.floor(addtime(g, v) / 360) == 1:
    y = " Jahr"
else:
    y = " Jahre"
# unterscheidet beim Output zwischen "Monat" und "Monate"
if math.floor(addtime(g, v) % 360) == 30:
    m = " Monat"
else:
    m = " Monate"
# unterscheidet beim Output zwischen "Tag" und "Tage"
if v == 1 or math.floor(addtime(g, v) % 30) == 1:
    d = " Tag"
else:
    d = " Tage"
# unterscheidet beim Output zwischen "Stunde" und "Stunden"
if math.floor((addtime(g, v) * 24) % 24) == 1:
    h = " Stunde"
else:
    h = " Stunden"
# unterscheidet beim Output zwischen "Minute" und "Minuten"
if math.floor((((addtime(g, v) * 24) % 24) * 60) % 60) == 1:
    mi = " Minute"
else:
    mi = " Minuten"
# unterscheidet beim Output zwischen "Sekunde" und "Sekunden"
if math.floor((((((addtime(g, v) * 24) % 24) * 60) % 60) * 60) % 60) == 1:
    s = " Sekunde"
else:
    s = " Sekunden"

print()
print("Bedenkzeit: ")
print(math.floor(addtime(g, v)/360), y)
print(math.floor((addtime(g, v) % 360)/30), m)
print(math.floor((addtime(g, v) % 360) % 30), d)
print(math.floor(((addtime(g, v) % 360) % 30) * 24) % 24, h)
print(math.floor((((((addtime(g, v) % 360) % 30) * 24) % 24) * 60) % 60), mi)
print(math.floor((((((((addtime(g, v) % 360) % 30) * 24) % 24) * 60) % 60) * 60) % 60), s)

# unterscheidet beim Output zwischen "Jahr" und "Jahre"
if math.floor(addtime(g, v) / 360) == 1:
    y = " Jahr"
else:
    y = " Jahre"
# unterscheidet beim Output zwischen "Monat" und "Monate"
if math.floor((addtime(g, v) + g) % 360) == 30:
    m = " Monat"
else:
    m = " Monate"
# unterscheidet beim Output zwischen "Tag" und "Tage"
if v == 1 or math.floor((addtime(g, v) + g) % 30) == 1:
    d = " Tag"
else:
    d = " Tage"
# unterscheidet beim Output zwischen "Stunde" und "Stunden"
if math.floor(((addtime(g, v) + g) * 24) % 24) == 1:
    h = " Stunde"
else:
    h = " Stunden"
# unterscheidet beim Output zwischen "Minute" und "Minuten"
if math.floor(((((addtime(g, v) + g) * 24) % 24) * 60) % 60) == 1:
    mi = " Minute"
else:
    mi = " Minuten"
# unterscheidet beim Output zwischen "Sekunde" und "Sekunden"
if math.floor(((((((addtime(g, v) + g) * 24) % 24) * 60) % 60) * 60) % 60) == 1:
    s = " Sekunde"
else:
    s = " Sekunden"

print()
print("Gesamtzeit: ")
print(math.floor((g + addtime(g, v))/360), y)
print(math.floor(((g + addtime(g, v)) % 360)/30), m)
print(math.floor(((g + addtime(g, v)) % 360) % 30), d)
print(math.floor((((g + addtime(g, v)) % 360) % 30) * 24) % 24, h)
print(math.floor(((((((g + addtime(g, v)) % 360) % 30) * 24) % 24) * 60) % 60), mi)
print(math.floor(((((((((g + addtime(g, v)) % 360) % 30) * 24) % 24) * 60) % 60) * 60) % 60), s)
