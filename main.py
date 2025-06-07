import pyjokes
from random import sample
from pyweb import pydom

def get_smthing(event):
    pydom["div#jokes"].html = f"{pyjokes.get_joke()} 🥁"

def get_rally(event):
    pydom["div#rally"].html = "Rally data will be fetched here."

#uusi versio:
def get_pool(luokat: tuple):
    #luokat numero vastaa rally_kyltit_kopio.txt tiedoston jokaisen rivin alussa olevia numeroita
    pool = []
    
    try:
        for luokka in range(luokat):
            if luokka == 0:
                pool.extend(range(2, 4))  # 2-3
            elif luokka == 1:
                pool.extend(range(4, 40))  # 4-39
            elif luokka == 2:
                pool.extend(range(40, 65))  # 40-64
            elif luokka == 3:
                pool.extend(range(65, 91))  # 65-90
            elif luokka == 4:
                pool.extend(range(91, 113))  # 91-112
    except:
        for luokka in luokat:
            if luokka == 0:
                pool.extend(range(2, 4))  # 2-3
            elif luokka == 1:
                pool.extend(range(4, 40))  # 4-39
            elif luokka == 2:
                pool.extend(range(40, 65))  # 40-64
            elif luokka == 3:
                pool.extend(range(65, 91))  # 65-90
            elif luokka == 4:
                pool.extend(range(91, 113))  # 91-112
    else:
        print("erroria pukkaa")
    return pool

"""
    """
def choose_exe(event): #tulostaa tuloksen (nro, nimi)
    luokat = (4, 0) #toimii jos tuple!
    lkm= 3
    pool= get_pool(luokat)
    all_exes = [
        [1, 'Tehtävän numero', 'Nimi', 'Suorituspaikka', 'Suoritusohje'
],[2, 'LÄHTÖ', 'LÄHTÖ', ' (A)', 'Koira seuraa ohjaajaa lähtökyltille. Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koirakko lähtee suorittamaan rataa.'
],[3, 'MAALI', 'MAALI', ' (A)', 'Tarvittaessa koirakko siirtyy normaalikäyntiin. Rata päättyy, kun koirakko ohittaa kyltin. Koirakko poistuu kilpailukehästä normaalikäyntiä.'
],[4, '101', 'MAAHAN', ' (A)', 'Ohjaajan pysähtyessä koira menee maahan ohjaajan viereen. Koira pysyy maassa, kunnes koirakko lähtee liikkeelle.'
],[5, '102', 'ISTU, MAAHAN', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira menee maahan. Koira pysyy maassa, kunnes koirakko lähtee liikkeelle.'
],[6, '103', 'ISTU, KIERRÄ KOIRA', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira jää istumaan ja ohjaaja kiertää koiran ympäri etukautta, palaa koiran viereen ja pysähtyy.'
],[7, '104', 'ISTU, MAAHAN, KIERRÄ KOIRA', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen, josta menee maahan. Koira jää maahan ja ohjaaja kiertää koiran ympäri etukautta, palaa koiran viereen ja pysähtyy. Koira pysyy maassa, kunnes koirakko lähtee liikkeelle.'
],[8, '105', 'TÄYSKÄÄNNÖS OIKEAAN', ' (B)', 'Koirakko tekee yhdessä tiiviin täyskäännöksen oikeaan.'
],[9, '106', 'TÄYSKÄÄNNÖS VASEMPAAN', ' (B)', 'Koirakko tekee yhdessä tiiviin täyskäännöksen vasempaan.'
],[10, '107', 'SILMUKKA OIKEAAN', ' (B)', 'Koirakko tekee yhdessä tiiviin käännöksen oikeaan ylittäen saapumislinjansa. Käännöksen kulman pitää olla 180° ja 270° välillä.'
],[11, '108', 'SILMUKKA VASEMPAAN', ' (B)', 'Koirakko tekee yhdessä tiiviin käännöksen vasempaan ylittäen saapumislinjansa. Käännöksen kulman pitää olla 180° ja 270° välillä.'
],[12, '109', '270° OIKEAAN', ' (B)', 'Koirakko tekee yhdessä tiiviin 270° käännöksen oikeaan.'
],[13, '110', '270° VASEMPAAN', ' (B)', 'Koirakko tekee yhdessä tiiviin 270° käännöksen vasempaan.'
],[14, '111', '360° OIKEAAN', ' (A)', 'Koirakko tekee yhdessä tiiviin 360° käännöksen oikeaan. Koirakko säilyttää alkuperäisen kulkusuuntansa.'
],[15, '112', '360° VASEMPAAN', ' (A)', 'Koirakko tekee yhdessä tiiviin 360° käännöksen vasempaan. Koirakko säilyttää alkuperäisen kulkusuuntansa.'
],[16, '113', 'TÄYSKÄÄNNÖS, KOIRA TAKAA', ' (B)', 'Ohjaaja tekee täyskäännöksen koiraa kohti koiran kiertäessä ohjaajan takaa.'
],[17, '114', 'ISTU, KÄÄNNÖS OIKEAAN, ISTU', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koirakko tekee yhdessä käännöksen oikeaan, pysähtyy ja koira istuu.'
],[18, '115', 'ISTU, KÄÄNNÖS VASEMPAAN, ISTU', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koirakko tekee yhdessä käännöksen vasempaan, pysähtyy ja koira istuu.'
],[19, '116', 'HIDASTA KÄYNTIÄ', ' (A)', 'Koirakko hidastaa kulkutahtiaan huomattavasti. Hitaan tahdin tulee säilyä, kunnes koirakko saapuu toiselle tahdinmuutos- tai maalikyltille.'
],[20, '117', 'JUOSTEN', ' (A)', 'Koirakko lisää kulkutahtiaan huomattavasti. Nopean tahdin tulee säilyä, kunnes koirakko saapuu toiselle tahdinmuutos- tai maalikyltille.'
],[21, '118', 'NORMAALIKÄYNTIÄ', ' (A)', 'Koirakko palaa normaaliin kulkutahtiin.'
],[22, '119', 'SPIRAALI OIKEAAN', ' (B)', 'Kolme kartiota on asetettu suoraan linjaan 1,5–2,5 metrin etäisyydelle toisistaan. Koirakko kiertää vasemmalta puolelta ensin kolme kartiota, sitten lähimmät kaksi ja viimeisenä lähimmän kartion.'
],[23, '120', 'SPIRAALI VASEMPAAN', ' (B)', 'Kolme kartiota on asetettu suoraan linjaan 1,5–2,5 metrin etäisyydelle toisistaan. Koirakko kiertää oikealta puolelta ensin kolme kartiota, sitten lähimmät kaksi ja viimeisenä lähimmän kartion.'
],[24, '121', 'PUJOTTELU', ' (B)', 'Neljä kartiota on asetettu suoraan linjaan 1,5–2,5 metrin etäisyydelle toisistaan. Koirakko pujottelee kartioiden välistä aloittaen suorituksen siten, että ensimmäinen kartio jää koirakon vasemmalle puolelle.'
],[25, '122', 'PUJOTTELU EDESTAKAISIN', ' (B)', 'Neljä kartiota on asetettu suoraan linjaan 1,5–2,5 metrin etäisyydelle toisistaan. Koirakko pujottelee edestakaisin kartioiden välistä aloittaen suorituksen siten, että ensimmäinen kartio jää koirakon vasemmalle puolelle.'
],[26, '123', 'KÄÄNNÖS OIKEAAN', ' (B)', 'Koirakko tekee yhdessä tiiviin käännöksen oikeaan.'
],[27, '124', 'KÄÄNNÖS VASEMPAAN', ' (B)', 'Koirakko tekee yhdessä tiiviin käännöksen vasempaan.'
],[28, '125', 'SEISO', ' (A)', 'Ohjaajan pysähtyessä koira pysähtyy seisomaan ohjaajan viereen. Koira pysyy seisomassa, kunnes koirakko lähtee liikkeelle.'
],[29, '126', 'ISTU, 1 ASKEL, ISTU, 2 ASKELTA, ISTU, 3 ASKELTA, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Ohjaaja ottaa yhden askeleen eteenpäin ja pysähtyy, sitten kaksi askelta ja pysähtyy, lopuksi kolme askelta ja pysähtyy. Ohjaajan liikkuessa eteenpäin koira seuraa mukana ja ohjaajan pysähtyessä istuu ohjaajan viereen.'
],[30, '127', 'ETEEN ISTU, 1 ASKEL TAAKSE, ISTU, 2 ASKELTA TAAKSE, ISTU, 3 ASKELTA TAAKSE, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan eteen. Ohjaaja peruuttaa yhden askeleen ja pysähtyy, sitten kaksi askelta ja pysähtyy, lopuksi kolme askelta ja pysähtyy. Ohjaajan peruuttaessa koira liikkuu mukana ohjaajan edessä ja ohjaajan pysähtyessä koira istuu ohjaajan eteen. Koira siirtyy ohjaajan vasemmalle puolelle. Seuraaminen jatkuu vasemmalla.'
],[31, '128', 'ISTU, 1 ASKEL, SEISO', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Ohjaaja ottaa yhden askeleen eteenpäin ja pysähtyy. Koira seuraa mukana ja ohjaajan pysähtyessä pysähtyy seisomaan ohjaajan viereen. Koira pysyy seisomassa, kunnes koirakko lähtee liikkeelle.'
],[32, '129', 'ISTU, 1 ASKEL, MAAHAN', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Ohjaaja ottaa yhden askeleen eteenpäin ja pysähtyy. Koira seuraa mukana ja ohjaajan pysähtyessä koira menee maahan ohjaajan viereen. Koira pysyy maassa, kunnes koirakko lähtee liikkeelle.'
],[33, '130', 'ETEEN ISTU, OIKEALTA VASEMMALLE', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan eteen. Koira siirtyy ohjaajan takaa vasemmalle puolelle. Seuraaminen jatkuu vasemmalla.'
],[34, '131', 'ETEEN ISTU, VASEMMALTA VASEMMALLE', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan eteen. Koira siirtyy suoraan ohjaajan vasemmalle puolelle. Seuraaminen jatkuu vasemmalla.'
],[35, '132', 'ETEEN ISTU, OIKEALTA VASEMMALLE, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan eteen. Koira siirtyy ohjaajan takaa vasemmalle puolelle istumaan. Seuraaminen jatkuu vasemmalla.'
],[36, '133', 'ETEEN ISTU, VASEMMALTA VASEMMALLE, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan eteen. Koira siirtyy suoraan ohjaajan vasemmalle puolelle istumaan. Seuraaminen jatkuu vasemmalla.'
],[37, '134', 'VIISTO ASKEL OIKEALLE', ' (B)', 'Koirakon liikkuessa ohjaaja ottaa yhden askeleen 45° etuviistoon oikeaan koiran seuratessa samassa linjassa ja rintamasuunnassa ohjaajan kanssa. Koirakko jatkaa eteenpäin kyltin oikealta puolelta.'
],[38, '135', 'KAHDEKSIKKO', ' (B)', 'Kaksi kartiota on asetettu 2,5–3 metrin etäisyydelle toisistaan. Koirakko kiertää kahdeksikon kartioiden ympäri tuomarin määräämällä tavalla ylittäen kartioiden välisen linjan kolme kertaa.'
],[39, '136', 'OHJAAJAN YMPÄRI', ' (A)', 'Ohjaajan pysähtyessä koira kiertää pysähtymättä ohjaajan ympäri etukautta ohjaajan seistessä paikallaan.'
],[40, '201', '2 x TÄYSKÄÄNNÖS, KOIRA TAKAA', ' (A)', 'Ohjaaja tekee täyskäännöksen koiraa kohti koiran kiertäessä ohjaajan takaa, etenee 1–2 metriä ja tekee uuden täyskäännöksen koiraa kohti koiran kiertäessä ohjaajan takaa. Koirakko jatkaa alkuperäiseen kulkusuuntaansa.'
],[41, '202', '2 x TÄYSKÄÄNNÖS, OIKEAAN JA VASEMPAAN', ' (A)', 'Koirakko tekee yhdessä tiiviin täyskäännöksen oikeaan, etenee 1–2 metriä ja tekee tiiviin täyskäännöksen vasempaan. Koirakko jatkaa alkuperäiseen kulkusuuntaansa.'
],[42, '203', '2 x TÄYSKÄÄNNÖS, VASEMPAAN JA OIKEAAN', ' (A)', 'Koirakko tekee yhdessä tiiviin täyskäännöksen vasempaan, etenee 1–2 metriä ja tekee tiiviin täyskäännöksen oikeaan. Koirakko jatkaa alkuperäiseen kulkusuuntaansa.'
],[43, '204', 'ISTU, MAAHAN, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira menee maahan, josta nousee istumaan.'
],[44, '205', 'ISTU, SEISO', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira nousee seisomaan. Koira pysyy seisomassa, kunnes koirakko lähtee liikkeelle.'
],[45, '206', 'ISTU, SEISO, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira nousee seisomaan, josta menee istumaan.'
],[46, '207', 'ISTU, SEISO, MAAHAN', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira nousee seisomaan, josta menee maahan. Koira pysyy maassa, kunnes koirakko lähtee liikkeelle.'
],[47, '208', 'ISTU, SEISO, KIERRÄ KOIRA', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira nousee seisomaan ja ohjaaja kiertää koiran ympäri etukautta, palaa koiran viereen ja pysähtyy. Koira pysyy seisomassa, kunnes koirakko lähtee liikkeelle.'
],[48, '209', 'ISTU, ETEEN ISTU, OIKEALTA VASEMMALLE, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira siirtyy ohjaajan eteen istumaan ja siitä ohjaajan takaa vasemmalle puolelle istumaan. Seuraaminen jatkuu vasemmalla.'
],[49, '210', 'ISTU, ETEEN ISTU, VASEMMALTA VASEMMALLE, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira siirtyy ohjaajan eteen istumaan ja siitä suoraan ohjaajan vasemmalle puolelle istumaan. Seuraaminen jatkuu vasemmalla.'
],[50, '211', 'ISTU, 1 ASKEL, KÄÄNNÖS OIKEAAN, 1 ASKEL, KUTSU, ISTU', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira pysyy istumassa, kun ohjaaja ottaa yhden askeleen eteenpäin. Ohjaaja pysähtyy ja kääntyy oikealle, ottaa yhden askeleen ja pysähtyy. Lopuksi koira kutsutaan ohjaajan viereen istumaan. Seuraamispuoli ei vaihdu.'
],[51, '212', 'ISTU, 1 ASKEL, KÄÄNNÖS VASEMPAAN, 1 ASKEL, KUTSU, ISTU', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira pysyy istumassa, kun ohjaaja ottaa yhden askeleen eteenpäin. Ohjaaja pysähtyy ja kääntyy vasemmalle, ottaa yhden askeleen ja pysähtyy. Lopuksi koira kutsutaan ohjaajan viereen istumaan. Seuraamispuoli ei vaihdu.'
],[52, '213', 'ISTU, TÄYSKÄÄNNÖS OIKEAAN', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koirakko tekee yhdessä tiiviin täyskäännöksen oikeaan.'
],[53, '214', 'ISTU, TÄYSKÄÄNNÖS VASEMPAAN', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koirakko tekee yhdessä tiiviin täyskäännöksen vasempaan.'
],[54, '215', 'ISTU, TÄYSKÄÄNNÖS OIKEAAN, ISTU', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koirakko tekee yhdessä tiiviin täyskäännöksen oikeaan, pysähtyy ja koira istuu.'
],[55, '216', 'ISTU, TÄYSKÄÄNNÖS VASEMPAAN, ISTU', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koirakko tekee yhdessä tiiviin täyskäännöksen vasempaan, pysähtyy ja koira istuu.'
],[56, '217', 'ISTU, KÄÄNNÖS OIKEAAN, 1 ASKEL, ISTU', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Ohjaaja kääntyy oikeaan, ottaa yhden askeleen ja pysähtyy. Koira seuraa mukana ja istuu ohjaajan pysähtyessä.'
],[57, '218', 'ISTU, KÄÄNNÖS VASEMPAAN, 1 ASKEL, ISTU', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Ohjaaja kääntyy vasempaan, ottaa yhden askeleen ja pysähtyy. Koira seuraa mukana ja istuu ohjaajan pysähtyessä.'
],[58, '219', 'ISTU, 1 ASKEL, SEISO, 2 ASKELTA, ISTU, 3 ASKELTA, MAAHAN', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Ohjaaja ottaa yhden askeleen eteenpäin ja pysähtyy. Koira seuraa ja jää seisomaan ohjaajan pysähtyessä. Ohjaaja ottaa kaksi askelta ja pysähtyy. Koira seuraa ja istuu ohjaajan pysähtyessä. Ohjaaja ottaa kolme askelta ja pysähtyy. Koira seuraa ja menee maahan ohjaajan pysähtyessä. Koira pysyy maassa, kunnes koirakko lähtee liikkeelle.'
],[59, '220', 'PYÖRÄHDYS', ' (A)', 'Koirakon liikkuessa koira tekee pyörähdyksen eteenpäin, ohjaajasta poispäin.'
],[60, '221', 'HOUKUTUS', ' (B)', 'Kaksi kartiota on asetettu 2,5–3 metrin päähän toisistaan. Kahden houkutuksen etäisyys toisistaan on 1,5–2 metriä. Kartiot ja houkutukset muodostavat vinoneliön. Koirakko kiertää kahdeksikon kartioiden ympäri tuomarin määräämällä tavalla ylittäen houkutusten välisen linjan kolme kertaa.'
],[61, '222', 'LÄHETYS ESTEEN YLI', ' (D)', 'Koira lähetetään hyppyesteen yli aikaisintaan kyltillä. Ohjaaja jatkaa matkaa esteen ohi.'
],[62, '223', 'KÄÄNNÖS VASEMPAAN, OHJAAJAN YMPÄRI', ' (B)', 'Ohjaaja tekee käännöksen vasempaan koiran kiertäessä pysähtymättä ohjaajan ympäri myötäpäivään.'
],[63, '224', 'SEISO, 1 ASKEL TAAKSE, SEISO', ' (A)', 'Ohjaajan pysähtyessä koira pysähtyy seisomaan ohjaajan viereen. Ohjaaja ottaa yhden askeleen taaksepäin koiran peruuttaessa samassa linjassa ja rintamasuunnassa ohjaajan kanssa. Ohjaajan pysähtyessä koira jää seisomaan ohjaajan viereen. Koira pysyy seisomassa, kunnes koirakko jatkaa eteenpäin.'
],[64, '225', 'VIISTO ASKEL VASEMPAAN', ' (B)', 'Koirakon liikkuessa ohjaaja ottaa yhden askeleen 45° etuviistoon vasempaan ja koira seuraa samassa linjassa ja rintamasuunnassa ohjaajan kanssa. Koirakko jatkaa kyltin vasemmalta puolelta.'
],[65, '301', 'SIVUASKEL OIKEAAN', ' (B)', 'Koirakon liikkuessa ohjaaja ottaa yhden askeleen oikeaan koiran seuratessa samassa linjassa ja rintamasuunnassa ohjaajan kanssa. Koirakko jatkaa kyltin oikealta puolelta.'
],[66, '302', 'SIVUASKEL VASEMPAAN', ' (B)', 'Koirakon liikkuessa ohjaaja ottaa yhden askeleen vasempaan koiran seuratessa samassa linjassa ja rintamasuunnassa ohjaajan kanssa. Koirakko jatkaa kyltin vasemmalta puolelta.'
],[67, '303', 'ISTU, SIVUASKEL OIKEAAN, ISTU', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Ohjaaja ottaa yhden askeleen oikeaan koiran seuratessa samassa linjassa ja rintamasuunnassa ohjaajan kanssa. Ohjaajan pysähtyessä koira istuu. Koirakko jatkaa kyltin oikealta puolelta.'
],[68, '304', 'ISTU, SIVUASKEL VASEMPAAN, ISTU', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Ohjaaja ottaa yhden askeleen vasempaan koiran seuratessa samassa linjassa ja rintamasuunnassa ohjaajan kanssa. Ohjaajan pysähtyessä koira istuu. Koirakko jatkaa kyltin vasemmalta puolelta.'
],[69, '305', 'ISTU, 1 ASKEL TAAKSE, ISTU, 2 ASKELTA TAAKSE, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Ohjaaja ottaa yhden askelen taaksepäin ja pysähtyy, sitten kaksi askelta ja pysähtyy. Ohjaajan peruuttaessa koira peruuttaa samassa linjassa ja rintamasuunnassa ohjaajan kanssa. Ohjaajan pysähtyessä koira istuu ohjaajan viereen.'
],[70, '306', 'ETEEN ISTU, 1 ASKEL TAAKSE, SEISO, 2 ASKELTA TAAKSE, ISTU, 3 ASKELTA TAAKSE, MAAHAN, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan eteen. Ohjaajan peruuttaessa koira liikkuu mukana ohjaajan edessä ja ohjaajan pysähtyessä koira ottaa määrätyn asennon. Ohjaajan peruutettua yhden askeleen koira seisoo, ohjaajan peruutettua kaksi askelta koira istuu ja ohjaajan peruutettua kolme askelta koira menee maahan. Koira siirtyy ohjaajan vasemmalle puolelle istumaan. Seuraaminen jatkuu vasemmalla.'
],[71, '307', 'SEISO, TÄYSKÄÄNNÖS OIKEAAN, SEISO', ' (B)', 'Ohjaajan pysähtyessä koira pysähtyy seisomaan ohjaajan viereen. Koirakko tekee yhdessä tiiviin täyskäännöksen oikealle ja pysähtyy, koira jää seisomaan. Koira pysyy seisomassa, kunnes koirakko lähtee liikkeelle.'
],[72, '308', 'SEISO, TÄYSKÄÄNNÖS VASEMPAAN, SEISO', ' (B)', 'Ohjaajan pysähtyessä koira pysähtyy seisomaan ohjaajan viereen. Koirakko tekee yhdessä tiiviin täyskäännöksen vasemmalle ja pysähtyy, koira jää seisomaan. Koira pysyy seisomassa, kunnes koirakko lähtee liikkeelle.'
],[73, '309', 'SEISO, OHJAAJAN YMPÄRI, SEISO', ' (A)', 'Ohjaajan pysähtyessä koira pysähtyy seisomaan ohjaajan viereen. Koira kiertää ohjaajan ympäri etukautta ja palaa alkuperäiselle paikalleen ohjaajan viereen seisomaan. Koira pysyy seisomassa, kunnes koirakko lähtee liikkeelle.'
],[74, '310', 'TÄYSKÄÄNNÖS VASTAKKAIN', ' (B)', 'Koirakon liikkuessa molemmat tekevät tiiviin, samanaikaisen täyskäännöksen toisiaan kohti. Seuraamispuoli vaihtuu.'
],[75, '311', 'PUOLENVAIHTO TAKAA', ' (A)', 'Koirakon liikkuessa koira tekee puolenvaihdon ohjaajan takaa. Koira ei saa pyörähtää puolenvaihdossa. Seuraamispuoli vaihtuu.'
],[76, '312', 'PUOLENVAIHTO JALKOJEN VÄLISTÄ', ' (A)', 'Koirakon liikkuessa koira tekee puolenvaihdon ohjaajan jalkojen välistä. Ohjaaja saa pysähtyä ja nostaa jalkaansa tehdäkseen puolenvaihdosta sujuvan. Seuraamispuoli vaihtuu.'
],[77, '313', 'MOLEMMAT TÄYSKÄÄNNÖS OIKEAAN', ' (B)', 'Koirakon liikkuessa molemmat tekevät tiiviin, samanaikaisen täyskäännöksen oikeaan. Seuraamispuoli vaihtuu.'
],[78, '314', 'MOLEMMAT TÄYSKÄÄNNÖS VASEMPAAN', ' (B)', 'Koirakon liikkuessa molemmat tekevät tiiviin, samanaikaisen täyskäännöksen vasempaan. Seuraamispuoli vaihtuu.'
],[79, '315', 'ISTU, PUOLENVAIHTO TAKAA, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira vaihtaa puolta ohjaajan takaa ja istuu. Koira ei saa pyörähtää puolta vaihtaessaan. Seuraamispuoli vaihtuu.'
],[80, '316', 'ISTU, PUOLENVAIHTO EDESTÄ, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira vaihtaa puolta ohjaajan edestä ja istuu. Koiran pitää pyörähtää puolta vaihtaessaan. Seuraamispuoli vaihtuu.'
],[81, '317', 'LIIKKEESTÄ SEISO, KIERRÄ KOIRA', ' (A)', 'Koirakon liikkuessa koira pysähtyy seisomaan ja ohjaaja pysähtymättä kiertää koiran ympäri etukautta, palaa koiran viereen ja pysähtyy. Koira pysyy seisomassa, kunnes koirakko lähtee liikkeelle.'
],[82, '318', 'LIIKKEESTÄ MAAHAN, KIERRÄ KOIRA', ' (A)', 'Koirakon liikkuessa koira menee maahan ja ohjaaja pysähtymättä kiertää koiran ympäri etukautta, palaa koiran viereen ja pysähtyy. Koira pysyy maassa, kunnes koirakko lähtee liikkeelle.'
],[83, '319', 'ISTU, SEISO, JÄTÄ KOIRA', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koira nousee seisomaan. Ohjaaja kävelee ilman koiraa joko kutsukyltille tai kutsukartion ohi (C) ja kutsuu koiran seuraamaan. Koira pysyy seisomassa, kunnes ohjaaja kutsuu koiraa. Kartiota käytettäessä luoksetulo on osa tätä tehtävää. Seuraamispuoli ei vaihdu.'
],[84, '320', 'LÄHETYS KAHDEN ESTEEN YLI', ' (D)', 'Kaksi estettä on sijoitettu suoraan linjaan tai enintään 90° kulmaan neljän metrin etäisyydelle toisistaan. Koira lähetetään kahden hyppyesteen yli aikaisintaan kyltillä. Ohjaaja jatkaa matkaa esteen ohi.'
],[85, '321', 'TÄYSKÄÄNNÖS, KUTSU', ' (B)', 'Tätä kylttiä voi käyttää vain kylttien 319, 408 ja 409 jälkeen. Kyltti on sijoitettu 3–5 metrin päähän edellisestä kyltistä. Ohjaaja tekee täyskäännöksen, pysähtyy ja kutsuu koiraa. Ohjaaja saa pysähtyä ennen täyskäännöstä. Koira tulee joko takaa tai suoraan ohjaajan vasemmalle puolelle ilman istumista. Seuraaminen jatkuu vasemmalla.'
],[86, '322', 'TÄYSKÄÄNNÖS, KUTSU ETEEN, ISTU, OIKEALTA VASEMMALLE, ISTU', ' (B)', 'Tätä kylttiä voi käyttää vain kylttien 319, 408 ja 409 jälkeen. Kyltti on sijoitettu 3–5 metrin päähän edellisestä kyltistä. Ohjaaja tekee täyskäännöksen, pysähtyy ja kutsuu koiraa. Ohjaaja saa pysähtyä ennen täyskäännöstä. Koira istuu ohjaajan eteen ja siirtyy ohjaajan takaa vasemmalle puolelle istumaan. Seuraaminen jatkuu vasemmalla.'
],[87, '323', 'TÄYSKÄÄNNÖS, KUTSU ETEEN, ISTU, VASEMMALTA VASEMMALLE, ISTU', ' (B)', 'Tätä kylttiä voi käyttää vain kylttien 319, 408 ja 409 jälkeen. Kyltti on sijoitettu 3–5 metrin päähän edellisestä kyltistä. Ohjaaja tekee täyskäännöksen, pysähtyy ja kutsuu koiraa. Ohjaaja saa pysähtyä ennen täyskäännöstä. Koira istuu ohjaajan eteen ja siitä suoraan ohjaajan vasemmalle puolelle istumaan. Seuraaminen jatkuu vasemmalla.'
],[88, '324', 'KÄÄNNÖS OIKEAAN, OHJAAJAN YMPÄRI', ' (B)', 'Ohjaaja tekee käännöksen oikeaan koiran kiertäessä pysähtymättä ohjaajan ympäri vastapäivään.'
],[89, '325', 'ETEEN SEISO, OIKEALTA VASEMMALLE, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira siirtyy seisomaan ohjaajan eteen ja siitä ohjaajan takaa vasemmalle puolelle istumaan. Seuraaminen jatkuu vasemmalla.'
],[90, '326', 'ETEEN SEISO, VASEMMALTA VASEMMALLE, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira siirtyy seisomaan ohjaajan eteen. Koira siirtyy suoraan ohjaajan vasemmalle puolelle istumaan. Seuraaminen jatkuu vasemmalla.'
],[91, '401', '2 SIVUASKELTA OIKEAAN', ' (B)', 'Koirakon liikkuessa ohjaaja ottaa kaksi askelta oikeaan koiran seuratessa samassa linjassa ja rintamasuunnassa ohjaajan kanssa. Koirakko jatkaa kyltin oikealta puolelta.'
],[92, '402', '2 SIVUASKELTA VASEMPAAN', ' (B)', 'Koirakon liikkuessa ohjaaja ottaa kaksi askelta vasempaan koiran seuratessa samassa linjassa ja rintamasuunnassa ohjaajan kanssa. Koirakko jatkaa kyltin vasemmalta puolelta.'
],[93, '403', 'ISTU, 2 SIVUASKELTA OIKEAAN, ISTU', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Ohjaaja ottaa kaksi askelta oikeaan koiran seuratessa samassa linjassa ja rintamasuunnassa ohjaajan kanssa. Ohjaajan pysähtyessä koira istuu. Koirakko jatkaa kyltin oikealta puolelta.'
],[94, '404', 'ISTU, 2 SIVUASKELTA VASEMPAAN, ISTU', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Ohjaaja ottaa kaksi askelta vasempaan koiran seuratessa samassa linjassa ja rintamasuunnassa ohjaajan kanssa. Ohjaajan pysähtyessä koira istuu. Koirakko jatkaa kyltin vasemmalta puolelta.'
],[95, '405', 'TÄYSKÄÄNNÖS POISPÄIN', ' (B)', 'Koirakon liikkuessa molemmat tekevät tiiviin ja yhdenaikaisen täyskäännöksen poispäin toisistaan. Seuraamispuoli vaihtuu.'
],[96, '406', 'PUOLENVAIHTO EDESTÄ', ' (A)', 'Koirakon liikkuessa koira tekee puolenvaihdon ohjaajan edestä. Koira ei saa pyörähtää puolta vaihtaessaan. Seuraamispuoli vaihtuu.'
],[97, '407', 'LIIKKEESSÄ OHJAAJAN YMPÄRI', ' (A)', 'Koirakon liikkuessa koira kiertää ohjaajan ympäri etukautta ja palaa alkuperäiselle seuraamispaikalleen.'
],[98, '408', 'LIIKKEESTÄ ISTU, JÄTÄ KOIRA', ' (A)', 'Koirakon liikkuessa koira istuu ja ohjaaja jatkaa pysähtymättä joko kutsukyltille tai kutsukartion ohi (C) ja kutsuu koiran seuraamaan. Koira pysyy istumassa, kunnes ohjaaja kutsuu koiraa. Kartiota käytettäessä luoksetulo on osa tätä tehtävää. Seuraamispuoli ei vaihdu.'
],[99, '409', 'LIIKKEESTÄ MAAHAN, JÄTÄ KOIRA', ' (A)', 'Koirakon liikkuessa koira menee maahan ja ohjaaja jatkaa pysähtymättä joko kutsukyltille tai kutsukartion ohi (C) ja kutsuu koiran seuraamaan. Koira pysyy maassa, kunnes ohjaaja kutsuu koiraa. Kartiota käytettäessä luoksetulo on osa tätä tehtävää. Seuraamispuoli ei vaihdu.'
],[100, '410', 'ISTU, LÄHETÄ KOIRA, SEISO, KUTSU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koirakko saa pysähtyessään kääntyä kohti kartiota. Ohjaaja lähettää koiran seisomaan kartion luo. Koira pysyy seisomassa kartion luona, kun ohjaaja kävelee kutsukartion ohi (C) ja kutsuu koiran seuraamaan. Seuraamispuoli ei vaihdu.'
],[101, '411', 'ETEEN SEISO, PERUUTA, SEISO', ' (A)', 'Ohjaajan pysähtyessä koira siirtyy ohjaajan eteen seisomaan. Koira peruuttaa vähintään kolme rungonmittaansa poispäin ohjaajasta ja pysähtyy seisomaan. Ohjaaja kävelee rataa eteenpäin koiran luo/linjalle ja kutsuu pysähtymättä koiran vasemmalle seuraamispuolelle. Seuraaminen jatkuu vasemmalla.'
],[102, '412', '3 ASKELTA TAAKSE', ' (A)', 'Koirakon liikkuessa ohjaaja ottaa vähintään kolme askelta taaksepäin koiran peruuttaessa samassa linjassa ja rintamasuunnassa ohjaajan kanssa.'
],[103, '413', 'ISTU, 1 ASKEL TAAKSE SEISO, 2 ASKELTA TAAKSE ISTU, 3 ASKELTA TAAKSE MAAHAN', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Ohjaajan peruuttaessa koira peruuttaa samassa linjassa ja rintamasuunnassa ohjaajan vieressä ja ohjaajan pysähtyessä koira ottaa määrätyn asennon. Ohjaajan peruutettua yhden askeleen koira seisoo, ohjaajan peruutettua kaksi askelta koira istuu ja ohjaajan peruutettua kolme askelta koira menee maahan. Koira pysyy maassa, kunnes koirakko lähtee liikkeelle.'
],[104, '414', 'ISTU, KÄÄNNÖS OIKEAAN, SEISO, KÄÄNNÖS OIKEAAN, ISTU, KÄÄNNÖS OIKEAAN, MAAHAN', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koirakko tekee yhdessä käännöksen oikeaan, pysähtyy ja koira seisoo. Koirakko tekee yhdessä käännöksen oikeaan, pysähtyy ja koira istuu. Koirakko tekee yhdessä käännöksen oikeaan, pysähtyy ja koira menee maahan. Koira pysyy maassa, kunnes koirakko lähtee liikkeelle.'
],[105, '415', 'ISTU, KÄÄNNÖS VASEMPAAN, SEISO, KÄÄNNÖS VASEMPAAN, ISTU, KÄÄNNÖS VASEMPAAN, MAAHAN', ' (B)', 'Ohjaajan pysähtyessä koira istuu ohjaajan viereen. Koirakko tekee yhdessä käännöksen vasempaan, pysähtyy ja koira seisoo. Koirakko tekee yhdessä käännöksen vasempaan, pysähtyy ja koira istuu. Koirakko tekee yhdessä käännöksen vasempaan, pysähtyy ja koira menee maahan. Koira pysyy maassa, kunnes koirakko lähtee liikkeelle.'
],[106, '416', 'ETEEN ISTU, SIVUASKEL VASEMPAAN, ISTU, SIVUASKEL OIKEAAN, ISTU', ' (A)', 'Ohjaajan pysähtyessä koira istuu ohjaajan eteen. Ohjaaja ottaa yhden askeleen vasempaan koiran siirtyessä mukana samassa linjassa ohjaajan edessä. Koira istuu ohjaajan eteen, kun ohjaaja pysähtyy. Ohjaaja ottaa yhden askeleen oikeaan koiran siirtyessä mukana samassa linjassa ohjaajan edessä. Koira istuu ohjaajan eteen, kun ohjaaja pysähtyy. Koira siirtyy ohjaajan vasemmalle puolelle istumaan. Seuraaminen jatkuu vasemmalla.'
],[107, '417', 'KÄÄNNÖS VASEMPAAN, KARTION YMPÄRI', ' (A)', 'Koirakon liikkuessa ohjaaja lähettää koiran kiertämään kartion myötäpäivään. Koiran tulee aloittaa kartiolle lähestyminen ennen kuin ohjaaja on kyltin kohdalla. Ohjaaja tekee käännöksen vasempaan ennen kartiota ja koira tulee kartion kierrettyään ohjaajan oikealle puolelle seuraamaan. Ohjaaja saa hidastaa tahtiaan koiran kiertäessä kartiota. Seuraamispuoli vaihtuu.'
],[108, '418', 'KÄÄNNÖS OIKEAAN, KARTION YMPÄRI', ' (A)', 'Koirakon liikkuessa ohjaaja lähettää koiran kiertämään kartion vastapäivään. Koiran tulee aloittaa kartiolle lähestyminen ennen kuin ohjaaja on kyltin kohdalla. Ohjaaja tekee käännöksen oikeaan ennen kartiota ja koira tulee kartion kierrettyään ohjaajan vasemmalle puolelle seuraamaan. Ohjaaja saa hidastaa tahtiaan koiran kiertäessä kartiota. Seuraamispuoli vaihtuu.'
],[109, '419', 'LIIKKEESTÄ ISTU, KIERRÄ KOIRA', ' (A)', 'Koirakon liikkuessa koira istuu ja ohjaaja pysähtymättä kiertää koiran ympäri etukautta, palaa koiran viereen ja pysähtyy.'
],[110, '420', 'ISTU, KUTSU ESTEEN YLI', ' (A+D)', 'Koirakko pysähtyy kyltin viereen ja koira istuu. Ohjaaja kävelee ilman koiraa esteen ohi ja kutsuu koiraa. Koira hyppää esteen yli ja palaa seuraamaan. Seuraamispuoli ei vaihdu. Ohjaaja saa kutsuttuaan hidastaa.'
],[111, '421', 'TÄYSKÄÄNNÖS, KUTSU ESTEEN YLI', ' (B)', 'Tätä kylttiä voi käyttää vain kylttien 319, 408 ja 409 jälkeen. Ohjaaja tekee täyskäännöksen, pysähtyy ja kutsuu koiraa. Ohjaaja saa pysähtyä ennen täyskäännöstä. Ohjaaja kutsuu koiran esteen yli vasemmalle puolelleen ilman istumista. Seuraaminen jatkuu vasemmalla.'
],[112, '422', 'TÄYSKÄÄNNÖS, PERUUTA, ISTU, MAAHAN, KUTSU, ISTU', ' (B)', 'Tätä kylttiä voi käyttää vain kylttien 319, 408 ja 409 jälkeen. Ohjaaja tekee täyskäännöksen ja pysähtyy. Ohjaaja saa pysähtyä ennen täyskäännöstä. Koira peruuttaa vähintään yhden rungonmittansa ja istuu, josta menee maahan. Ohjaaja kutsuu koiran vasemmalle puolelleen istumaan. Seuraaminen jatkuu vasemmalla.'
],
    ]
    possibilities =[]
    
    """
    #luokat numero vastaa rally_kyltit_kopio.txt tiedoston jokaisen rivin alussa olevia numeroita
    with open('salat\rally_kyltit_kopio.txt', 'r', encoding='utf-8') as kyltitfile:
    """
    for row in all_exes:
        parts= row #parts[0] on järjestysnumero
        
        #print(parts[0], parts[1], parts[2], parts[3], parts[4])
        #seuravaksi pistäisi lisätä rivit, jotka alkavat tietyillä nmeroilla possibilities listaan
        if int(parts[0]) in pool:
            possibilities.append(row)
            
    
    
    choosen_exes=[]
    
    if len(possibilities) >= lkm:
        choosen_exes= sample(possibilities, lkm)
    else:
        choosen_exes=possibilities

    while lkm>0:
        for exes in choosen_exes:
            pydom["div#rally2"].html = f"{exes[1]} {exes[2]}"
            lkm -= 1
        