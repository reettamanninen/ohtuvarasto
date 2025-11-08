from varasto import Varasto

def luo_varastot():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    return mehua, olutta

def tulosta_varasto(varasto, nimi):
    print(f"{nimi}: {varasto}")

def tulosta_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def muokkaa_mehua(mehua):
    toiminnat = [("Lisätään", 50.7), ("Otetaan", 3.14)]
    for teksti, maara in toiminnat:
        print(f"{teksti} {maara}")
        if teksti == "Lisätään":
            mehua.lisaa_varastoon(maara)
        else:
            mehua.ota_varastosta(maara)
        tulosta_varasto(mehua, "Mehuvarasto")

def testaa_virhetilanteet(mehua, olutta):
    virheet = [
        ("Varasto(-100.0)", Varasto(-100.0)),
        ("Varasto(100.0, -50.7)", Varasto(100.0, -50.7))
    ]
    for teksti, varasto in virheet:
        print(teksti)
        print(varasto)

    ylimaaraiset = [
        ("Olut varastoon liikaa",
         olutta.lisaa_varastoon, 1000.0, olutta, "Olutvarasto"),
        ("Mehu varastoon negatiivinen",
         mehua.lisaa_varastoon, -666.0, mehua, "Mehuvarasto")
    ]
    for teksti, funktio, maara, varasto, nimi in ylimaaraiset:
        print(teksti)
        funktio(maara)
        tulosta_varasto(varasto, nimi)

    otot = [
        ("Olutta otetaan liikaa",
         olutta.ota_varastosta, 1000.0, olutta, "Olutvarasto"),
        ("Mehua otetaan negatiivinen",
         mehua.ota_varastosta, -32.9, mehua, "Mehuvarasto")
    ]
    for teksti, funktio, maara, varasto, nimi in otot:
        print(teksti)
        saatiin = funktio(maara)
        print(f"saatiin {saatiin}")
        tulosta_varasto(varasto, nimi)

def main():
    mehua, olutta = luo_varastot()
    tulosta_varasto(mehua, "Mehuvarasto")
    tulosta_varasto(olutta, "Olutvarasto")
    tulosta_getterit(olutta)
    muokkaa_mehua(mehua)
    testaa_virhetilanteet(mehua, olutta)

if __name__ == "__main__":
    main()
