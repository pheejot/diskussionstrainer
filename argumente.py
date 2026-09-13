"""Feste Inhalte aus dem Materialpool-Vault.

Die IDs (P1-P10, K1-K9) sind die Schnittstelle zur KI und zur Wissensbasis.
Bei Aenderungen am Vault muessen sie stabil bleiben.
"""

TECHNIKEN = {
    'anders deuten': {
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
        'leitfrage': 'Wann stimmt das Argument – und wann nicht?',
        'erklaerung': (
            'Du gibst zu, dass das Argument stimmt – aber nur unter bestimmten '
            'Bedingungen. Du nennst die Grenze.'
        ),
        'beispiel': 'Debatten können Wissen erhöhen, aber nicht bei allen gleich.',
    },
    'entkraeften': {
        'leitfrage': 'Warum überzeugt das Argument nicht vollständig?',
        'erklaerung': (
            'Du zeigst eine echte Schwachstelle: Der Beleg passt nicht, die '
            'Begründung trägt nicht, oder die Folgerung stimmt so nicht. '
            'Widersprechen allein reicht nicht.'
        ),
        'beispiel': 'Transparenz zeigt viel Geld, beseitigt seinen Einfluss aber nicht.',
    },
    'gewichten': {
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

# id, seite, titel, behauptung, begruendung
ARGUMENTE = [
    ('P1', 'pro', 'Mehr direkte Mitentscheidung',
     'Bundesweite Volksentscheide stärken die Beteiligung.',
     'Bürger wählen dann nicht nur Parteien. Sie entscheiden auch selbst über '
     'konkrete Sachfragen und haben zwischen Wahlen direkten Einfluss.'),
    ('P2', 'pro', 'Mitentscheidung kann Akzeptanz stärken',
     'Wer mitentscheiden kann, akzeptiert politische Entscheidungen eher.',
     'Ein faires Verfahren zeigt: Meine Stimme wurde gezählt. Das kann auch dann '
     'wichtig sein, wenn die eigene Seite verliert.'),
    ('P3', 'pro', 'Volksentscheide fördern öffentliche Debatten',
     'Vor Volksentscheiden wird öffentlich über Sachfragen gesprochen.',
     'Initiativen, Parteien, Medien und Bürger erklären ihre Position. Eine '
     'konkrete Abstimmungsfrage schafft Aufmerksamkeit.'),
    ('P4', 'pro', 'Klare Informationen und Regeln sind möglich',
     'Volksentscheide können transparent und fair gestaltet werden.',
     'Der Staat kann die Frage prüfen, Pro und Kontra erklären und '
     'Kampagnengelder offenlegen.'),
    ('P5', 'pro', 'Bürger können eigene Fehler korrigieren',
     'Direkte Demokratie kann eigene Entscheidungen später wieder korrigieren.',
     'Wenn Bürger selbst abstimmen dürfen, können sie eine frühere Entscheidung '
     'mit einer neuen Abstimmung ändern.'),
    ('P6', 'pro', 'Bürgerinteressen kommen auf die Agenda',
     'Volksinitiativen zwingen Politik, Bürgerinteressen ernst zu nehmen.',
     'Mit genügend Unterschriften können Bürger ein Thema auf die Tagesordnung '
     'bringen. Parlament und Regierung müssen darauf reagieren.'),
    ('P7', 'pro', 'Bürger können das Parlament kontrollieren',
     'Ein Referendum gibt Bürgern ein wirksames Veto.',
     'Bürger könnten ein beschlossenes Gesetz stoppen. Regierung und Parlament '
     'müssten deshalb früher erklären und Kompromisse suchen.'),
    ('P8', 'pro', 'Die Drohung einer Abstimmung fördert Kompromisse',
     'Direkte Demokratie kann Parlamente zu früheren Kompromissen bewegen.',
     'Wenn Bürger ein Gesetz später stoppen können, bezieht das Parlament '
     'betroffene Gruppen eher vorher ein.'),
    ('P9', 'pro', 'Mehr echte Alternativen im Wettbewerb',
     'Volksentscheide geben einzelnen Vorschlägen eine faire Chance.',
     'Parteien bündeln viele Themen zu einem Programm. Eine Volksinitiative löst '
     'eine einzelne Sachfrage heraus - auch ohne große Partei dahinter.'),
    ('P10', 'pro', 'Die Agenda wird etwas gleichberechtigter',
     'Volksinitiativen können Themen mittlerer Gruppen besser aufgreifen.',
     'Parlamente reagieren oft stärker auf gut vernetzte und wohlhabende Gruppen. '
     'Eine Initiative eröffnet einen zusätzlichen Weg.'),

    ('K1', 'kontra', 'Häufige Vetos können Politik blockieren',
     'Viele Referenden können Regieren langsamer und unsicherer machen.',
     'Beschlossene Gesetze könnten wieder gestoppt werden. Regierung und '
     'Parlament planen dann weniger sicher.'),
    ('K2', 'kontra', 'Volksentscheide können Demagogen nützen',
     'Laute Stimmungsmacher und einfache Parolen können zu viel Einfluss bekommen.',
     'Emotionale Kampagnen wirken vor großem Publikum stark. Eine ruhige, '
     'sachliche Abwägung tritt dann leicht zurück.'),
    ('K3', 'kontra', 'Geld beeinflusst Abstimmungskampagnen',
     'Finanzstarke Gruppen können die öffentliche Debatte dominieren.',
     'Teure Werbung erreicht viele Menschen. Schwächere Gruppen können ihre '
     'Gründe weniger sichtbar machen.'),
    ('K4', 'kontra', 'Komplexe Fragen werden auf Ja oder Nein verkürzt',
     'Eine Ja-Nein-Abstimmung kann schwierige Probleme zu stark vereinfachen.',
     'Im Parlament kann ein Entwurf beraten und verändert werden. Auf dem '
     'Stimmzettel gibt es nur Zustimmung oder Ablehnung.'),
    ('K5', 'kontra', 'Mehrheiten können Minderheiten überstimmen',
     'Volksentscheide können Interessen von Minderheiten gefährden.',
     'Eine Mehrheit entscheidet auch über Fragen, die vor allem eine kleine '
     'Gruppe betreffen. Die Mehrheit spürt die Nachteile vielleicht nicht selbst.'),
    ('K6', 'kontra', 'Ein Ergebnis löst die Umsetzung nicht',
     'Ein erfolgreiches Votum ist noch keine umsetzbare Lösung.',
     'Nach der Abstimmung bleiben Rechtsfragen, Kosten und Zuständigkeiten. Eine '
     'einfache Forderung kann viele schwierige Entscheidungen auslösen.'),
    ('K7', 'kontra', 'Vertrauen wächst nicht automatisch',
     'Volksentscheide lösen Unzufriedenheit mit Demokratie nicht automatisch.',
     'Vertrauen hängt auch von fairen Ergebnissen und glaubwürdiger Politik ab. '
     'Wer oft verliert, kann sogar enttäuschter werden.'),
    ('K8', 'kontra', 'Vor allem Bessergestellte stimmen ab',
     'Häufige Abstimmungen können politische Ungleichheit vergrößern.',
     'Menschen mit mehr Bildung, Zeit und politischem Interesse beteiligen sich '
     'häufiger. Gleiche Stimmzettel führen dann nicht zu gleichem Einfluss.'),
    ('K9', 'kontra', 'Wissen und Information sind ungleich verteilt',
     'Nicht alle Bürger können komplexe Vorlagen gleich gut prüfen.',
     'Politische Entscheidungen brauchen Zeit, Fachwissen und verständliche '
     'Informationen. Die sind ungleich verteilt.'),
]

ARGUMENT_NACH_ID = {a[0]: a for a in ARGUMENTE}


def argument_text(arg_id: str) -> str:
    """Der Wortlaut, der als Ausgangsargument an die KI geht."""
    _, _, _, behauptung, begruendung = ARGUMENT_NACH_ID[arg_id]
    return f'{behauptung} {begruendung}'
