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
