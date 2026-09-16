"""Feste Inhalte aus dem Materialpool-Vault.

Die IDs (P1-P10, K1-K9) sind die Schnittstelle zur KI und zur Wissensbasis.
Bei Aenderungen am Vault muessen sie stabil bleiben.
"""

TECHNIKEN = {
    'anders deuten': {
        'emoji': '🔄',
        'leitfrage': 'Kann man dieselbe Information auch anders verstehen?',
        'erklaerung': (
            'Du nimmst dieselbe Tatsache und zeigst, dass man sie auch anders '
            'verstehen kann. Du bestreitest das Argument nicht – du drehst die '
            'Bedeutung.'
        ),
        'beispiel': (
            'Ein Quorum schützt vor kleinen aktiven Gruppen – man kann es aber '
            'auch so deuten, dass es eine Mehrheit der Abstimmenden ausbremst.'
        ),
    },
    'einschraenken': {
        'emoji': '✂️',
        'leitfrage': 'Wann stimmt das Argument – und wann nicht?',
        'erklaerung': (
            'Du gibst zu, dass das Argument stimmt – aber nur unter bestimmten '
            'Bedingungen. Du nennst die Grenze.'
        ),
        'beispiel': 'Debatten können Wissen erhöhen, aber nicht bei allen gleich.',
    },
    'entkraeften': {
        'emoji': '🎯',
        'leitfrage': 'Warum überzeugt das Argument nicht vollständig?',
        'erklaerung': (
            'Du zeigst eine echte Schwachstelle: Der Beleg passt nicht, die '
            'Begründung trägt nicht, oder die Folgerung stimmt so nicht. '
            'Widersprechen allein reicht nicht.'
        ),
        'beispiel': 'Transparenz zeigt viel Geld, beseitigt seinen Einfluss aber nicht.',
    },
    'gewichten': {
        'emoji': '⚖️',
        'leitfrage': 'Welches Argument ist nach einem Kriterium wichtiger?',
        'erklaerung': (
            'Du erkennst das Argument an – und stellst ein anderes daneben, das '
            'nach einem Kriterium schwerer wiegt. Beide Seiten kommen vor.'
        ),
        'beispiel': (
            'Mehr Beteiligung ist wichtig – aber eine gut durchdachte '
            'Entscheidung wiegt hier schwerer.'
        ),
    },
}

# Anzeigename -> interner Schluessel (Umlaute nur in der Anzeige)
TECHNIK_LABEL = {
    'Anders deuten': 'anders deuten',
    'Einschränken': 'einschraenken',
    'Entkräften': 'entkraeften',
    'Gewichten': 'gewichten',
}
TECHNIK_ANZEIGE = {v: k for k, v in TECHNIK_LABEL.items()}

ROLLEN = {
    'ohne Rolle': [],
    'AfD': ['Partizipation', 'Responsivität'],
    'Mehr Demokratie e. V.': ['Öffentlichkeit', 'Transparenz'],
    'CDU': ['Entscheidungsqualität', 'Regierungsfähigkeit'],
    'Sozialverband': ['Politische Gleichheit', 'Gemeinwohlorientierung'],
    'Moderationsteam': [],
}

VAULT = 'https://publish.obsidian.md/volksentscheide-recherche/'


def vault_url(pfad: str) -> str:
    """Vollstaendige Adresse einer Seite im veroeffentlichten Materialpool.

    Geprueft 2026-09-14: Einzelseiten funktionieren, ORDNER nicht -
    .../02_ARGUMENTE gibt "This page does not exist". Als Sammeleinstieg
    dient deshalb 00_START/00_LEITFRAGE.
    """
    return VAULT + pfad


# Feste Einstiegsseiten im Materialpool
POOL_SEITEN = {
    'techniken': ('Die vier Techniken', '03_BEZUEGE/Argumente_kontern'),
    'kriterien': ('Alle Kriterien und Argumente', '00_START/00_LEITFRAGE'),
    'ausgestaltung': ('Bessere Regeln als Erwiderung',
                      '03_BEZUEGE/Auf_die_Ausgestaltung_kommt_es_an'),
    'gutes_argument': ('Was ist ein gutes Argument?',
                       '00_START/01_WAS_IST_EIN_GUTES_ARGUMENT'),
}

# Kriterienname -> Dateiname im Vault (Umlaute dort umschrieben)
KRITERIEN_PFAD = {
    'Partizipation': '01_KRITERIEN/Partizipation',
    'Politische Gleichheit': '01_KRITERIEN/Politische_Gleichheit',
    'Transparenz': '01_KRITERIEN/Transparenz',
    'Responsivität': '01_KRITERIEN/Responsivitaet',
    'Öffentlichkeit': '01_KRITERIEN/Oeffentlichkeit',
    'Politischer Wettbewerb': '01_KRITERIEN/Politischer_Wettbewerb',
    'Entscheidungsqualität': '01_KRITERIEN/Entscheidungsqualitaet',
    'Problemlösungsfähigkeit': '01_KRITERIEN/Problemloesungsfaehigkeit',
    'Regierungsfähigkeit': '01_KRITERIEN/Regierungsfaehigkeit',
    'Umsetzbarkeit': '01_KRITERIEN/Umsetzbarkeit',
    'Gemeinwohlorientierung': '01_KRITERIEN/Gemeinwohlorientierung',
}

# Die 19 Argumente. "pfad" = Seite im Materialpool, "gegen" = Gegenstrang
# (eine Argument-ID, oder ein Vault-Pfad, wo es kein Pool-Argument gibt).
ARGUMENTE = [
    {'id': 'P1', 'seite': 'pro', 'titel': 'Mehr direkte Mitentscheidung',
     'behauptung': 'Bundesweite Volksentscheide stärken die Beteiligung.',
     'begruendung': 'Bürger wählen dann nicht nur Parteien. Sie entscheiden auch '
                    'selbst über konkrete Sachfragen und haben zwischen Wahlen '
                    'direkten Einfluss.',
     'pfad': '02_ARGUMENTE/PRO_Mehr_direkte_Mitentscheidung', 'gegen': 'K8'},
    {'id': 'P2', 'seite': 'pro', 'titel': 'Mitentscheidung kann Akzeptanz stärken',
     'behauptung': 'Wer mitentscheiden kann, akzeptiert politische Entscheidungen eher.',
     'begruendung': 'Ein faires Verfahren zeigt: Meine Stimme wurde gezählt. Das '
                    'kann auch dann wichtig sein, wenn die eigene Seite verliert.',
     'pfad': '02_ARGUMENTE/PRO_Akzeptanz_und_Vertrauen', 'gegen': 'K7'},
    {'id': 'P3', 'seite': 'pro', 'titel': 'Volksentscheide fördern öffentliche Debatten',
     'behauptung': 'Vor Volksentscheiden wird öffentlich über Sachfragen gesprochen.',
     'begruendung': 'Initiativen, Parteien, Medien und Bürger erklären ihre '
                    'Position. Eine konkrete Abstimmungsfrage schafft Aufmerksamkeit.',
     'pfad': '02_ARGUMENTE/PRO_Oeffentliche_Debatte', 'gegen': 'K9'},
    {'id': 'P4', 'seite': 'pro', 'titel': 'Klare Informationen und Regeln sind möglich',
     'behauptung': 'Volksentscheide können transparent und fair gestaltet werden.',
     'begruendung': 'Der Staat kann die Frage prüfen, Pro und Kontra erklären und '
                    'Kampagnengelder offenlegen.',
     'pfad': '02_ARGUMENTE/PRO_Klare_Information_und_Regeln', 'gegen': 'K3'},
    {'id': 'P5', 'seite': 'pro', 'titel': 'Bürger können eigene Fehler korrigieren',
     'behauptung': 'Direkte Demokratie kann eigene Entscheidungen später wieder korrigieren.',
     'begruendung': 'Wenn Bürger selbst abstimmen dürfen, können sie eine frühere '
                    'Entscheidung mit einer neuen Abstimmung ändern.',
     'pfad': '02_ARGUMENTE/PRO_Fehler_koennen_korrigiert_werden', 'gegen': 'K4'},
    {'id': 'P6', 'seite': 'pro', 'titel': 'Bürgerinteressen kommen auf die Agenda',
     'behauptung': 'Volksinitiativen zwingen Politik, Bürgerinteressen ernst zu nehmen.',
     'begruendung': 'Mit genügend Unterschriften können Bürger ein Thema auf die '
                    'Tagesordnung bringen. Parlament und Regierung müssen darauf reagieren.',
     'pfad': '02_ARGUMENTE/PRO_Buergerinteressen_auf_die_Agenda', 'gegen': 'K3'},
    {'id': 'P7', 'seite': 'pro', 'titel': 'Bürger können das Parlament kontrollieren',
     'behauptung': 'Ein Referendum gibt Bürgern ein wirksames Veto.',
     'begruendung': 'Bürger könnten ein beschlossenes Gesetz stoppen. Regierung und '
                    'Parlament müssten deshalb früher erklären und Kompromisse suchen.',
     'pfad': '02_ARGUMENTE/PRO_Parlament_kontrollieren', 'gegen': 'K1'},
    {'id': 'P8', 'seite': 'pro', 'titel': 'Die Drohung einer Abstimmung fördert Kompromisse',
     'behauptung': 'Direkte Demokratie kann Parlamente zu früheren Kompromissen bewegen.',
     'begruendung': 'Wenn Bürger ein Gesetz später stoppen können, bezieht das '
                    'Parlament betroffene Gruppen eher vorher ein.',
     'pfad': '02_ARGUMENTE/PRO_Kompromisse_vor_der_Abstimmung', 'gegen': 'K1'},
    {'id': 'P9', 'seite': 'pro', 'titel': 'Mehr echte Alternativen im Wettbewerb',
     'behauptung': 'Volksentscheide geben einzelnen Vorschlägen eine faire Chance.',
     'begruendung': 'Parteien bündeln viele Themen zu einem Programm. Eine '
                    'Volksinitiative löst eine einzelne Sachfrage heraus – auch ohne '
                    'große Partei dahinter.',
     'pfad': '02_ARGUMENTE/PRO_Mehr_Alternativen_im_Wettbewerb', 'gegen': 'K3'},
    {'id': 'P10', 'seite': 'pro', 'titel': 'Die Agenda wird etwas gleichberechtigter',
     'behauptung': 'Volksinitiativen können Themen mittlerer Gruppen besser aufgreifen.',
     'begruendung': 'Parlamente reagieren oft stärker auf gut vernetzte und '
                    'wohlhabende Gruppen. Eine Initiative eröffnet einen zusätzlichen Weg.',
     'pfad': '02_ARGUMENTE/PRO_Agenda_etwas_gleichberechtigter', 'gegen': 'K8'},

    {'id': 'K1', 'seite': 'kontra', 'titel': 'Häufige Vetos können Politik blockieren',
     'behauptung': 'Viele Referenden können Regieren langsamer und unsicherer machen.',
     'begruendung': 'Beschlossene Gesetze könnten wieder gestoppt werden. Regierung '
                    'und Parlament planen dann weniger sicher.',
     'pfad': '02_ARGUMENTE/KONTRA_Blockaden_und_Unsicherheit', 'gegen': 'P8'},
    {'id': 'K2', 'seite': 'kontra', 'titel': 'Volksentscheide können Demagogen nützen',
     'behauptung': 'Laute Stimmungsmacher und einfache Parolen können zu viel Einfluss bekommen.',
     'begruendung': 'Emotionale Kampagnen wirken vor großem Publikum stark. Eine '
                    'ruhige, sachliche Abwägung tritt dann leicht zurück.',
     'pfad': '02_ARGUMENTE/KONTRA_Demagogen_und_Manipulation', 'gegen': 'P4'},
    {'id': 'K3', 'seite': 'kontra', 'titel': 'Geld beeinflusst Abstimmungskampagnen',
     'behauptung': 'Finanzstarke Gruppen können die öffentliche Debatte dominieren.',
     'begruendung': 'Teure Werbung erreicht viele Menschen. Schwächere Gruppen '
                    'können ihre Gründe weniger sichtbar machen.',
     'pfad': '02_ARGUMENTE/KONTRA_Geld_beeinflusst_Kampagnen', 'gegen': 'P4'},
    {'id': 'K4', 'seite': 'kontra', 'titel': 'Komplexe Fragen werden auf Ja oder Nein verkürzt',
     'behauptung': 'Eine Ja-Nein-Abstimmung kann schwierige Probleme zu stark vereinfachen.',
     'begruendung': 'Im Parlament kann ein Entwurf beraten und verändert werden. Auf '
                    'dem Stimmzettel gibt es nur Zustimmung oder Ablehnung.',
     'pfad': '02_ARGUMENTE/KONTRA_Komplexe_Fragen_werden_vereinfacht', 'gegen': 'P4'},
    {'id': 'K5', 'seite': 'kontra', 'titel': 'Mehrheiten können Minderheiten überstimmen',
     'behauptung': 'Volksentscheide können Interessen von Minderheiten gefährden.',
     'begruendung': 'Eine Mehrheit entscheidet auch über Fragen, die vor allem eine '
                    'kleine Gruppe betreffen. Die Mehrheit spürt die Nachteile '
                    'vielleicht nicht selbst.',
     'pfad': '02_ARGUMENTE/KONTRA_Minderheiten_koennen_verlieren',
     'gegen': '05_KONTEXT/Schutzregeln_fuer_faire_Abstimmungen'},
    {'id': 'K6', 'seite': 'kontra', 'titel': 'Ein Ergebnis löst die Umsetzung nicht',
     'behauptung': 'Ein erfolgreiches Votum ist noch keine umsetzbare Lösung.',
     'begruendung': 'Nach der Abstimmung bleiben Rechtsfragen, Kosten und '
                    'Zuständigkeiten. Eine einfache Forderung kann viele schwierige '
                    'Entscheidungen auslösen.',
     'pfad': '02_ARGUMENTE/KONTRA_Umsetzung_bleibt_kompliziert', 'gegen': 'P6'},
    {'id': 'K7', 'seite': 'kontra', 'titel': 'Vertrauen wächst nicht automatisch',
     'behauptung': 'Volksentscheide lösen Unzufriedenheit mit Demokratie nicht automatisch.',
     'begruendung': 'Vertrauen hängt auch von fairen Ergebnissen und glaubwürdiger '
                    'Politik ab. Wer oft verliert, kann sogar enttäuschter werden.',
     'pfad': '02_ARGUMENTE/KONTRA_Vertrauen_waechst_nicht_automatisch', 'gegen': 'P2'},
    {'id': 'K8', 'seite': 'kontra', 'titel': 'Vor allem Bessergestellte stimmen ab',
     'behauptung': 'Häufige Abstimmungen können politische Ungleichheit vergrößern.',
     'begruendung': 'Menschen mit mehr Bildung, Zeit und politischem Interesse '
                    'beteiligen sich häufiger. Gleiche Stimmzettel führen dann nicht '
                    'zu gleichem Einfluss.',
     'pfad': '02_ARGUMENTE/KONTRA_Vor_allem_Bessergestellte_stimmen_ab', 'gegen': 'P1'},
    {'id': 'K9', 'seite': 'kontra', 'titel': 'Wissen und Information sind ungleich verteilt',
     'behauptung': 'Nicht alle Bürger können komplexe Vorlagen gleich gut prüfen.',
     'begruendung': 'Politische Entscheidungen brauchen Zeit, Fachwissen und '
                    'verständliche Informationen. Die sind ungleich verteilt.',
     'pfad': '02_ARGUMENTE/KONTRA_Wissen_ist_ungleich_verteilt', 'gegen': 'P3'},
]

ARGUMENT_NACH_ID = {a['id']: a for a in ARGUMENTE}


def argument_text(arg_id: str) -> str:
    """Der Wortlaut, der als Ausgangsargument an die KI geht."""
    a = ARGUMENT_NACH_ID[arg_id]
    return f"{a['behauptung']} {a['begruendung']}"


def gegenstrang(arg_id: str):
    """(Beschriftung, Vault-Pfad) des Gegenstrangs - oder None."""
    a = ARGUMENT_NACH_ID.get(arg_id)
    if not a or not a.get('gegen'):
        return None
    gegen = a['gegen']
    if gegen in ARGUMENT_NACH_ID:
        return ARGUMENT_NACH_ID[gegen]['titel'], ARGUMENT_NACH_ID[gegen]['pfad']
    return 'Schutzregeln für faire Abstimmungen', gegen


# ---------------------------------------------------------------------------
# Erweiterung 15.09.2026 - Gegenseite, Hintergrund, Uebertrag auf die Rollenkarte
# Anlass: In der Rollenvorbereitung fehlte Hintergrundwissen, um flexibel zu
# reagieren. Alle Inhalte stammen aus wissensbasis.md (Abschnitte 5 und 7).
# Die Erwiderungsideen werden hier bewusst NICHT uebernommen.
# ---------------------------------------------------------------------------

# Position der Gaesterollen
ROLLEN_SEITE = {
    'AfD': 'pro',
    'Mehr Demokratie e. V.': 'pro',
    'CDU': 'kontra',
    'Sozialverband': 'kontra',
}

# Kriterien je Argument (Wissensbasis Abschnitt 5)
KRITERIEN_ARG = {
    'P1': ['Partizipation'],
    'P2': ['Partizipation', 'Responsivität'],
    'P3': ['Öffentlichkeit'],
    'P4': ['Transparenz'],
    'P5': ['Entscheidungsqualität', 'Problemlösungsfähigkeit'],
    'P6': ['Responsivität'],
    'P7': ['Responsivität'],
    'P8': ['Responsivität', 'Entscheidungsqualität'],
    'P9': ['Politischer Wettbewerb'],
    'P10': ['Politische Gleichheit', 'Responsivität'],
    'K1': ['Regierungsfähigkeit'],
    'K2': ['Entscheidungsqualität', 'Öffentlichkeit'],
    'K3': ['Politische Gleichheit', 'Öffentlichkeit', 'Politischer Wettbewerb'],
    'K4': ['Entscheidungsqualität'],
    'K5': ['Politische Gleichheit', 'Gemeinwohlorientierung'],
    'K6': ['Umsetzbarkeit', 'Problemlösungsfähigkeit'],
    'K7': ['Responsivität', 'Entscheidungsqualität'],
    'K8': ['Politische Gleichheit'],
    'K9': ['Entscheidungsqualität', 'Politische Gleichheit'],
}


def gegenseite(rolle: str):
    """'pro' oder 'kontra' - die Seite, die der Rolle widerspricht. Sonst None."""
    seite = ROLLEN_SEITE.get(rolle)
    if seite is None:
        return None
    return 'kontra' if seite == 'pro' else 'pro'


def typische_rollen(arg_id: str) -> list:
    """Gaesterollen derselben Seite, deren Leitkriterien das Argument trifft.

    Beispiel: K1 (Regierungsfaehigkeit) -> ['CDU']. Damit sieht ein AfD-Gast,
    von wem er dieses Argument in der Fishbowl erwarten muss.
    """
    a = ARGUMENT_NACH_ID.get(arg_id)
    if not a:
        return []
    krit = KRITERIEN_ARG.get(arg_id, [])
    return [r for r, s in ROLLEN_SEITE.items()
            if s == a['seite'] and any(k in krit for k in ROLLEN[r])]


def fuer_rolle_sortiert(auswahl: list) -> list:
    """Argumente mit typischer Gaesterolle zuerst, sonst Reihenfolge wie im Pool."""
    return sorted(auswahl, key=lambda a: 0 if typische_rollen(a['id']) else 1)


# Belege (Wissensbasis Abschnitt 7) - Fall und Kernangabe wortgleich
BELEGE = {
    'B-CH-Alltag': ('Abstimmen gehört in der Schweiz zum Alltag',
                    'Stimmberechtigte erhalten Stimmzettel und offizielle '
                    'Erläuterungen, verschickt spätestens drei Wochen vor dem '
                    'Termin. Viele Vorlagen können aber auch überfordern.'),
    'CH-Instrumente': ('Drei Schweizer Instrumente',
                       'Volksinitiative: 100.000 Unterschriften in 18 Monaten, '
                       'Änderung der Bundesverfassung (Anstoß). Fakultatives '
                       'Referendum: 50.000 Unterschriften in 100 Tagen oder acht '
                       'Kantone, stoppt ein Gesetz (Bremse). Obligatorisches '
                       'Referendum: automatisch, z. B. bei Verfassungsänderungen '
                       '(Pflicht).'),
    'B-Brexit': ('Brexit 2016',
                 '51,9 Prozent für „Leave“. Die Abstimmung entschied die '
                 'Richtung, nicht die Form. Danach mussten Handel, Grenzen, '
                 'Bürgerrechte und Fristen geklärt werden. Ein Weg zur '
                 'Selbstkorrektur fehlte.'),
    'B-Prop22': ('Kalifornien, Proposition 22 (2020)',
                 'Uber, Lyft und weitere Firmen gaben rund 200 Millionen '
                 'US-Dollar aus; die von ihnen unterstützte Seite gewann. Nicht '
                 'direkt auf Deutschland übertragbar.'),
    'B-Minarett': ('Schweiz, Minarettverbot 2009',
                   '57,5 Prozent für ein Verbot neuer Minarette. Das betraf '
                   'besonders die muslimische Minderheit.'),
    'B-Irland': ('Irland, Ehe für alle 2015',
                 'Rund 62 Prozent Ja am 22. Mai 2015. Irland war das erste Land, '
                 'das die Ehe für alle per Volksabstimmung einführte – eine '
                 'Mehrheit kann Minderheitenrechte auch ausweiten.'),
    'B-Kalifornien': ('Kalifornien, Proposition 8 (2008)',
                      'Rund 52 Prozent Ja für ein Verbot der gleichgeschlechtlichen '
                      'Ehe. Gerichte erklärten das Verbot später für ungültig, ab '
                      '2013 waren solche Ehen wieder möglich.'),
    'B-DW': ('Berlin, „Deutsche Wohnen & Co enteignen“ 2021',
             '57,6 Prozent dafür. Danach prüfte eine Expertenkommission '
             'Rechtsfragen, Entschädigung, Kosten und Modelle.'),
    'B-Berlin-Klima': ('Berlin, Klima-Volksentscheid 2023',
                       '50,9 Prozent der Teilnehmenden stimmten mit Ja, aber nur '
                       '18,2 Prozent aller Stimmberechtigten – nötig waren 25 '
                       'Prozent. Die Vorlage wurde nicht angenommen.'),
    'B-Hamburg': ('Hamburger Zukunftsentscheid 2025',
                  '12. Oktober 2025, Beteiligung 43,6 Prozent, 53 Prozent Ja, '
                  'Quorum erreicht, das Gesetz gilt: Klimaneutralität bis 2040 '
                  'statt 2045, jährliche CO2-Budgets, Sozialklausel.'),
    'B-Bienen': ('Bayern, „Rettet die Bienen“ 2019',
                 'Über 1,7 Millionen Unterschriften, über 18 Prozent der '
                 'Stimmberechtigten – das erfolgreichste Volksbegehren in Bayern. '
                 'Der Landtag übernahm die Forderung, ein Volksentscheid fand gar '
                 'nicht statt.'),
    'B-S21': ('Stuttgart 21, Volksabstimmung 2011',
              '58,9 Prozent Nein (also: weiterbauen), 41,1 Prozent Ja, '
              'Beteiligung 48,3 Prozent. Das Ergebnis wurde breit anerkannt und '
              'beendete einen langen Konflikt.'),
    'B-CH-Masseneinwanderung': ('Schweiz 2014',
                                'Rund 50,3 Prozent Ja für feste Höchstzahlen bei '
                                'der Einwanderung. Das widersprach dem Vertrag mit '
                                'der EU; das Parlament setzte nur abgeschwächt um.'),
    'B-Studie-2023': ('Studie zu 43 Schweizer Abstimmungen (2023)',
                      'Wer abstimmt, hängt vor allem davon ab, ob man früher '
                      'regelmäßig teilgenommen hat – dazu Interesse, Bildung und '
                      'soziale Klasse.'),
    'B-Studie-2026': ('Studie zur Schweiz (2026)',
                      'Volksinitiativen bringen Themen mittlerer Einkommens- und '
                      'Bildungsgruppen stärker auf die Tagesordnung als das '
                      'Parlament. Bei den Ergebnissen bleibt ein Vorteil für '
                      'Menschen mit höherem Einkommen und mehr Bildung.'),
    'B-Uebersicht-2024': ('Übersicht über 67 Studien (2024)',
                          'Im Durchschnitt nur kleine positive Wirkungen auf '
                          'Beteiligung, Wissen, Zufriedenheit und Vertrauen – mit '
                          'großen Unterschieden nach Land, Verfahren und Thema.'),
}

# Hintergrund je Argument: Belegsatz (Abschnitt 5, ohne Verweise) + Fall-IDs.
# Nur die Belege des Arguments SELBST - keine Faelle, die schon den Konter
# liefern (z. B. Irland/Kalifornien bei K5). Sonst nimmt der Hintergrund den
# Denkschritt vorweg.
HINTERGRUND = {
    'P1': ('In der Schweiz gibt es auf Bundesebene regelmäßig Volksabstimmungen.',
           ['B-CH-Alltag', 'CH-Instrumente']),
    'P2': ('Studien zeigen positive Wirkungen, eine große Übersicht von 2024 findet '
           'aber nur kleine durchschnittliche Effekte.',
           ['B-Uebersicht-2024', 'B-S21']),
    'P3': ('In der Schweiz erhalten Stimmberechtigte offizielle Erläuterungen mit '
           'Positionen und Argumenten.',
           ['B-CH-Alltag']),
    'P4': ('In der Schweiz werden Abstimmungsunterlagen vorab verschickt, größere '
           'Kampagnen müssen ihre Finanzierung offenlegen.',
           ['B-CH-Alltag']),
    'P5': ('In der Schweiz haben Bürger frühere Ergebnisse später angepasst; beim '
           'Brexit fehlte dieser Weg.',
           ['B-Brexit']),
    'P6': ('Eine Schweizer Studie von 2026 zeigt: Initiativen setzen Themen teilweise '
           'gleichberechtigter auf die Tagesordnung als Parlamente.',
           ['B-Studie-2026', 'B-Bienen']),
    'P7': ('In der Schweiz kann gegen ein Gesetz des Parlaments ein fakultatives '
           'Referendum verlangt werden – mit festen Fristen und Unterschriftenzahlen.',
           ['CH-Instrumente']),
    'P8': ('Schon die Möglichkeit eines Referendums bringt das Parlament dazu, früher '
           'Kompromisse zu suchen. In Bayern übernahm der Landtag 2019 die Forderung.',
           ['CH-Instrumente', 'B-Bienen']),
    'P9': ('In der Schweiz können Bürger mit einer Volksinitiative ein eigenes '
           'Anliegen zur Abstimmung bringen – auch ohne große Partei dahinter.',
           ['CH-Instrumente']),
    'P10': ('Eine Studie von 2026 zeigt: Initiativen bringen Themen mittlerer Gruppen '
            'stärker auf die Tagesordnung; bei den Ergebnissen bleiben Vorteile '
            'höherer Einkommen.',
            ['B-Studie-2026']),
    'K1': ('Der Vergleich Deutschland–Schweiz zeigt: Direkte Demokratie verändert das '
           'ganze politische System. Die Schweiz verbindet sie mit einer starken '
           'Kompromisskultur – einzelne Instrumente lassen sich nicht einfach kopieren.',
           ['CH-Instrumente']),
    'K2': ('Theodor Heuss nannte die Volksgesetzgebung bei der Arbeit am Grundgesetz '
           '1948/49 „eine Prämie für jeden Demagogen“.',
           []),
    'K3': ('Beim Volksentscheid „Proposition 22“ in Kalifornien gaben Uber, Lyft und '
           'andere Firmen 2020 rund 200 Millionen Dollar aus.',
           ['B-Prop22']),
    'K4': ('Beim Brexit 2016 war offen, wie der EU-Austritt genau aussehen sollte.',
           ['B-Brexit']),
    'K5': ('In der Schweiz stimmte 2009 eine Mehrheit für ein Verbot neuer Minarette.',
           ['B-Minarett']),
    'K6': ('Beim Berliner Volksentscheid 2021 stimmten 57,6 Prozent dafür – danach '
           'prüfte eine Expertenkommission erst, wie es umgesetzt werden kann.',
           ['B-DW', 'B-CH-Masseneinwanderung', 'B-Hamburg', 'B-Berlin-Klima']),
    'K7': ('Eine Übersicht über 67 Studien findet im Durchschnitt nur kleine positive '
           'Wirkungen auf Wissen, Teilnahme und Vertrauen.',
           ['B-Uebersicht-2024']),
    'K8': ('Eine Studie zu 43 Schweizer Abstimmungen zeigt: Frühere Teilnahme, '
           'Interesse, Bildung und soziale Klasse spielen eine Rolle.',
           ['B-Studie-2023']),
    'K9': ('In Schweizer Untersuchungen fühlten sich viele Stimmberechtigte nicht '
           'ausreichend informiert. Viele Vorlagen können überfordern.',
           ['B-CH-Alltag']),
}


# ---------------------------------------------------------------------------
# Umbau 15.09.2026 abends - Auswahlaufgabe statt Schreibaufgabe
# Je Argument vier Erwiderungen, eine pro Technik. Alle vier sind brauchbare
# Konter; sie unterscheiden sich nur in der Technik. Die App gibt eine Technik
# vor, die Schueler:innen waehlen die passende Erwiderung.
#
# Regeln beim Schreiben:
# - Keine Satzanfaenge aus dem Tippkasten der Rollenkarte ("Das spricht auch
#   fuer uns, weil", "Das stimmt nur, wenn", "Das stimmt, aber das Problem
#   bleibt", "Uns ist ... wichtiger, weil") - sonst erkennt man die Technik am
#   Satzanfang statt am Inhalt.
# - Einschraenken = das Argument gilt nur unter einer Bedingung / nur fuer
#   einen Teil. Entkraeften = Beleg oder Begruendung tragen nicht.
# - Nur Fakten aus wissensbasis.md.
# - "abgeleitet": True heisst, die Deutung steht so nicht woertlich in der
#   Wissensbasis (keine neuen Fakten, aber eigene Schlussfolgerung).
#
# Hintergrund je Erwiderung: "belege" (Schluessel in BELEGE), "kriterium"
# (Schluessel in KRITERIEN_INFO), "argumente" (IDs aus ARGUMENTE).
# ---------------------------------------------------------------------------

TECHNIK_REIHE = ['anders deuten', 'einschraenken', 'entkraeften', 'gewichten']

BELEGE['Ausgestaltung'] = (
    'Bessere Regeln für Volksentscheide',
    'Viele Einwände richten sich gegen eine schlechte Ausgestaltung. Mögliche '
    'Regeln: eine klare Frage mit rechtlicher Vorprüfung, ein amtliches '
    'Informationsheft mit Pro und Kontra, Quorum und Fristen, Offenlegung von '
    'Spenden und Kampagnenkosten, Schutz der Grundrechte. Solche Regeln '
    'verringern Risiken, beseitigen sie aber nicht vollständig.')
BELEGE['Weimar'] = (
    'Volksentscheide in der Weimarer Republik',
    'Hitler kam über die repräsentative Demokratie an die Macht: Das '
    'Ermächtigungsgesetz beschlossen gewählte Abgeordnete, nicht das Volk. Auf '
    'Reichsebene gab es in der ganzen Weimarer Zeit nur wenige, folgenlose '
    'Volksbegehren (Lübbe-Wolff 2023).')

# Wissensbasis Abschnitt 4 - Leitfrage und Kurzerklaerung
KRITERIEN_INFO = {
    'Partizipation': (
        'Wie gut können sich alle Bürger, auch Minderheiten, politisch einbringen?',
        'Umfasst Wahlen, Abstimmungen und andere Mitwirkung. Entscheidend ist '
        'nicht nur, ob Beteiligung erlaubt ist, sondern ob sie zugänglich ist und '
        'tatsächlich Einfluss ermöglicht.'),
    'Politische Gleichheit': (
        'Wie gleichberechtigt können alle Bürger, auch Minderheiten, politischen '
        'Einfluss nehmen?',
        'Bildung, Einkommen, Zeit oder finanzielle Macht dürfen nicht dazu führen, '
        'dass einige Gruppen dauerhaft stärker gehört werden.'),
    'Transparenz': (
        'Wie nachvollziehbar sind politische Entscheidungen?',
        'Bürger sollen erkennen, wer entscheidet, welche Argumente zählen und wer '
        'Kampagnen bezahlt.'),
    'Responsivität': (
        'Wie gut berücksichtigt Politik die Bürgerinteressen?',
        'Politik muss nicht jede Forderung erfüllen, soll aber reagieren und ihre '
        'Entscheidung begründen.'),
    'Öffentlichkeit': (
        'Wie offen werden politische Fragen diskutiert?',
        'Unterschiedliche Positionen sollen sichtbar sein, damit Bürger Argumente '
        'vergleichen können.'),
    'Politischer Wettbewerb': (
        'Wie fair konkurrieren politische Alternativen?',
        'Setzt echte Alternativen und faire Regeln voraus.'),
    'Entscheidungsqualität': (
        'Wie gut durchdacht sind politische Entscheidungen?',
        'Nutzt zuverlässige Informationen, berücksichtigt verschiedene Interessen, '
        'bedenkt Folgen.'),
    'Problemlösungsfähigkeit': (
        'Wie wirksam löst Politik gesellschaftliche Probleme?',
        'Eine schnelle oder beliebte Entscheidung ist nicht automatisch wirksam.'),
    'Regierungsfähigkeit': (
        'Wie gut kann Politik entscheiden und handeln?',
        'Bedeutet nicht, ohne Beratung besonders schnell zu entscheiden.'),
    'Umsetzbarkeit': (
        'Wie gut lassen sich Entscheidungen umsetzen?',
        'Muss rechtlich erlaubt, finanzierbar und organisatorisch durchführbar sein.'),
    'Gemeinwohlorientierung': (
        'Wie gut dient die Entscheidung der Allgemeinheit und berücksichtigt dabei '
        'Minderheiten?',
        'Gemeinwohl ist nicht nur der Wunsch der Mehrheit.'),
}


def _e(text, belege=(), kriterium='', argumente=(), abgeleitet=False):
    return {'text': text, 'belege': list(belege), 'kriterium': kriterium,
            'argumente': list(argumente), 'abgeleitet': abgeleitet}


ERWIDERUNGEN = {
    # ---------------- Pro-Argumente -> Erwiderungen der Kontra-Seite ----------
    'P1': {
        'anders deuten': _e(
            'Dass in der Schweiz regelmäßig abgestimmt wird, kann man auch '
            'anders sehen: So viele Vorlagen können überfordern. In Schweizer '
            'Untersuchungen fühlten sich viele nicht ausreichend informiert.',
            belege=['B-CH-Alltag'], argumente=['K9']),
        'einschraenken': _e(
            'Mehr Einfluss bekommen vor allem die, die tatsächlich abstimmen gehen. '
            'Das sind häufiger Menschen mit mehr Bildung, Zeit und politischem '
            'Interesse.',
            belege=['B-Studie-2023'], argumente=['K8']),
        'entkraeften': _e(
            'Ein Recht zum Abstimmen allein ist noch keine echte Beteiligung. '
            'Partizipation heißt, dass alle Zugang haben und wirklich Einfluss '
            'nehmen können.',
            kriterium='Partizipation', argumente=['K8']),
        'gewichten': _e(
            'Mitentscheiden ist ein Gewinn. Schwerer wiegt aber, dass Entscheidungen '
            'gut durchdacht sind – und dafür braucht es Zeit, Fachwissen und '
            'Beratung.',
            kriterium='Entscheidungsqualität', argumente=['K9']),
    },
    'P2': {
        'anders deuten': _e(
            'Die kleinen Effekte aus der Übersicht von 2024 kann man auch '
            'anders lesen: Ob Menschen Entscheidungen akzeptieren, hängt '
            'offenbar stark von anderen Dingen ab – etwa von fairen Ergebnissen'
            ' und glaubwürdiger Politik.',
            belege=['B-Uebersicht-2024'], argumente=['K7'], abgeleitet=True),
        'einschraenken': _e(
            'Akzeptanz kann wachsen, aber nicht bei allen. Wer sich schlecht '
            'informiert fühlt, kann nach der Abstimmung sogar enttäuschter '
            'sein.',
            argumente=['K7']),
        'entkraeften': _e(
            'Dass die eigene Stimme gezählt wurde, tröstet nicht automatisch: '
            'Wer bei Abstimmungen oft verliert, kann sogar enttäuschter werden.',
            argumente=['K7']),
        'gewichten': _e(
            'Akzeptanz ist wichtig. Mehr zählt aber, ob eine Entscheidung das '
            'Problem wirklich löst – eine beliebte Entscheidung ist nicht '
            'automatisch wirksam.',
            kriterium='Problemlösungsfähigkeit'),
    },
    'P3': {
        'anders deuten': _e(
            'Dass Bürger vor jeder Abstimmung offizielle Erläuterungen '
            'bekommen, kann man auch so sehen: Die Vorlagen sind oft schwierig '
            'und können Menschen überfordern.',
            belege=['B-CH-Alltag'], argumente=['K9']),
        'einschraenken': _e(
            'Von der Debatte haben vor allem Menschen etwas, die Zeit, Fachwissen '
            'und gute Sprachkenntnisse mitbringen. Bei allen anderen kommt davon '
            'weniger an.',
            argumente=['K9']),
        'entkraeften': _e(
            'Viel Aufmerksamkeit heißt noch nicht, dass fair diskutiert wird. Teure '
            'Kampagnen können die Debatte bestimmen – bei Proposition 22 gaben '
            'Firmen rund 200 Millionen Dollar aus.',
            belege=['B-Prop22'], argumente=['K3']),
        'gewichten': _e(
            'Offene Debatten sind ein Plus. Schwerer wiegt eine sachliche Abwägung – '
            'und die geht bei lauten, emotionalen Kampagnen leicht unter.',
            kriterium='Entscheidungsqualität', argumente=['K2']),
    },
    'P4': {
        'anders deuten': _e(
            'Dass so viele Regeln nötig sind – Vorprüfung, Informationsheft, '
            'Offenlegung –, kann man auch als Warnzeichen sehen: Ohne diese Regeln '
            'sind Volksentscheide offenbar sehr anfällig.',
            belege=['Ausgestaltung'], abgeleitet=True),
        'einschraenken': _e(
            'Klare Regeln machen vor allem sichtbar, wer zahlt und worum es '
            'geht. Ob alle die Informationen auch verstehen, hängt weiter von '
            'Bildung, Zeit und Sprachkenntnissen ab.',
            argumente=['K9']),
        'entkraeften': _e(
            'Offenlegung macht Geld sichtbar, nimmt ihm aber nicht seinen Einfluss. '
            'Teure Werbung erreicht trotzdem mehr Menschen.',
            belege=['B-Prop22'], argumente=['K3']),
        'gewichten': _e(
            'Klare Informationen sind gut. Entscheidender ist, ob eine schwierige '
            'Frage gut gelöst wird – und auf dem Stimmzettel gibt es nur Ja oder '
            'Nein, keinen Kompromiss.',
            kriterium='Entscheidungsqualität', argumente=['K4']),
    },
    'P5': {
        'anders deuten': _e(
            'Der Brexit zeigt auch die Kehrseite: Ein einziges Abstimmungsergebnis '
            'kann ein Land festlegen, obwohl danach noch viele Fragen offen sind.',
            belege=['B-Brexit'], argumente=['K4']),
        'einschraenken': _e(
            'Korrigieren klappt vor allem, wenn Bürger selbst neue Initiativen '
            'starten dürfen. Bei Abstimmungen, die von oben angesetzt werden, fehlt '
            'dieser Weg.',
            belege=['B-Brexit']),
        'entkraeften': _e(
            'Eine neue Abstimmung behebt die eigentliche Schwäche nicht: Auch beim '
            'zweiten Mal gibt es nur Ja oder Nein, keinen ausgehandelten Kompromiss.',
            argumente=['K4']),
        'gewichten': _e(
            'Fehler korrigieren zu können, ist gut. Für uns zählt mehr, dass Politik '
            'verlässlich handeln kann – ständig neue Abstimmungen machen Planung '
            'unsicher.',
            kriterium='Regierungsfähigkeit', argumente=['K1']),
    },
    'P6': {
        'anders deuten': _e(
            '„Parlament und Regierung müssen reagieren“ kann man auch anders '
            'verstehen: Reagieren heißt nicht zustimmen – die Politik kann die '
            'Forderung auch begründet ablehnen.',
            kriterium='Responsivität'),
        'einschraenken': _e(
            'Gleichberechtigter wird nur die Tagesordnung. Bei den Ergebnissen haben '
            'Menschen mit höherem Einkommen und mehr Bildung laut der Studie '
            'weiterhin einen Vorteil.',
            belege=['B-Studie-2026']),
        'entkraeften': _e(
            'Auch finanzstarke Gruppen nutzen Volksentscheide: Bei Proposition '
            '22 gaben Firmen rund 200 Millionen Dollar aus, und ihre Seite '
            'gewann. Um Bürgerinteressen ging es dabei nicht unbedingt.',
            belege=['B-Prop22'], argumente=['K3']),
        'gewichten': _e(
            'Neue Themen auf der Tagesordnung sind gut. Am Ende zählt aber mehr, ob '
            'sich die Entscheidung umsetzen lässt – rechtlich, finanziell und '
            'praktisch.',
            kriterium='Umsetzbarkeit', argumente=['K6']),
    },
    'P7': {
        'anders deuten': _e(
            'Ein Veto kann man auch als Bremse sehen: Beschlossene Gesetze können '
            'immer wieder gestoppt werden, und Regierung und Parlament planen dann '
            'unsicherer.',
            argumente=['K1']),
        'einschraenken': _e(
            'Wirksam ist das Veto nur für Gruppen, die in kurzer Zeit genug '
            'Unterschriften sammeln können – in der Schweiz 50.000 in 100 '
            'Tagen.',
            belege=['CH-Instrumente']),
        'entkraeften': _e(
            'Stoppen ist noch keine gute Kontrolle: Beim Referendum können Bürger '
            'ein Gesetz nur ablehnen, aber nicht beraten oder verbessern.',
            argumente=['K4']),
        'gewichten': _e(
            'Kontrolle durch die Bürger ist wichtig. Schwerer wiegt, dass Regierung '
            'und Parlament handeln können – gerade bei dringenden Problemen.',
            kriterium='Regierungsfähigkeit', argumente=['K1']),
    },
    'P8': {
        'anders deuten': _e(
            'Die Drohung mit einer Abstimmung kann man auch als Blockade sehen: Aus '
            'Sorge vor einem Referendum werden schwierige Gesetze vielleicht gar '
            'nicht erst beschlossen.',
            argumente=['K1'], abgeleitet=True),
        'einschraenken': _e(
            'Die frühe Kompromisssuche ist für die Schweiz mit ihrer starken '
            'Kompromisskultur beschrieben. Wo diese Kultur fehlt, ist nicht '
            'sicher, dass die Drohung Kompromisse bringt.',
            belege=['CH-Instrumente'], argumente=['K1']),
        'entkraeften': _e(
            'Ein Kompromiss ist nicht automatisch die bessere Lösung. Dass mehr '
            'Gruppen beteiligt sind, sagt noch nichts darüber, ob das Problem '
            'gelöst wird.',
            argumente=['K1']),
        'gewichten': _e(
            'Frühe Kompromisse sind ein Plus. Schwerer wiegt für uns die '
            'politische Gleichheit: Einkommen, Bildung oder Geld dürfen nicht '
            'entscheiden, welche Gruppen stärker gehört werden.',
            kriterium='Politische Gleichheit'),
    },
    'P9': {
        'anders deuten': _e(
            'Dass eine Initiative eine einzelne Frage herauslöst, kann man auch als '
            'Nachteil sehen: Zusammenhänge mit anderen Themen gehen dabei verloren.',
            argumente=['K1'], abgeleitet=True),
        'einschraenken': _e(
            'Eine faire Chance haben Vorschläge nur, wenn beide Seiten ähnlich viel '
            'Geld für Werbung haben. Sonst ist im Vorteil, wer mehr ausgeben kann.',
            belege=['B-Prop22'], argumente=['K3']),
        'entkraeften': _e(
            '„Ohne große Partei“ heißt nicht ohne starke Unterstützung: Eine '
            'Volksinitiative braucht in der Schweiz 100.000 Unterschriften in '
            '18 Monaten.',
            belege=['CH-Instrumente']),
        'gewichten': _e(
            'Mehr Auswahl ist gut. Entscheidender ist, dass eine Frage gründlich '
            'beraten wird – bei einer einzelnen Ja-Nein-Frage fehlt der Kompromiss.',
            kriterium='Entscheidungsqualität', argumente=['K4']),
    },
    'P10': {
        'anders deuten': _e(
            'Dass vor allem mittlere Gruppen profitieren, kann auch heißen: '
            'Menschen mit wenig Einkommen und wenig Bildung haben davon nicht '
            'unbedingt etwas.',
            belege=['B-Studie-2026'], abgeleitet=True),
        'einschraenken': _e(
            'Etwas gleichberechtigter wird nur die Tagesordnung. Bei den Ergebnissen '
            'bleibt der Vorteil für Menschen mit höherem Einkommen und mehr Bildung.',
            belege=['B-Studie-2026']),
        'entkraeften': _e(
            'Eine gleichere Tagesordnung macht das Abstimmen selbst nicht '
            'gleicher: In der Schweiz hängt die Teilnahme von früherer '
            'Teilnahme, Interesse, Bildung und sozialer Klasse ab.',
            belege=['B-Studie-2023'], argumente=['K8']),
        'gewichten': _e(
            'Eine offenere Tagesordnung ist ein Plus. Schwerer wiegt, ob die '
            'Entscheidungen gut durchdacht sind – dafür braucht es Zeit und '
            'Fachwissen, und die sind ungleich verteilt.',
            kriterium='Entscheidungsqualität', argumente=['K9']),
    },

    # ---------------- Kontra-Argumente -> Erwiderungen der Pro-Seite ----------
    'K1': {
        'anders deuten': _e(
            'Dass Gesetze gestoppt werden können, kann man auch als Vorteil '
            'sehen: Regierung und Parlament beziehen betroffene Gruppen dann '
            'früher ein und suchen Kompromisse.',
            belege=['CH-Instrumente'], argumente=['P8']),
        'einschraenken': _e(
            'Ein Referendum kommt nur zustande, wenn genug Menschen es '
            'verlangen – in der Schweiz 50.000 Unterschriften in 100 Tagen oder'
            ' acht Kantone.',
            belege=['CH-Instrumente'], argumente=['P7']),
        'entkraeften': _e(
            'Regierungsfähig heißt nicht, besonders schnell zu entscheiden. Gute '
            'Politik braucht Beratung, auch wenn das länger dauert.',
            kriterium='Regierungsfähigkeit'),
        'gewichten': _e(
            'Verlässliches Regieren ist wichtig. Mehr zählt für uns, dass die Politik '
            'auf die Bürger hört – und das muss sie, wenn Bürger ein Gesetz stoppen '
            'können.',
            kriterium='Responsivität', argumente=['P7']),
    },
    'K2': {
        'anders deuten': _e(
            'Den Satz von Theodor Heuss kann man auch als Misstrauen gegenüber den '
            'Bürgern lesen – nicht als Beweis, dass Volksentscheide gefährlich sind.',
            abgeleitet=True),
        'einschraenken': _e(
            'Stimmungsmacher haben es vor allem leicht, wenn sachliche Informationen '
            'fehlen. Mit einem amtlichen Informationsheft und klaren Regeln wird das '
            'schwerer.',
            belege=['Ausgestaltung'], argumente=['P4']),
        'entkraeften': _e(
            'Die Warnung von Heuss ist historisch überzogen: Hitler kam über '
            'gewählte Abgeordnete an die Macht, nicht über das Volk. In der '
            'Weimarer Zeit gab es auf Reichsebene nur wenige, folgenlose '
            'Volksbegehren.',
            belege=['Weimar']),
        'gewichten': _e(
            'Die Gefahr durch Stimmungsmacher ist ernst. Schwerer wiegt aber, dass '
            'Bürger sich überhaupt selbst einbringen können – sonst entscheiden '
            'immer nur andere für sie.',
            kriterium='Partizipation', argumente=['P1']),
    },
    'K3': {
        'anders deuten': _e(
            'Dass man die 200 Millionen Dollar bei Proposition 22 kennt, zeigt auch: '
            'Wer hinter einer Kampagne steckt, kann öffentlich sichtbar werden.',
            belege=['B-Prop22'], argumente=['P4'], abgeleitet=True),
        'einschraenken': _e(
            'Geld hat vor allem dann großen Einfluss, wenn es keine '
            'Kampagnenregeln gibt. Mit Grenzen für Spenden und Kampagnen lässt '
            'sich dieser Einfluss verkleinern.',
            belege=['Ausgestaltung'], argumente=['P6']),
        'entkraeften': _e(
            'Geld wirkt nicht nur bei Volksentscheiden, sondern auch im Wettbewerb '
            'der Parteien. Das Argument spricht also nicht speziell gegen '
            'Volksentscheide.',
            argumente=['P9']),
        'gewichten': _e(
            'Der Einfluss von Geld ist ein Problem. Für uns zählt mehr, dass Bürger '
            'eigene Themen einbringen können, die die Politik sonst liegen lässt.',
            kriterium='Responsivität', argumente=['P6']),
    },
    'K4': {
        'anders deuten': _e(
            'Den Brexit kann man auch anders lesen: Das Problem war nicht das Ja '
            'oder Nein, sondern dass es keinen Weg gab, das Ergebnis später zu '
            'korrigieren.',
            belege=['B-Brexit'], argumente=['P5']),
        'einschraenken': _e(
            'Zu stark vereinfacht wird vor allem, wenn die Frage unklar ist. Mit '
            'einer klaren Frage und einer Vorprüfung lässt sich das verringern.',
            belege=['Ausgestaltung'], argumente=['P4']),
        'entkraeften': _e(
            'Ein Kompromiss ist trotzdem möglich – schon vor der Abstimmung: '
            'Bei „Rettet die Bienen“ übernahm der bayerische Landtag die '
            'Forderung mit einem Begleitgesetz, und ein Volksentscheid fand gar'
            ' nicht statt.',
            belege=['B-Bienen'], argumente=['P8']),
        'gewichten': _e(
            'Einfache Fragen haben Nachteile. Mehr zählt für uns, dass die Politik '
            'erfährt, was die Bürger wollen – ein klares Ja oder Nein zeigt das '
            'deutlich.',
            kriterium='Responsivität', abgeleitet=True),
    },
    'K5': {
        'anders deuten': _e(
            'Dass eine Mehrheit über Minderheitenfragen entscheidet, kann '
            'Rechte auch ausweiten: In Irland führte eine Volksabstimmung 2015 '
            'die Ehe für alle ein.',
            belege=['B-Irland']),
        'einschraenken': _e(
            'Gefährlich wird es vor allem, wenn Grundrechte nicht geschützt sind. '
            'Werden Fragen vorher rechtlich geprüft, setzt das der Mehrheit Grenzen.',
            belege=['Ausgestaltung']),
        'entkraeften': _e(
            'Das Problem haben nicht nur Volksentscheide: Auch gewählte '
            'Parlamente treffen manchmal Entscheidungen gegen Minderheiten.',
            belege=['Minderheiten-Parlament']),
        'gewichten': _e(
            'Die Gefahr für Minderheiten ist ernst. Schwerer wiegt für uns, '
            'dass Politik auf die Bürger hört – mit Volksentscheiden kann sie '
            'wichtige Themen nicht einfach liegen lassen.',
            kriterium='Responsivität', argumente=['P6']),
    },
    'K6': {
        'anders deuten': _e(
            'Die Expertenkommission nach dem Berliner Volksentscheid kann man auch '
            'positiv sehen: Das klare Votum hat die Politik gezwungen, das Thema '
            'ernsthaft zu prüfen.',
            belege=['B-DW']),
        'einschraenken': _e(
            'Schwierig wird die Umsetzung vor allem, wenn Kosten und '
            'Rechtsfragen erst nach der Abstimmung geprüft werden. Werden sie '
            'vorher geprüft, wird dieses Risiko kleiner.',
            belege=['Ausgestaltung']),
        'entkraeften': _e(
            'Ein Votum kann schon eine fertige Lösung sein: Beim Hamburger '
            'Zukunftsentscheid 2025 stimmten die Bürger über ein Gesetz ab, und'
            ' dieses Gesetz gilt jetzt.',
            belege=['B-Hamburg']),
        'gewichten': _e(
            'Die Umsetzung kann schwierig sein. Mehr zählt, dass Bürger ein Thema '
            'selbst auf die Tagesordnung bringen können, das die Politik sonst '
            'vermeiden würde.',
            kriterium='Responsivität', argumente=['P6']),
    },
    'K7': {
        'anders deuten': _e(
            'Die Übersicht über 67 Studien kann man auch so lesen: Die Wirkungen auf '
            'Vertrauen und Wissen sind klein, aber sie sind positiv.',
            belege=['B-Uebersicht-2024'], argumente=['P2']),
        'einschraenken': _e(
            'Enttäuscht werden vor allem Menschen, die sich schlecht informiert '
            'fühlen. Kurze, verständliche Informationen vor der Abstimmung können '
            'das verringern.',
            belege=['Ausgestaltung'], argumente=['P3']),
        'entkraeften': _e(
            'Verlieren muss nicht enttäuschen: Bei Stuttgart 21 wurde das '
            'Ergebnis breit anerkannt und beendete einen langen Konflikt.',
            belege=['B-S21']),
        'gewichten': _e(
            'Mehr Vertrauen ist nicht garantiert. Mehr zählt, dass Bürger '
            'mitentscheiden können – ein faires Verfahren ist schon für sich ein '
            'Gewinn.',
            kriterium='Partizipation', argumente=['P2']),
    },
    'K8': {
        'anders deuten': _e(
            'Dass vor allem Bessergestellte abstimmen, kann man auch als Auftrag '
            'sehen: Es braucht leichtere Zugänge und verständliche Informationen – '
            'nicht weniger Mitbestimmung.',
            argumente=['P1'], abgeleitet=True),
        'einschraenken': _e(
            'Die Ungleichheit ist nicht bei jeder Abstimmung gleich stark – das'
            ' zeigt dieselbe Studie zu 43 Schweizer Abstimmungen.',
            belege=['B-Studie-2023']),
        'entkraeften': _e(
            'Ungleichen Einfluss gibt es auch im Parlament: Laut einer Studie von '
            '2026 greifen Initiativen die Themen mittlerer Gruppen sogar besser auf '
            'als Parlamente.',
            belege=['B-Studie-2026'], argumente=['P10']),
        'gewichten': _e(
            'Ungleiche Beteiligung ist ein Problem. Schwerer wiegt aber, dass Bürger '
            'zwischen den Wahlen überhaupt direkt mitentscheiden können.',
            kriterium='Partizipation', argumente=['P1']),
    },
    'K9': {
        'anders deuten': _e(
            'Dass sich viele nicht ausreichend informiert fühlen, kann man auch'
            ' positiv sehen: Die Menschen merken, dass sie mehr wissen wollen, '
            'bevor sie entscheiden.',
            belege=['B-CH-Alltag'], abgeleitet=True),
        'einschraenken': _e(
            'Ungleiche Wissenschancen gibt es vor allem, wenn Informationen schwer '
            'verständlich sind. Kurze, barrierefreie Erklärungen können die Lücken '
            'verkleinern.',
            belege=['Ausgestaltung'], argumente=['P3']),
        'entkraeften': _e(
            'Volksentscheide können Wissen sogar vergrößern: Eine Übersicht über 67 '
            'Studien findet kleine positive Wirkungen auf das Wissen der Bürger.',
            belege=['B-Uebersicht-2024']),
        'gewichten': _e(
            'Ungleiches Wissen ist ein Problem. Mehr zählt, dass politische Fragen '
            'offen diskutiert werden – dabei lernen viele Menschen dazu.',
            kriterium='Öffentlichkeit', argumente=['P3']),
    },
}


def technik_beutel_neu(letzte: str = '') -> list:
    """Die vier Techniken in zufaelliger Reihenfolge, ohne direkte Wiederholung
    an der Nahtstelle zum vorigen Durchgang. Es wird von hinten gezogen (pop)."""
    import random
    beutel = TECHNIK_REIHE[:]
    random.shuffle(beutel)
    if letzte and beutel[-1] == letzte:
        beutel[0], beutel[-1] = beutel[-1], beutel[0]
    return beutel

BELEGE['B-Frauenstimmrecht'] = (
    'Schweiz, Frauenstimmrecht 1971',
    'Am 7. Februar 1971 stimmten rund zwei Drittel mit Ja. Frauen erhielten das '
    'nationale Stimmrecht; im Kanton Appenzell Innerrhoden erst 1990 nach einem '
    'Gerichtsurteil.')

BELEGE['Minderheiten-Parlament'] = (
    'Auch Parlamente entscheiden gegen Minderheiten',
    'Auch gewählte Parlamente treffen manchmal Entscheidungen gegen Minderheiten – '
    'die Gefahr ist nicht allein ein Problem direkter Demokratie. Grundrechte und '
    'Gerichte begrenzen die Ergebnisse in beiden Fällen (Lübbe-Wolff 2023).')
