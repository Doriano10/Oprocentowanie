# wiadomość powitalna
print("Witaj w kalkulatorze oprocentowania pożyczki")

# pobranie od użytkownika wartości początkowej kredytu
kwota_początkowa = float(input("Proszę podać początkową kwotę kredytu:\n"))

# pobranie od użytkownika wartości oprocentowania pożyczki
oprocentowanie = float(input("Proszę podać oprocentowanie pożyczki:\n"))

# pobranie od użytkownika wartości kwoty raty stałej
rata = float(input("Proszę podać wartość raty kredytu:\n"))

# zmienne zawierające wartość inflacji w następnych miesiącach
infl_1 = 1.59282448436825
infl_2 = -0.453509101198007
infl_3 = 2.32467171712441
infl_4 = 1.26125440724877
infl_5 = 1.78252628571251
infl_6 = 2.32938454145522
infl_7 = 1.50222984223283
infl_8 = 1.78252628571251
infl_9 = 2.32884899407637
infl_10 = 0.616921348207244
infl_11 = 2.35229588637833
infl_12 = 0.337779545187098
infl_13 = 1.57703524727525
infl_14 = -0.292781442607648
infl_15 = 2.48619659017508
infl_16 = 0.267110317834564
infl_17 = 1.41795267229799
infl_18 = 1.05424326726375
infl_19 = 1.4805201044812
infl_20 = 1.57703524727525
infl_21 = -0.0774206903147018
infl_22 = 1.16573339872354
infl_23 = 0.404186717638335
infl_24 = 1.49970852083123

# wzór na kwotę zadłużenia
# month = float(1 + (infl_1 + oprocentowanie) / 1200) * kwota_początkowa - rata

# wzór na wiadomość dla użytkownika
# print(f"Twoja pozostała kwota kredytu to {month} zł, to o {kwota_początkowa - month} zł")

# styczeń
print("styczeń:")
month1 = round(1 + (infl_1 + oprocentowanie) / 1200) * kwota_początkowa - rata
print(f"Twoja pozostała kwota kredytu to {month1} zł, to o {kwota_początkowa - month1} zł\n")

# luty
print("luty:")
month2 = float(1 + (infl_2 + oprocentowanie) / 1200) * month1 - rata
print(f"Twoja pozostała kwota kredytu to {month2} zł, to o {month1 - month2} zł\n")

# marzec
print("marzec:")
month3 = float(1 + (infl_3 + oprocentowanie) / 1200) * month2 - rata
print(f"Twoja pozostała kwota kredytu to {month3} zł, to o {month2 - month3} zł\n")

# kwiecień
print("kwiecień:")
month4 = float(1 + (infl_4 + oprocentowanie) / 1200) * month3 - rata
print(f"Twoja pozostała kwota kredytu to {month4} zł, to o {month3 - month4} zł\n")

# maj
print("maj:")
month5 = float(1 + (infl_5 + oprocentowanie) / 1200) * month4 - rata
print(f"Twoja pozostała kwota kredytu to {month5} zł, to o {month4 - month5} zł\n")

# czerwiec
print("czerwiec:")
month6 = float(1 + (infl_6 + oprocentowanie) / 1200) * month5 - rata
print(f"Twoja pozostała kwota kredytu to {month6} zł, to o {month5 - month6} zł\n")

# lipiec
print("lipiec:")
month7 = float(1 + (infl_7 + oprocentowanie) / 1200) * month6 - rata
print(f"Twoja pozostała kwota kredytu to {month7} zł, to o {month6 - month7} zł\n")

# sierpień
print("sierpień:")
month8 = float(1 + (infl_8 + oprocentowanie) / 1200) * month7 - rata
print(f"Twoja pozostała kwota kredytu to {month8} zł, to o {month7 - month8} zł\n")

# wrzesień
print("wrzesień:")
month9 = float(1 + (infl_9 + oprocentowanie) / 1200) * month8 - rata
print(f"Twoja pozostała kwota kredytu to {month9} zł, to o {month8 - month9} zł\n")

# październik
print("październik:")
month10 = float(1 + (infl_10 + oprocentowanie) / 1200) * month9 - rata
print(f"Twoja pozostała kwota kredytu to {month10} zł, to o {month9 - month10} zł\n")

# listopad
print("listopad:")
month11 = float(1 + (infl_11 + oprocentowanie) / 1200) * month10 - rata
print(f"Twoja pozostała kwota kredytu to {month11} zł, to o {month10 - month11} zł\n")

# grudzień
print("grudzień:")
month12 = float(1 + (infl_12 + oprocentowanie) / 1200) * month11 - rata
print(f"Twoja pozostała kwota kredytu to {month12} zł, to o {month11 - month12} zł\n")

#styczeń
print("styczeń:")
month13 = float(1 + (infl_13 + oprocentowanie) / 1200) * month12 - rata
print(f"Twoja pozostała kwota kredytu to {month13} zł, to o {month12 - month13} zł\n")

# luty
print("luty:")
month14 = float(1 + (infl_14 + oprocentowanie) / 1200) * month13 - rata
print(f"Twoja pozostała kwota kredytu to {month14} zł, to o {month13 - month14} zł\n")

# marzec
print("marzec:")
month15 = float(1 + (infl_15 + oprocentowanie) / 1200) * month14 - rata
print(f"Twoja pozostała kwota kredytu to {month15} zł, to o {month14 - month15} zł\n")

# kwiecień
print("kwiecień:")
month16 = float(1 + (infl_16 + oprocentowanie) / 1200) * month15 - rata
print(f"Twoja pozostała kwota kredytu to {month16} zł, to o {month15 - month16} zł\n")

# maj
print("maj:")
month17 = float(1 + (infl_17 + oprocentowanie) / 1200) * month16 - rata
print(f"Twoja pozostała kwota kredytu to {month17} zł, to o {month16 - month17} zł\n")

# czerwiec
print("czerwiec:")
month18 = float(1 + (infl_18 + oprocentowanie) / 1200) * month17 - rata
print(f"Twoja pozostała kwota kredytu to {month18} zł, to o {month17 - month18} zł\n")

# lipiec
print("lipiec:")
month19 = float(1 + (infl_19 + oprocentowanie) / 1200) * month18 - rata
print(f"Twoja pozostała kwota kredytu to {month19} zł, to o {month18 - month19} zł\n")

# sierpień
print("sierpień:")
month20 = float(1 + (infl_20 + oprocentowanie) / 1200) * month19 - rata
print(f"Twoja pozostała kwota kredytu to {month20} zł, to o {month19 - month20} zł\n")

# wrzesień
print("wrzesień:")
month21 = float(1 + (infl_21 + oprocentowanie) / 1200) * month20 - rata
print(f"Twoja pozostała kwota kredytu to {month21} zł, to o {month20 - month21} zł\n")

# październik
print("październik:")
month22 = float(1 + (infl_22 + oprocentowanie) / 1200) * month21 - rata
print(f"Twoja pozostała kwota kredytu to {month22} zł, to o {month21 - month22} zł\n")

# listopad
print("listopad:")
month23 = float(1 + (infl_23 + oprocentowanie) / 1200) * month22 - rata
print(f"Twoja pozostała kwota kredytu to {month23} zł, to o {month22 - month23} zł\n")

# grudzień
print("grudzień:")
month24 = float(1 + (infl_24 + oprocentowanie) / 1200) * month23 - rata
print(f"Twoja pozostała kwota kredytu to {month24} zł, to o {month23 - month24} zł\n")