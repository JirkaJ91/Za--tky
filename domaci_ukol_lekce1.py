mesta=["Praha","Brno","Liberec","Turnov","Semily"]
ceny=(180,250,100,80,90)
cara="="*35
nabidka="""1-Praha 180
2-Brno 250
3-Liberec 100
4-Turnov 80
5-Semily 90
"""
print("VÍTEJTE V JIZDENKOVCE")
print(cara)
print(nabidka)
print(cara)
print()
destinace=input("CISLO DESTINACE:")
jmeno=input("JMÉNO:")
prijmeni=input("PŘÍJMENÍ:")
email=input("EMAIL:")
telefon=input("TELEFON:")
print(cara)
print()
spravna_destinace=mesta[int(destinace) - 1]
cena=ceny[int(destinace) - 1]
print(cara)
print(f"""DEKUJI, {jmeno} ZA OBJEDNAVKU,
CIL. DESTINACE: {spravna_destinace}, CENA JIZDNEHO: {cena},
NA TVUJ MAIL {email} JSME TI POSLALI LISTEK.""")