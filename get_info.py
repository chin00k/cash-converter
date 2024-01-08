

def get_info(text_detected):
    
    text_detected = text_detected.lower()
    
    origin = ""
    
    mcad = ["cana", "nada", "premier", "premi", "emier", 
            "john a", "macdo", "onald", "a macd", "cinq ", "anad", "laurier"
            "wilfrid"]
    
    mgbp = ["eng", "nglan", "gland", "pound", "of sco", "poun", "ound", 
            "ief cas", "nor and comp"]
    
    musd = ["ral rese", "united states", "ted sta", "states", "america"
            "ameri", "erica", "washington", "washin", "hingto", "lic and pri"
            "for all debts"]
    
    meur = ["euro", "uro ", " eur", "bce ecb", "ecb ezb", "ezb ekt", "ekt ekp"
            , "eur0", "ekp ekt", "ekt esb", "esb ekb", "ekb bce", "bce ebc",
            "£200 "]
    
    minr = ["india", " ind", "ndia", "dia ", "rupee", "upee", "pees", 
            "gandi", "mahatma", "tma gan", "ahatm"]
    
    msgp = ["singa", "sigap", "apore", "ngapu", "apura", "gapore"]
    
    maud = ["australia", "commonwealth", "asutr", "trali", "ralia", "strali"
            "lth of aus", "ank of aus", " aus", "ommonw", "monwea"]
    
    mnzd = ["new zealand", "zealand", " zeal", "aland ", "new zea", "te putea"
            , "matua", "tea matu", "te pute", "aotea", "tearoa"]
    #nzd 50, 100 do not work well
    
    
    mchf = ["schweizerische", "svizra", "franc", "suisse", "franken", 
            "anken", "schwe", "franchi", "anchi ", "frank", " fran", "naziun"]
    #chf 1000 fails
    
    mhkd = ["ghai", "hong", "kong", "hsbc", " hsb", "sbc ", "standard",
            "chartered", "china", "standa", "adard", "nk of ch", " shanghai"
            "hangh", "nghai", "ard char", "hai bank"]
    #10 hkd fails
    
    msek = ["sveriges", "riksbank", "tjugo", " sver", "sverig", "riges", 
            "riksb", " tjug", "hundra  kro"]
    #sek is not great
    
    
    mmxn = ["banco", "mexico", "méxico", "méxic", "éxico", "xico ", "peso"
            , "esos ", " mex", " méx", "co de me", "co de mé"]
    
    mnok = ["norges", "femti", "ges ban", "mti kro", "es bank"]
   
    

    value = ""
    
    val2000 = ["two thou", "two th"]
    
    val1000 = ["thousa", "usand", "mille", "tusen", "usen k", "ett tus"
               "mil pes", " 1000 ", "milli", "tause", " taus"]
    
    val500 = ["five Hundred", "quin", "fem hund", "five hundr", "ive hun", 
              " 500 "]
    
    val200 = ["two hundred", "two hun", "oscie", "doscien", "doscie", 
              "tva hun", "to hundr", " 200 ", "duatschi", "atschient", 
              "zweihund", "weihun", "£200 "]
    
    val100 = ["one hun", "ne hundr", "franklin", "anklin", " frankl"  " cent ",
              "cien", "ett hun", "tt hund", "ndre kron", "ien pes", "cien p"
              "cento", "cent "]
    
    val50 = ["fifty", "ifty ", "cuante", " fift", "grant", " gran"
             , "femti", "emtio", "tio kro", "cincuenta", " cincue", 
             "enta peso", "fty pou", "funzfig", "nzfig", "tschuncanta"
             , "canta fr", "cinquanta", "inquan", "cinquante", "cinqua",
              "uante ", "ante fr", "cinquan", "fty dol", "nty hon"]
    
    val20 = ["twenty", "vingt", "wenty ", " twent", "jackson", " jacks", 
             "ckson ", "ingt ", " ving", "tjugo", "jugo ", " tjug", "viente"
             , "iente ", "vient ", "nty pou", "nty dol", "zwanzig", "anzig "
             , " zwanzi", "entg fran"]
    
    val10 = [" ten ", " dix ", "hamilton", " hamilt", "ilton ", "ten dol",
             "ten rup", "ten hon", "ten pou", "dieci", " diec", "ieci "
             , "zehn"]
    
    val5 = [" five ", " cinq ", "five ", " five", " cinq", "cinq ", "lincoln"
            "linco", "ncoln", "incol", "ive dol", "ive pou"]
    
    val2 = [" two ", " two", "two ", "two dol"]
    
    val1 = [" one ", " un ", " one", "one ", "one dol", "one pou", 
            " washington "]
    
    EM = 0
    
    if any(x in text_detected for x in mcad):
        origin = "CAD"
    elif any(x in text_detected for x in mgbp):
            origin = "GBP"
    elif any(x in text_detected for x in musd):
            origin = "USD"
    elif any(x in text_detected for x in meur):
            origin = "EUR"
    elif any(x in text_detected for x in minr):
            origin = "INR"    
    elif any(x in text_detected for x in msgp):
            origin = "SGP"
    elif any(x in text_detected for x in maud):
            origin = "AUD"
    elif any(x in text_detected for x in mnzd):
            origin = "NZD"   
    elif any(x in text_detected for x in mchf):
            origin = "CHF"
    elif any(x in text_detected for x in mhkd):
            origin = "HKD"
    elif any(x in text_detected for x in msek):
            origin = "SEK"
    elif any(x in text_detected for x in mmxn):
            origin = "MXN"
    elif any(x in text_detected for x in mnok):
            origin = "NOK"
    else:
        EM = 1
    
    if any(x in text_detected for x in val1000):
        value = 1000
    elif any(x in text_detected for x in val500):
            value = 500
    elif any(x in text_detected for x in val200):
            value = 200
    elif any(x in text_detected for x in val100):
            value = 100
    elif any(x in text_detected for x in val50):
            value = 50
    elif any(x in text_detected for x in val20):
            value = 20
    elif any(x in text_detected for x in val10):
            value = 10
    elif any(x in text_detected for x in val5):
            value = 5
    elif any(x in text_detected for x in val2):
            value = 2
    elif any(x in text_detected for x in val1):
            value = 1
    elif any(x in text_detected for x in val2000):
            value = 2000


    
    return(origin, value, EM)