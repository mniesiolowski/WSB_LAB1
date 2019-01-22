auto = "0"

while auto == "0":

  

  a = int (input("Jeśli chcesz poznać podatki oraz składki ZUS dla umowy o pracę wpisz 1, jeśli dla umowy zlecenia wpisz 2: "))



  while (a==1 or a==2):



    b = float (input("Podaj kwotę brutto: "))



    if (a==1):



      print ("wynagrodzenie brutto będące podstawą wymiaru składek: ", b)

      print ("składki finansowane przez pracownika:")

      emeryt = round(b * 0.0976, 2)

      print ("emerytalna: ", emeryt)

      rent = round(b * 0.015, 2)

      print ("rentowa: ", rent)

      chorob = round(b * 0.0245, 2)

      print ("chorobowa: ", chorob)

      sumasfpp = emeryt + rent + chorob

      print ("suma składek finansowanych przez pracownika: ", sumasfpp)

      pwsz = b - sumasfpp

      print ("podstawa wymiaru składki zdrowotnej: ", pwsz)

      szdz = round(0.09*pwsz, 2)

      print ("składka zdrowotna do zapłaty: ", szdz)

      szdood = round(0.0775*pwsz, 2)

      print ("składka zdrowotna do odliczenia od podatku: ", szdood)

      kup = 111.25

      print ("koszty uzyskania przychodu: ", kup)

      poznpit = round(b - kup - sumasfpp)

      print ("podstawa obliczenia zaliczki na PIT: ", poznpit)

      znpit = round((0.18*poznpit) - 46.33 - szdood)

      print("zaliczka na PIT: ", znpit)

      netto_uop = round (b - sumasfpp - szdz - znpit, 2)

      print("Twoje wynagrodzenie NETTO na umowie o pracę wyniesie: ", netto_uop)

      break



    elif (a==2):

      if (b<=200):

        print ("podstawa wymiaru składek na ubezpieczenia społeczne: ", b)

        snus = round(0.1371*b, 2)

        print ("składki na ubezpieczenia społeczne finansowane przez zleceniobiorcę: ", snus)

        pwsnuz = round(b - snus, 2)

        print ("podstawa wymiaru składki na ubezpieczenie zdrowotne: ", pwsnuz)

        snuz = round(pwsnuz * 0.09, 2)

        print ("składka na ubezpieczenie zdrowotne: ", snuz)

        popz = round(b)

        print ("podstawa opodatkowania, po zaokrągleniu do pełnych złotych: ", popz)

        zpd = round(popz * 0.18)

        print ("zryczałtowany podatek dochodowy, po zaokrągleniu do pełnych złotych: ", zpd)

        netto_uzlt200 = round (b - (snus + snuz + zpd), 2)

        print("Twoje wynagrodzenie NETTO na umowie zlecenie wyniesie: ", netto_uzlt200)

        break



      elif (b>200):

        print ("podstawa wymiaru składek na ubezpieczenia społeczne: ", b)

        snus1 = round(0.1371*b, 2)

        print ("składki na ubezpieczenia społeczne finansowane przez zleceniobiorcę: ", snus1)

        pwsnuz1 = round(b - snus1, 2)

        print ("podstawa wymiaru składki na ubezpieczenie zdrowotne: ", pwsnuz1)

        snuz1 = round(pwsnuz1 * 0.09, 2)

        snuz2 = round(pwsnuz1 * 0.075, 2)

        print ("składka na ubezpieczenie zdrowotne 9%: ", snuz1)

        kup1 = round((b - snus1) * 0.2, 2)

        print ("koszty uzyskania przychodów: ", kup1)

        popz1 = round(b - (kup1 + snus1))

        print ("podstawa opodatkowania, po zaokrągleniu do pełnych złotych: ", popz1)

        znp = round(popz1 * 0.18, 2)

        print ("zaliczka na podatek: ", znp)

        znpdp = round(znp - snuz2)

        print ("zaliczka na podatek do przekazania do urzędu skarbowego: ", znpdp)

        netto_uzmt200 = round (b - (snus1 + snuz1 + znpdp), 2)

        print("Twoje wynagrodzenie NETTO na umowie zlecenie wyniesie: ", netto_uzmt200)

        break



  else:

    print("Wybierz opcję 1 lub 2!")