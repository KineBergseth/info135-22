class Test:
    class_variable = 0  # dette er en klasse variabel

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # dette er en instance variabel
        print(f'init {self.class_variable}')  # kan få tilgang og printe klasse variabel med self eller klassenavn
        Test.class_variable = 5  # når man skal modifisere må man bruke klassenavn

    """ dette er en spesiell metode som vil printe en representasjon av et objekt i string format istedenfor
    <__main__.Test object at 0x00000240C54EA920> type output. Man kan selv velge hvilken info man vil printe,
    så lenge den returnerer et output som er en string inne i anførselstegn. metoden kjøres når man printer ut 
    selve objektet, som lenger nede i koden print(testy) """
    def __str__(self):
        return f'class var {Test.class_variable}, class var {self.class_variable},instance var {self.instance_variable}'

    """ 
    inne i en konstruktør og instance metoder kan man bruke enten self eller klassenavnet fulgt av .variabelnavn for
    å få tilgang til variabelen for å f. eks printe den. Utenfor klassen kan man kun bruke klassenavn.variabelnavn.
    Hvis man ønsker å modifisere en klasse variabel hvor som helst, må man bruke klassenavnet etterfulgt av 
    .variabelnavn (self vil ikke fungere når man skal modifisere)
    """


testy = Test(3)
testy2 = Test(8)  # her er class_variable fra før satt til 5 fra 'testy' sin init, så de vil printe forskjellige tall
print(testy)
print(testy2)
print('printe klases variabel fra utenfor klasse: ', end='')
print(Test.class_variable)  # her må man bruke Test.variabelnavn, her fungerer ikke self når man er utenfor klassen


