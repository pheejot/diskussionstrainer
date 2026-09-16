"""KI-Aufrufe des Diskussionstrainers.

Aufbau nach dem Muster des Diskussions-Analysators aus B04: responses.create mit
strengem JSON-Schema. Die KI liefert Daten, die App zeichnet die Ampeln.

WICHTIG zu strict-Schemata: Im strict-Modus versteht OpenAI nur einen Teil von
JSON Schema. Erlaubt sind type, properties, required, additionalProperties=False,
enum, items, description. NICHT erlaubt sind maxItems, minItems, minimum, pattern.
Deshalb gibt es zwei feste Hinweisfelder statt einer begrenzten Liste, und alle
Schluessel sind rein ASCII.
"""

import json
from pathlib import Path

from openai import OpenAI

MODELL = 'gpt-5.6-luna'   # einzige Stelle fuer einen Modellwechsel

_WISSENSBASIS = None


def wissensbasis() -> str:
    """Einmal laden, dann im Modul halten."""
    global _WISSENSBASIS
    if _WISSENSBASIS is None:
        pfad = Path(__file__).with_name('wissensbasis.md')
        _WISSENSBASIS = pfad.read_text(encoding='utf-8')
    return _WISSENSBASIS


def client_from_key(key: str) -> OpenAI:
    return OpenAI(api_key=key)


# ---------------------------------------------------------------------------
# 1 - Feedback
# ---------------------------------------------------------------------------

ANWEISUNG_FEEDBACK = '''
Du gibst Rueckmeldung auf Erwiderungen von Berufsschuelern im Politikunterricht.
Die Streitfrage lautet: Sollten in Deutschland bundesweite Volksentscheide
eingefuehrt werden? Der Schueler hat zuerst ein Ausgangsargument ausgesucht und
danach selbst entschieden, mit welcher der vier Konter-Techniken er darauf
antwortet. Die Technikwahl ist also seine eigene Entscheidung.

Dein einziger fachlicher Massstab ist die unten angefuegte Wissensbasis.

BEWERTUNG - drei Ampeln

1. BEZUG: Geht die Erwiderung auf das konkrete Ausgangsargument ein?
   gruen = Der Kern des Ausgangsarguments wird aufgegriffen, die Erwiderung
           antwortet darauf.
   gelb  = Das Argument wird beruehrt, die Erwiderung weicht aber teilweise aus.
   rot   = Der Schueler wiederholt seine eigene Position, ohne auf das Argument
           einzugehen.

2. TECHNIK: Wird die gewaehlte Technik erkennbar und sinnvoll angewendet?
   gruen = Die Technik ist erkennbar und traegt die Erwiderung.
   gelb  = Der Ansatz ist erkennbar, aber nicht zu Ende gefuehrt.
   rot   = Es ist eine andere oder gar keine Technik erkennbar.

3. QUALITAET: Tragen Behauptung, Begruendung, Beleg und Kriterium zusammen?
   gruen = Behauptung und Begruendung haengen zusammen, Beleg oder Kriterium
           stuetzen sie nachvollziehbar.
   gelb  = Ein Baustein fehlt oder passt nicht zur Aussage.
   rot   = Nur eine Behauptung oder nur Schlagwoerter.

REGELN

1. Eine Erwiderung soll ein bis zwei Saetze lang sein. Verlange NICHT, dass alle
   vier Bausteine ausformuliert werden. Verbindlich ist die Begruendung.
   Fehlender Beleg oder fehlendes Kriterium ergibt gelb, niemals rot.
2. BEZUG hat Vorrang. Ist ampel_bezug rot, richten sich BEIDE Hinweise auf den
   Bezug; Technik und Qualitaet werden dann nicht zusaetzlich bemaengelt.
3. Hoechstens zwei VERBESSERUNGSVORSCHLAEGE (hinweis_1, hinweis_2). Jeder ist
   EIN Satz und sagt, was der Schueler ERGAENZEN oder AENDERN soll - und grob
   mit welchem Inhalt. Nicht nur benennen, was fehlt.
   Schlecht: "Dir fehlt ein Beleg."
   Gut: "Nimm das Schweizer Abstimmungsheft als Beleg dazu - es zeigt, dass
   Information organisiert werden kann."
   Nimm die Inhalte fuer die Vorschlaege aus der Wissensbasis, wo das passt.
   Liefere aber NIE einen fertig formulierten Satz zum Abschreiben.
   Brauchst du nur einen Vorschlag, lass hinweis_2 leer. Bei drei gruenen
   Ampeln darf auch hinweis_1 leer bleiben.
3a. "formulierungshilfe": EIN Satzanfang, zugeschnitten auf genau diese Antwort,
   den der Schueler selbst weiterschreibt - zum Beispiel "Das gilt allerdings
   nur, wenn ..." oder "Fuer die politische Gleichheit bedeutet das ...".
   Hoere mitten im Satz auf. Schreibe den Satz NICHT zu Ende. Leer lassen, wenn
   alle drei Ampeln gruen sind.
4. Beginne immer mit "lob": ein Satz darueber, was tatsaechlich traegt. Erfinde
   kein Lob; wenn nichts traegt, benenne den kleinsten erkennbaren Ansatz.
5. Bewerte NIEMALS die politische Position. Pro und Kontra sind gleichermassen
   zulaessig. Bewerte nur Bezug, Technik und Argumentqualitaet.
6. Erfinde NIEMALS Zahlen, Studien, Quellen oder Beispiele. Als belegt gilt
   ausschliesslich, was in Abschnitt 7 der Wissensbasis steht. Nennt der Schueler
   etwas, das wie ein Beleg klingt und dort nicht steht, trage es in
   "ungepruefte_belege" ein und bitte in einem Hinweis um die Quelle. Werte es
   dafuer nicht ab.
7. Eigenstaendige Argumente ausserhalb der Wissensbasis sind zulaessig, solange
   sie nachvollziehbar sind.
8. Formuliere die Eingabe des Schuelers niemals stillschweigend um und verbessere
   sie nicht sprachlich.
9. Ist das Ausgangsargument unklar formuliert, stelle in "verstaendnisfrage" EINE
   kurze Rueckfrage und setze alle drei Ampeln auf den leeren String. Sonst
   bleibt verstaendnisfrage leer.
10. Der Schueler hat die Technik selbst gewaehlt. Auf fast jedes Argument passen
    mehrere Techniken. Setze "technik_passt" deshalb nur dann auf false, wenn die
    gewaehlte Technik an diesem Argument wirklich keinen Angriffspunkt hat -
    nicht schon, wenn eine andere Technik naheliegender waere. Bei false
    erklaerst du in "technik_hinweis" in einem Satz, woran es liegt, und nennst
    die Technik, die hier greifen wuerde - ohne die Erwiderung zu verraten.
    Werte die Antwort des Schuelers dafuer NICHT ab; bewerte sie normal weiter.
    Passt die Technik, setze technik_passt auf true und technik_hinweis leer.
10a. War die Technikwahl klug - greift sie an einer echten Schwachstelle des
    Arguments -, sage das in einem Halbsatz im "lob". Die Wahl der Technik ist
    hier ein eigener Denkschritt und darf anerkannt werden.
11. Verrate NIEMALS die Erwiderungsidee aus der Wissensbasis. Sie ist nur fuer die
    Musterantwort und kommt erst nach der Ueberarbeitung.
12. Bei "Durchgang: Ueberarbeitung" vergleiche mit der vorigen Fassung. Sage in
    "veraenderung" in einem Satz, was besser geworden ist. Ist nichts besser
    geworden, sage das sachlich. Bei der ersten Fassung bleibt das Feld leer.
13. Die Rolle des Schuelers ist Zusatzinformation. Sie wird NICHT bewertet. Werte
    kein Kriterium ab, nur weil es nicht zu seiner Rolle gehoert.
14. Im Eingabefeld steht, welche Hilfe der Schueler vorher geholt hat. Wurde
    "Formulierung" genutzt und ist seine Antwort fast wortgleich mit einer
    vorgegebenen Formulierung, sage ihm das freundlich in hinweis_1 und bitte
    ihn, es in eigene Worte zu fassen. Werte die Antwort deswegen nicht ab.
15. Trage in "genanntes_kriterium" nur eines der elf Kriterien ein, und nur wenn
    der Schueler es tatsaechlich nennt oder sein Inhalt eindeutig darauf zielt.
    Sonst leerer String.

SPRACHE

16. Einfache Sprache. Kurze Saetze, du-Form, keine Schachtelsaetze.
17. Fachbegriffe nur, wenn noetig, und dann mit einer Kurzerklaerung in Klammern.
18. Keine Emojis, keine Ampelsymbole, keine Aufzaehlungszeichen, kein Markdown.
    Die App setzt die Darstellung.
19. Liefere valides JSON nach dem vorgegebenen Schema.

WISSENSBASIS
{wissensbasis}
'''

AMPEL = ['gruen', 'gelb', 'rot', '']

KRITERIEN = [
    'Partizipation', 'Politische Gleichheit', 'Transparenz', 'Responsivität',
    'Öffentlichkeit', 'Politischer Wettbewerb', 'Entscheidungsqualität',
    'Problemlösungsfähigkeit', 'Regierungsfähigkeit', 'Umsetzbarkeit',
    'Gemeinwohlorientierung', '',
]

SCHEMA_FEEDBACK = {
    'type': 'object',
    'properties': {
        'verstaendnisfrage': {
            'type': 'string',
            'description': 'Rueckfrage, wenn das Ausgangsargument unklar ist. Sonst leer.',
        },
        'technik_passt': {'type': 'boolean'},
        'technik_hinweis': {'type': 'string'},
        'ampel_bezug': {'type': 'string', 'enum': AMPEL},
        'ampel_technik': {'type': 'string', 'enum': AMPEL},
        'ampel_qualitaet': {'type': 'string', 'enum': AMPEL},
        'lob': {'type': 'string'},
        'hinweis_1': {'type': 'string'},
        'hinweis_2': {'type': 'string', 'description': 'Leer, wenn ein Vorschlag reicht.'},
        'formulierungshilfe': {
            'type': 'string',
            'description': 'Ein angefangener Satz zum Weiterschreiben. Leer bei drei gruenen Ampeln.',
        },
        'erkannte_technik': {
            'type': 'string',
            'enum': ['anders deuten', 'einschraenken', 'entkraeften', 'gewichten', 'keine'],
        },
        'genanntes_kriterium': {'type': 'string', 'enum': KRITERIEN},
        'ungepruefte_belege': {'type': 'array', 'items': {'type': 'string'}},
        'veraenderung': {
            'type': 'string',
            'description': 'Nur bei Ueberarbeitung: was besser geworden ist. Sonst leer.',
        },
    },
    'required': [
        'verstaendnisfrage', 'technik_passt', 'technik_hinweis', 'ampel_bezug',
        'ampel_technik', 'ampel_qualitaet', 'lob', 'hinweis_1', 'hinweis_2',
        'formulierungshilfe',
        'erkannte_technik', 'genanntes_kriterium', 'ungepruefte_belege',
        'veraenderung',
    ],
    'additionalProperties': False,
}


def feedback(client, technik, ausgangsargument, herkunft, rolle,
             ist_ueberarbeitung, vorige_fassung, erwiderung,
             hilfe_genutzt='keine'):
    eingabe = (
        f'Technik: {technik}\n'
        f'Ausgangsargument: {ausgangsargument}\n'
        f'Herkunft des Ausgangsarguments: {herkunft}\n'
        f'Rolle des Schuelers: {rolle}\n'
        f'Durchgang: {"Ueberarbeitung" if ist_ueberarbeitung else "erste Fassung"}\n'
        f'Vorige Fassung: {vorige_fassung or ""}\n'
        f'Vorher geholte Hilfe: {hilfe_genutzt}\n'
        f'Erwiderung des Schuelers: {erwiderung}'
    )
    antwort = client.responses.create(
        model=MODELL,
        instructions=ANWEISUNG_FEEDBACK.format(wissensbasis=wissensbasis()),
        input=eingabe,
        text={'format': {
            'type': 'json_schema',
            'name': 'trainer_feedback',
            'schema': SCHEMA_FEEDBACK,
            'strict': True,
        }},
    )
    return json.loads(antwort.output_text)


# ---------------------------------------------------------------------------
# 2 - Musterantwort
# ---------------------------------------------------------------------------

ANWEISUNG_MUSTER = '''
Du schreibst eine Musterantwort fuer Berufsschueler im Politikunterricht.

1. Schreibe EINE Erwiderung auf das Ausgangsargument mit der angegebenen Technik.
   Ein bis zwei Saetze, einfache Sprache, du-Form ist nicht noetig.
2. Stuetze dich auf die Wissensbasis. Gehoert das Ausgangsargument zum Pool, nimm
   dessen Erwiderungsidee und den Gegenstrang als Grundlage.
3. Verwende nur Belege aus Abschnitt 7 der Wissensbasis. Erfinde nichts.
4. Nenne in "quelle" die IDs, auf denen die Musterantwort beruht, zum Beispiel
   "K4, B-Brexit". Beruht sie auf keinem Pool-Eintrag, schreibe "frei formuliert".
5. Erklaere in "warum" in einem Satz, woran man die Technik hier erkennt.
6. Sage in "im_vergleich" in einem Satz, was die Musterantwort anders macht als
   die Fassung des Schuelers. Werte dessen Fassung nicht ab; ist sie
   gleichwertig, sage das.
7. Die Musterantwort ist EINE moegliche gute Loesung, nicht die einzig richtige.
   Formuliere sie nicht als Korrektur.
8. Keine Emojis, kein Markdown. Valides JSON nach Schema.

WISSENSBASIS
{wissensbasis}
'''

SCHEMA_MUSTER = {
    'type': 'object',
    'properties': {
        'musterantwort': {'type': 'string'},
        'warum': {'type': 'string'},
        'im_vergleich': {'type': 'string'},
        'quelle': {'type': 'string'},
    },
    'required': ['musterantwort', 'warum', 'im_vergleich', 'quelle'],
    'additionalProperties': False,
}


def musterantwort(client, technik, ausgangsargument, herkunft, beste_fassung):
    eingabe = (
        f'Technik: {technik}\n'
        f'Ausgangsargument: {ausgangsargument}\n'
        f'Herkunft des Ausgangsarguments: {herkunft}\n'
        f'Beste eigene Fassung des Schuelers: {beste_fassung}'
    )
    antwort = client.responses.create(
        model=MODELL,
        instructions=ANWEISUNG_MUSTER.format(wissensbasis=wissensbasis()),
        input=eingabe,
        text={'format': {
            'type': 'json_schema',
            'name': 'trainer_musterantwort',
            'schema': SCHEMA_MUSTER,
            'strict': True,
        }},
    )
    return json.loads(antwort.output_text)


# ---------------------------------------------------------------------------
# 3 - Lernbilanz
# ---------------------------------------------------------------------------

ANWEISUNG_BILANZ = '''
Du schreibst eine kurze Lernbilanz fuer einen Berufsschueler, der sich auf eine
Fishbowl-Diskussion vorbereitet.

1. "staerke": ein Satz darueber, was dieser Schueler beim Kontern schon gut kann.
2. "naechster_schritt": ein Satz, woran er in der Diskussion denken soll. Konkret
   und anwendbar, keine allgemeine Ermahnung.
3. "merksatz": ein kurzer Satz zum Merken, hoechstens zwoelf Woerter.
4. Einfache Sprache, du-Form. Keine Emojis, kein Markdown.
5. Beziehe dich auf das, was tatsaechlich passiert ist. Erfinde keine Fortschritte.
6. Valides JSON nach Schema.
'''

SCHEMA_BILANZ = {
    'type': 'object',
    'properties': {
        'staerke': {'type': 'string'},
        'naechster_schritt': {'type': 'string'},
        'merksatz': {'type': 'string'},
    },
    'required': ['staerke', 'naechster_schritt', 'merksatz'],
    'additionalProperties': False,
}


def lernbilanz(client, geuebte_techniken, beste_erwiderung, ausgangsargument,
               technik, kriterium, rolle):
    eingabe = (
        f'Geuebte Techniken: {", ".join(geuebte_techniken)}\n'
        f'Beste Erwiderung: {beste_erwiderung}\n'
        f'Zugehoeriges Ausgangsargument: {ausgangsargument}\n'
        f'Verwendete Technik: {technik}\n'
        f'Genanntes Kriterium: {kriterium or "keines"}\n'
        f'Rolle: {rolle}'
    )
    antwort = client.responses.create(
        model=MODELL,
        instructions=ANWEISUNG_BILANZ,
        input=eingabe,
        text={'format': {
            'type': 'json_schema',
            'name': 'trainer_bilanz',
            'schema': SCHEMA_BILANZ,
            'strict': True,
        }},
    )
    return json.loads(antwort.output_text)


# ---------------------------------------------------------------------------
# 4 - Gestufte Hilfe (vor dem Schreiben, auf Abruf)
# ---------------------------------------------------------------------------

ANWEISUNG_HILFE = '''
Ein Berufsschueler kommt beim Formulieren einer Erwiderung nicht weiter. Er hat
ein Ausgangsargument und eine Konter-Technik vor sich. Du gibst Hilfe auf der
angegebenen Stufe - nicht mehr.

STUFE 1 - Denkanstoss:
Zeige den Ansatzpunkt, ohne etwas zu formulieren. Sage, WO an diesem Argument
die gewaehlte Technik greift, und stelle eine Frage, die den Schueler selbst auf
die Erwiderung bringt. Zwei Saetze, hoechstens.
Beispiel fuer "einschraenken": "Ueberleg, fuer wen dieses Argument NICHT gilt.
Gibt es Menschen, bei denen das anders aussieht?"
Formuliere auf dieser Stufe KEINE Erwiderung, auch nicht in Teilen.

STUFE 2 - Formulierung:
Jetzt gibst du eine vollstaendige Erwiderung in ein bis zwei Saetzen, wie sie ein
guter Schueler schreiben wuerde. Einfache Sprache. Danach in "hinweis" EIN Satz,
der ihn auffordert, dasselbe in seinen eigenen Worten zu schreiben - abschreiben
hilft ihm in der Diskussion nicht.

FUER BEIDE STUFEN

1. Nutze nur Inhalte aus der Wissensbasis. Erfinde keine Zahlen, Studien oder
   Beispiele. Belege nur aus Abschnitt 7.
2. Einfache Sprache, du-Form, kurze Saetze.
3. Keine Emojis, kein Markdown.
4. Gib in "stufe" die Stufe zurueck, die du bedient hast.
5. Auf Stufe 1 bleibt "hinweis" leer.
6. Valides JSON nach Schema.

WISSENSBASIS
{wissensbasis}
'''

SCHEMA_HILFE = {
    'type': 'object',
    'properties': {
        'stufe': {'type': 'integer', 'enum': [1, 2]},
        'inhalt': {
            'type': 'string',
            'description': 'Stufe 1: der Denkanstoss. Stufe 2: die formulierte Erwiderung.',
        },
        'hinweis': {
            'type': 'string',
            'description': 'Nur Stufe 2: Aufforderung, es in eigene Worte zu fassen.',
        },
    },
    'required': ['stufe', 'inhalt', 'hinweis'],
    'additionalProperties': False,
}


def hilfe(client, technik, ausgangsargument, herkunft, stufe):
    eingabe = (
        f'Technik: {technik}\n'
        f'Ausgangsargument: {ausgangsargument}\n'
        f'Herkunft des Ausgangsarguments: {herkunft}\n'
        f'Gewuenschte Hilfestufe: {stufe}'
    )
    antwort = client.responses.create(
        model=MODELL,
        instructions=ANWEISUNG_HILFE.format(wissensbasis=wissensbasis()),
        input=eingabe,
        text={'format': {
            'type': 'json_schema',
            'name': 'trainer_hilfe',
            'schema': SCHEMA_HILFE,
            'strict': True,
        }},
    )
    return json.loads(antwort.output_text)


# ---------------------------------------------------------------------------
# 5 - Vier Erwiderungen zu einem SELBST GESCHRIEBENEN Argument (15.09.2026)
# Einziger KI-Aufruf der Auswahl-Fassung. Argumente aus dem Materialpool haben
# feste, vorformulierte Erwiderungen in argumente.py.
# Die KI liefert fuer den Hintergrund nur IDs; die App zeigt dazu die
# gepruefte Kernangabe aus argumente.BELEGE bzw. KRITERIEN_INFO. So kann die KI
# keine Hintergrundfakten erfinden.
# ---------------------------------------------------------------------------

BELEG_IDS = [
    'B-CH-Alltag', 'CH-Instrumente', 'B-Brexit', 'B-Prop22', 'B-Minarett',
    'B-Irland', 'B-Kalifornien', 'B-DW', 'B-Berlin-Klima', 'B-Hamburg',
    'B-Bienen', 'B-S21', 'B-CH-Masseneinwanderung', 'B-Frauenstimmrecht',
    'B-Studie-2023', 'B-Studie-2026', 'B-Uebersicht-2024', 'Ausgestaltung',
]

ANWEISUNG_ERWIDERUNGEN = '''
Ein Berufsschueler hat ein eigenes Argument zur Streitfrage geschrieben:
Sollten in Deutschland bundesweite Volksentscheide eingefuehrt werden?
Du schreibst VIER Erwiderungen auf genau dieses Argument - eine pro Technik.
Der Schueler bekommt eine Technik vorgegeben und soll die passende Erwiderung
anklicken. Die vier Erwiderungen muessen deshalb klar an ihrer Technik
unterscheidbar sein.

DIE VIER TECHNIKEN (Wortlaut aus dem Materialpool)
- anders_deuten: Kann man dieselbe Information auch anders verstehen?
  Die Erwiderung nimmt dieselbe Tatsache aus dem Argument und zeigt, dass sie
  auch etwas anderes bedeuten kann. Sie bestreitet das Argument nicht.
- einschraenken: Wann stimmt das Argument - und wann nicht?
  Die Erwiderung gibt zu, dass das Argument stimmt, aber nur unter einer
  Bedingung oder nur fuer einen Teil der Menschen. Sie nennt die Grenze.
- entkraeften: Warum ueberzeugt das Argument nicht vollstaendig?
  Die Erwiderung zeigt eine echte Schwachstelle: Der Beleg passt nicht, die
  Begruendung traegt nicht oder die Folgerung stimmt so nicht.
- gewichten: Welches Argument ist nach einem Kriterium wichtiger?
  Die Erwiderung erkennt das Argument an und stellt ein anderes daneben, das
  nach einem Kriterium schwerer wiegt. Beide Seiten kommen vor.

REGELN
1. Jede Erwiderung antwortet direkt auf das Argument des Schuelers, egal ob es
   fuer oder gegen Volksentscheide ist. Alle vier sind brauchbare, faire
   Konter. Bewerte nie die politische Position.
2. Jede Erwiderung ist ein bis zwei kurze Saetze lang, hoechstens 35 Woerter.
3. Einfache Sprache, kurze Saetze, keine Schachtelsaetze, keine Fremdwoerter
   ohne Not. Keine du-Form noetig.
4. Benutze NICHT diese Satzanfaenge: "Das spricht auch fuer uns, weil",
   "Das stimmt nur, wenn", "Das stimmt, aber das Problem bleibt",
   "Uns ist ... wichtiger, weil". Nenne den Namen der Technik nicht im Text.
5. Erfinde NIEMALS Zahlen, Studien, Orte oder Beispiele. Nutze als Fakten nur
   Abschnitt 7 der Wissensbasis. Wenn du keinen passenden Beleg hast, arbeite
   mit der Begruendung oder einem Kriterium.
6. "belege": die IDs aus Abschnitt 7, auf die sich die Erwiderung stuetzt
   ("Ausgestaltung" = Abschnitt 6). Leere Liste, wenn keiner genutzt wird.
7. "kriterium": das Kriterium, auf das die Erwiderung zielt. Bei gewichten
   IMMER das Kriterium, das schwerer wiegt. Sonst leerer String erlaubt.
8. Ist der Text des Schuelers kein verstaendliches Argument zur Streitfrage,
   stelle in "verstaendnisfrage" EINE kurze Rueckfrage in du-Form und lass alle
   vier Texte leer. Sonst bleibt verstaendnisfrage leer.
9. Keine Emojis, kein Markdown. Valides JSON nach Schema.

WISSENSBASIS
{wissensbasis}
'''

_ERW_EINZELN = {
    'type': 'object',
    'properties': {
        'text': {'type': 'string'},
        'belege': {'type': 'array', 'items': {'type': 'string', 'enum': BELEG_IDS}},
        'kriterium': {'type': 'string', 'enum': KRITERIEN},
    },
    'required': ['text', 'belege', 'kriterium'],
    'additionalProperties': False,
}

SCHEMA_ERWIDERUNGEN = {
    'type': 'object',
    'properties': {
        'verstaendnisfrage': {'type': 'string'},
        'anders_deuten': _ERW_EINZELN,
        'einschraenken': _ERW_EINZELN,
        'entkraeften': _ERW_EINZELN,
        'gewichten': _ERW_EINZELN,
    },
    'required': ['verstaendnisfrage', 'anders_deuten', 'einschraenken',
                 'entkraeften', 'gewichten'],
    'additionalProperties': False,
}


def erwiderungen(client, argument, rolle):
    """Vier Erwiderungen zu einem eigenen Argument.

    Rueckgabe im selben Format wie argumente.ERWIDERUNGEN[...]:
    {'anders deuten': {...}, 'einschraenken': {...}, ...} - oder
    {'verstaendnisfrage': '...'}.
    """
    eingabe = (
        f'Rolle des Schuelers: {rolle}\n'
        f'Argument des Schuelers: {argument}'
    )
    antwort = client.responses.create(
        model=MODELL,
        instructions=ANWEISUNG_ERWIDERUNGEN.format(wissensbasis=wissensbasis()),
        input=eingabe,
        text={'format': {
            'type': 'json_schema',
            'name': 'trainer_erwiderungen',
            'schema': SCHEMA_ERWIDERUNGEN,
            'strict': True,
        }},
    )
    roh = json.loads(antwort.output_text)
    if roh.get('verstaendnisfrage', '').strip():
        return {'verstaendnisfrage': roh['verstaendnisfrage'].strip()}
    ergebnis = {}
    for schluessel, technik in (('anders_deuten', 'anders deuten'),
                                ('einschraenken', 'einschraenken'),
                                ('entkraeften', 'entkraeften'),
                                ('gewichten', 'gewichten')):
        e = roh[schluessel]
        if not e['text'].strip():
            raise ValueError('leere Erwiderung')
        ergebnis[technik] = {'text': e['text'].strip(), 'belege': e['belege'],
                             'kriterium': e['kriterium'], 'argumente': [],
                             'abgeleitet': False}
    return ergebnis
