#EJERCICIO 1
def palindroma(string):
    return string == string[::-1]

def string(palabra):
    text1='afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilo'
    text2='sophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconc'
    text3='ernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspe'
    text4='akwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodaya'
    text5='hsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswas'
    text6='misunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonande'
    text7='verypureandwisespiritthatevertookfleshtobegreatistobemisunderstood'
    tupla = text1+text2+text3+text4+text5+text6+text7
    string  = tupla.partition(palabra)
    if palabra in string:
        if palindroma(palabra):
            print('{} Si se lee igual al reves'.format(palabra))
        else:
            print('{} No se lee igual al reves'.format(palabra))
    else:
        print('No es encontro la pabra {}'.format(palabra))
string('bad')