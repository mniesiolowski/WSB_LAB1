auto = "t"

while auto == "t":

 

  waga = float (input("Podaj swoją wagę w kilogramach: "))

  wzrost = float (input("Podaj swój wzrost w metrach: "))



  bmi=round((waga/(wzrost**2)), 2)



  if (bmi<18.5):

    print("Twoje BMI wynosi: ", bmi)

    print("Niedowaga")

    print("Ryzyko chorób towarzyszących otyłości: Niskie ")



  elif (bmi>=18.5 and bmi <=24.9):

    print("Twoje BMI wynosi: ", bmi)

    print(" Norma")

    print("Ryzyko chorób towarzyszących otyłości: Średnie")



  elif (bmi>=25 and bmi <=29.9):

    print("Twoje BMI wynosi: ", bmi)

    print(" Nadwaga")

    print("Ryzyko chorób towarzyszących otyłości: Podwyższone")    



  elif (bmi>=30 and bmi <=34.9):

    print("Twoje BMI wynosi: ", bmi)

    print("I Nadwaga")

    print("Ryzyko chorób towarzyszących otyłości: Umiarkowanie podwyższone")    



  elif (bmi>=35 and bmi <=39.9):

    print("Twoje BMI wynosi: ", bmi)

    print("II Nadwaga")

    print("Ryzyko chorób towarzyszących otyłości: Wysokie")



  elif (bmi>=40):

    print("Twoje BMI wynosi: ", bmi)

    print("III Nadwaga")

    print("Ryzyko chorób towarzyszących otyłości: Bardzo wysokie") 