print("Vi har en regel for en tallrekke i hodet. Gjett på tre tall i rekkefølge, så skal vi fortelle deg"
          "om de oppfyller regelen. Når du er klar kan du gjette på hva regelen er for noe.")

#Lager en string som skal bryte while lokka når brukeren er klar til å gjette.
nytt_gjett = " "

while nytt_gjett != "klar":

    #Brukeren får gjette på tre tall separert med mellomrom.
    gjett = str(input("Gjett på tre tall i rekkefølge: "))


    #Separerer tallene i stringen med komma og bruker tuple funksjonen
    # til å angi et variabelnavn direkte.
    tall1, tall2, tall3 = gjett.split()


    #Hvis tallene blir større og større får brukeren beskjed om at
    # regelen er opprettholdt. Deretter får brukeren muligheten til å legge inn et nytt gjett.
    # Brukeren kan også velge å bryte while-løkka for å gjette på regel ved å skrive exit.
    if tall1<tall2<tall3:
        print("Riktig! Sykt bra jobba! Det er sykt vanskelig å få til på første forsøk altså!"
              "Du er smart! Dette er en gyldig tallrekke. \n\n"
              "For et nytt gjett, press en tast. For å gjette på regelen skriv klar")

        nytt_gjett = input(" ")

    #Her gjelder akkurat det samme, bare at beskjeden er annerledes når de har gjettet feil tallrekke.
    else:
        print("Nei, dette er ikke en del av tallrekka! Vil du prøve et gjett til?\n\n "
              "For et nytt gjett, press en tast. For å gjette på regelen skriv klar")

        nytt_gjett = input(" ")


#Når while-lokka er brutt, får brukeren muligheten til å gjette på hva regelen er. Deretter kommer svaret opp som en stening :P
# Her er det nok litt rom for forbedring xD
final_guess = input("Skriv inn hva du tror regelen er. Deretter avsløres sva1ret.\n")

print("Hvis du gjettet på at regelen var at tallet skal stige hadde du riktig svar."
      "Hvis ikke har du nok (som alle andre) et alvorlig tilfelle av confirmation bias!")