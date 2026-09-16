"""Diskussionstrainer - vier Techniken zum Kontern (Auswahl-Fassung).

Selbstlernangebot zwischen B03 Teil 2 und der Fishbowl in B04.

Ablauf (Umbau 15.09.2026 abends):
Rolle -> Argument der Gegenseite -> zur vorgegebenen Technik die passende
Erwiderung antippen -> Aufloesung + freiwillig in eigenen Worten ->
naechstes Argument oder Uebertrag auf die Rollenkarte.

- Gaeste sehen nur die Argumente der Gegenseite. Moderationsteam und
  "ohne Rolle" bekommen einen Pro/Kontra-Umschalter.
- Die Technik wird ausgelost: alle vier kommen in zufaelliger Reihenfolge
  dran, bevor sich eine wiederholt.
- Alle vier Antworten sind brauchbare Konter, jede mit einer anderen Technik.
  Falsch getippt -> Hinweis, welche Technik das war, zweiter Versuch. Nach dem
  zweiten Fehlversuch wird aufgeloest.
- Zu Pool-Argumenten sind die vier Erwiderungen fest vorformuliert
  (argumente.ERWIDERUNGEN), ohne KI. Nur zu einem selbst geschriebenen
  Argument formuliert die KI die vier Erwiderungen (trainer.erwiderungen).
- Zum Argument und zu jeder Erwiderung gibt es aufklappbaren Hintergrund aus
  den geprueften Belegen der Wissensbasis.

Es wird nichts gespeichert. Kein Serverspeicher, keine Lehreruebersicht.
Die vorige Schreib-Fassung (mit Ampel-Feedback) liegt als Sicherung in alt/.
"""

import html
import os
import random
from datetime import date, datetime

import streamlit as st

import trainer
from glossar import markiere
from argumente import (ARGUMENTE, ARGUMENT_NACH_ID, BELEGE, ERWIDERUNGEN,
                       HINTERGRUND, KRITERIEN_INFO, KRITERIEN_PFAD, POOL_SEITEN,
                       ROLLEN, TECHNIKEN, TECHNIK_ANZEIGE, TECHNIK_REIHE,
                       argument_text, fuer_rolle_sortiert, gegenseite,
                       gegenstrang, technik_beutel_neu, typische_rollen,
                       vault_url)

LEITFRAGE = 'Sollten in Deutschland bundesweite Volksentscheide eingeführt werden?'
SITZUNGSLIMIT = 16          # KI-Antworten pro Schuelersitzung (nur eigene Argumente)
TAGESGRENZE = 400           # KI-Antworten pro Tag fuer die gesamte App
EIGENE_HERKUNFT = 'eigene Eingabe'

st.set_page_config(page_title='Diskussionstrainer', page_icon='🗣️', layout='centered')


# ---------------------------------------------------------------------------
# Darstellung
# ---------------------------------------------------------------------------

st.markdown(
    """
    <style>
      .block-container { padding-top: 2rem; padding-bottom: 4rem; max-width: 44rem; }
      .stButton > button {
          width: 100%; padding: .95rem 1rem; font-size: 1.12rem;
          font-weight: 600; border-radius: 12px; margin-bottom: .35rem;
      }
      textarea { font-size: 1.1rem !important; line-height: 1.5 !important; }
      .karte {
          border: 1px solid #D9E2F3; background: #F2F5FA; border-radius: 12px;
          padding: .9rem 1.1rem; margin: .6rem 0;
      }
      .karte .label {
          font-size: .78rem; letter-spacing: .06em; text-transform: uppercase;
          color: #5A6B85; margin-bottom: .3rem;
      }
      .karte .inhalt { font-size: 1.05rem; line-height: 1.5; color: #0F2C5C; }
      .ampel {
          display: flex; align-items: center; gap: .7rem;
          padding: .6rem .8rem; border-radius: 10px; margin-bottom: .4rem;
          background: #F7F9FC; border: 1px solid #E3E9F3;
      }
      .punkt { width: 1.15rem; height: 1.15rem; border-radius: 50%; flex: none; }
      .ampel .name { font-weight: 600; min-width: 8.5rem; color: #0F2C5C; }
      .ampel .wert { color: #5A6B85; font-size: .95rem; }
      .schrittzeile { color: #5A6B85; font-size: .85rem; margin-bottom: .2rem; }

      /* Verweise in den Materialpool - sehen aus wie Knoepfe, oeffnen aber
         einen neuen Tab, damit die Trainer-Sitzung erhalten bleibt. */
      a.poollink {
          display: block; text-decoration: none; text-align: left;
          border: 1px solid #4C94D8; background: #FFFFFF; color: #1F4E79;
          border-radius: 10px; padding: .7rem .9rem; margin-bottom: .4rem;
          font-weight: 600; font-size: 1.02rem; line-height: 1.35;
      }
      a.poollink:hover { background: #E3EDF9; }
      a.poollink .extern { float: right; color: #5A6B85; font-weight: 400; }

      /* Glossar: angetipptes Wort klappt eine Erklaerung auf.
         <details> ist ein natives HTML-Element - funktioniert auf dem iPad
         ohne JavaScript und ohne Hover. */
      /* inline-block statt inline: Chrome erzwingt hinter einem <details>
         sonst einen Zeilenumbruch, auch wenn die Zeile noch Platz hat.
         Beim Aufklappen wird daraus ein Block, damit die Erklaerung die
         volle Breite bekommt. */
      details.gl { display: inline-block; vertical-align: baseline; }
      details.gl[open] { display: block; margin: .15rem 0 .1rem 0; }
      details.gl > summary {
          display: inline; cursor: pointer; list-style: none;
          color: #1F4E79; font-weight: 600;
          border-bottom: 2px dotted #4C94D8;
      }
      details.gl > summary::-webkit-details-marker { display: none; }
      details.gl > summary::marker { content: ''; }
      /* kleines Fragezeichen: zeigt, dass man tippen kann */
      details.gl > summary::after {
          content: '?'; font-size: .62em; font-weight: 700;
          vertical-align: super; margin-left: .12em; color: #4C94D8;
      }
      details.gl[open] > summary { background: #E3EDF9; }
      details.gl[open] > summary::after { content: '×'; font-size: .8em;
          vertical-align: baseline; color: #5A6B85; }
      /* Im zugeklappten Zustand darf die Erklaerung KEINEN Platz belegen -
         sonst bricht der Satz an jedem Glossarwort um. */
      .gl-text { display: none; }
      details.gl[open] > .gl-text {
          display: block; margin: .25rem 0 .3rem 1.1rem;
          padding: .45rem .7rem;
          background: #FFFFFF; border-left: 4px solid #4C94D8;
          border-radius: 0 6px 6px 0;
          font-size: .93rem; line-height: 1.4; color: #3A4A63; font-weight: 400;
      }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
      .karte.technik { border: 2px solid #1F4E79; background: #FFFFFF; }
      .karte.richtig { border: 2px solid #2E7D32; background: #E8F3E9; }
      .karte.falsch  { border-color: #E6C4C4; background: #FBF3F3; opacity: .75; }
      .hinweis-falsch {
          color: #8E2A2A; font-size: .95rem; line-height: 1.4;
          margin: -.2rem 0 .7rem 0;
      }
      .zwischenraum { height: .6rem; }
    </style>
    """,
    unsafe_allow_html=True,
)


def karte(label: str, inhalt: str, glossar: bool = True, klasse: str = '',
          roh: bool = False):
    """Karte mit Label. Glossarwoerter werden automatisch antippbar.

    roh=True: Text stammt von Schueler:innen oder der KI und wird vorher
    HTML-maskiert.
    """
    if roh:
        inhalt = html.escape(inhalt)
    text = markiere(inhalt) if glossar else inhalt
    st.markdown(
        f'<div class="karte {klasse}"><div class="label">{label}</div>'
        f'<div class="inhalt">{text}</div></div>',
        unsafe_allow_html=True,
    )


def satz(inhalt: str, praefix: str = ''):
    """Fliesstext mit antippbaren Glossarwoertern."""
    if not inhalt:
        return
    st.markdown(f'<div class="inhalt">{praefix}{markiere(inhalt)}</div>',
                unsafe_allow_html=True)


def poollink(beschriftung: str, pfad: str):
    """Ein Verweis in den Materialpool. Oeffnet IMMER einen neuen Tab -
    sonst verlaesst der Schueler den Trainer und seine Sitzung ist weg."""
    st.markdown(
        f'<a class="poollink" href="{vault_url(pfad)}" target="_blank" '
        f'rel="noopener">{beschriftung}<span class="extern">↗</span></a>',
        unsafe_allow_html=True,
    )


def materialpool_block(arg_id: str = ''):
    """Aufklappbarer Bereich mit Verweisen in den Materialpool."""
    with st.expander('📖 Im Materialpool nachschlagen'):
        if arg_id and arg_id in ARGUMENT_NACH_ID:
            poollink('Dieses Argument im Materialpool',
                     ARGUMENT_NACH_ID[arg_id]['pfad'])
            gegen = gegenstrang(arg_id)
            if gegen:
                poollink(f'Was die Gegenseite sagt: {gegen[0]}', gegen[1])
        for schluessel in ('techniken', 'kriterien', 'ausgestaltung'):
            beschriftung, pfad = POOL_SEITEN[schluessel]
            poollink(beschriftung, pfad)
        st.caption('Öffnet sich in einem neuen Tab. Der Trainer bleibt offen – '
                   'wechsle einfach zurück.')


def hintergrund_block(arg_id: str = ''):
    """Hintergrund zu einem Pool-Argument - ohne KI, nur gepruefte Belege."""
    if arg_id not in HINTERGRUND:
        return
    belegsatz, faelle = HINTERGRUND[arg_id]
    with st.expander('🔎 Hintergrund zum Argument'):
        karte('📌 Kurz gesagt', belegsatz)
        for fall_id in faelle:
            titel, text = BELEGE[fall_id]
            karte(f'🗂️ {titel}', text)
        st.caption('Alle Angaben stammen aus dem Materialpool.')


def erwiderung_hintergrund(e: dict, titel: str):
    """Hintergrund zu einer Erwiderung: Belege, Kriterium, verwandtes Argument.

    Die Inhalte kommen immer aus argumente.py - auch bei KI-Erwiderungen
    liefert die KI nur die IDs.
    """
    belege = [b for b in e.get('belege', []) if b in BELEGE]
    krit = e.get('kriterium', '')
    argumente = [a for a in e.get('argumente', []) if a in ARGUMENT_NACH_ID]
    with st.expander(f'🔎 Hintergrund zu {titel}'):
        for b in belege:
            t, text = BELEGE[b]
            karte(f'🗂️ {t}', text)
        if krit in KRITERIEN_INFO:
            leitfrage, kurz = KRITERIEN_INFO[krit]
            karte(f'⚖️ Kriterium: {krit}',
                  f'{leitfrage}<br><span style="font-size:.95rem">{kurz}</span>',
                  glossar=False)
            if krit in KRITERIEN_PFAD:
                poollink(f'Mehr zum Kriterium {krit}', KRITERIEN_PFAD[krit])
        for a in argumente:
            karte(f'💬 Dazu passt das Argument: {ARGUMENT_NACH_ID[a]["titel"]}',
                  argument_text(a))
        if not (belege or krit in KRITERIEN_INFO or argumente):
            st.caption('Zu dieser Antwort gibt es keinen eigenen Beleg im '
                       'Materialpool. Sie arbeitet mit einer Begründung.')


# Rollen mit Artikel, fuer Saetze wie "Wenn die CDU sagt ..."
ROLLE_IM_SATZ = {
    'AfD': 'die AfD',
    'Mehr Demokratie e. V.': 'Mehr Demokratie',
    'CDU': 'die CDU',
    'Sozialverband': 'der Sozialverband',
}
ROLLE_KURZ = {'Mehr Demokratie e. V.': 'Mehr Demokratie'}


def arg_beschriftung(arg_id: str) -> str:
    """Titel plus die Gaesterolle, von der das Argument zu erwarten ist."""
    titel = ARGUMENT_NACH_ID[arg_id]['titel']
    namen = [ROLLE_KURZ.get(r, r) for r in typische_rollen(arg_id)]
    return f'{titel}  ({" / ".join(namen)})' if namen else titel


def kuerze(text: str, n: int = 90) -> str:
    return text if len(text) <= n else text[:n].rsplit(' ', 1)[0] + ' …'


def rollenkarten_zeile(d: dict) -> tuple:
    """(wer, was, technik, antwort) fuer den Uebertrag auf die Rollenkarte."""
    herkunft = d.get('herkunft', '')
    if herkunft in ARGUMENT_NACH_ID:
        namen = [ROLLE_IM_SATZ[r] for r in typische_rollen(herkunft)]
        wer = ' oder '.join(namen) if namen else 'die Gegenseite'
        was = ARGUMENT_NACH_ID[herkunft]['titel']
    else:
        wer, was = 'die Gegenseite', kuerze(d['argument'])
    antwort = d.get('eigene') or d['erwiderung']
    return wer, was, TECHNIK_ANZEIGE[d['technik']], antwort


# ---------------------------------------------------------------------------
# Zugang, Limits
# ---------------------------------------------------------------------------

def secret(name: str, standard: str = '') -> str:
    try:
        return str(st.secrets.get(name, os.getenv(name, standard)))
    except Exception:
        return os.getenv(name, standard)


@st.cache_resource
def tageszaehler() -> dict:
    """Gemeinsamer Zaehler fuer alle Sitzungen.

    Achtung: Streamlit Community Cloud startet den Container bei Inaktivitaet
    neu; dann faengt der Zaehler wieder bei null an. Als Missbrauchsbremse
    reicht das, als Abrechnung nicht.
    """
    return {'tag': date.today(), 'anzahl': 0}


def freigabe_offen() -> tuple:
    """(offen, meldung) - Fenster kommt aus den Secrets, Format JJJJ-MM-TT."""
    start, ende = secret('FREIGABE_START'), secret('FREIGABE_ENDE')
    heute = date.today()
    try:
        if start and heute < datetime.strptime(start, '%Y-%m-%d').date():
            return False, f'Der Trainer ist ab dem {_de(start)} freigeschaltet.'
        if ende and heute > datetime.strptime(ende, '%Y-%m-%d').date():
            return False, f'Der Trainer war bis zum {_de(ende)} freigeschaltet.'
    except ValueError:
        return True, ''      # unlesbares Datum sperrt niemanden aus
    return True, ''


def _de(iso: str) -> str:
    j, m, t = iso.split('-')
    return f'{t}.{m}.{j}'


def budget_frei() -> tuple:
    z = tageszaehler()
    if z['tag'] != date.today():
        z['tag'], z['anzahl'] = date.today(), 0
    if z['anzahl'] >= TAGESGRENZE:
        return False, ('Der Trainer hat heute sein Tageslimit erreicht. '
                       'Bitte morgen noch einmal versuchen.')
    if st.session_state.ki_aufrufe >= SITZUNGSLIMIT:
        return False, (f'Du hast die {SITZUNGSLIMIT} Rückmeldungen dieser Sitzung '
                       'aufgebraucht. Schließe jetzt ab - deine Ergebnisse bleiben '
                       'erhalten.')
    return True, ''


def zaehle():
    tageszaehler()['anzahl'] += 1
    st.session_state.ki_aufrufe += 1


# ---------------------------------------------------------------------------
# Zustand
# ---------------------------------------------------------------------------

STARTWERTE = {
    'freigeschaltet': False,
    'schritt': 'rolle',
    'rolle': 'ohne Rolle',
    'herkunft': '',
    'ausgangsargument': '',
    'erw': None,              # die vier Erwiderungen dieser Runde
    'technik': '',            # die ausgeloste Technik
    'reihenfolge': [],        # Reihenfolge der Antworten A-D
    'falsch': [],             # falsch angetippte Techniken
    'erfolg': '',             # 'erster' | 'zweiter' | 'aufgeloest'
    'runde': 0,
    'gesichert': False,
    'beutel': [],
    'letzte_technik': '',
    'verstaendnisfrage': '',
    'ki_aufrufe': 0,
    'durchgaenge': [],
    'fehler': '',
}

for k, v in STARTWERTE.items():
    if k not in st.session_state:
        st.session_state[k] = v.copy() if isinstance(v, (list, dict)) else v


def gehe_zu(schritt: str):
    st.session_state.schritt = schritt
    st.rerun()


def starte_runde(herkunft: str, argument: str, erw: dict):
    """Technik auslosen, Antworten mischen, zur Auswahl wechseln."""
    if not st.session_state.beutel:
        st.session_state.beutel = technik_beutel_neu(st.session_state.letzte_technik)
    technik = st.session_state.beutel.pop()
    reihenfolge = TECHNIK_REIHE[:]
    random.shuffle(reihenfolge)
    st.session_state.letzte_technik = technik
    st.session_state.technik = technik
    st.session_state.reihenfolge = reihenfolge
    st.session_state.herkunft = herkunft
    st.session_state.ausgangsargument = argument
    st.session_state.erw = erw
    st.session_state.falsch = []
    st.session_state.erfolg = ''
    st.session_state.gesichert = False
    st.session_state.runde += 1
    st.session_state.fehler = ''
    gehe_zu('auswahl')


def technik_zuruecklegen():
    """Beim Abbruch einer Runde kommt die Technik zurueck in den Beutel."""
    if st.session_state.technik and st.session_state.erfolg == '':
        st.session_state.beutel.append(st.session_state.technik)
        st.session_state.technik = ''


def sichere_durchgang():
    if st.session_state.gesichert or not st.session_state.erw:
        return
    runde = st.session_state.runde
    st.session_state.durchgaenge.append({
        'herkunft': st.session_state.herkunft,
        'argument': st.session_state.ausgangsargument,
        'technik': st.session_state.technik,
        'erwiderung': st.session_state.erw[st.session_state.technik]['text'],
        'eigene': st.session_state.get(f'eigene_{runde}', '').strip(),
        'erfolg': st.session_state.erfolg,
    })
    st.session_state.gesichert = True


def ki_client():
    """None, wenn kein Schluessel hinterlegt ist."""
    key = secret('OPENAI_API_KEY')
    return trainer.client_from_key(key) if key else None


def rufe_ki(funktion, *args):
    """KI-Aufruf mit Limitpruefung und verstaendlicher Fehlermeldung.

    Der Client wird ausserhalb des try geholt: st.stop() und st.rerun() werfen
    in Streamlit gewoehnliche Exceptions und wuerden hier sonst als
    Netzwerkfehler durchgehen.
    """
    frei, meldung = budget_frei()
    if not frei:
        st.session_state.fehler = meldung
        return None
    client = ki_client()
    if client is None:
        st.session_state.fehler = ('Eigene Argumente gehen gerade nicht. Nimm ein '
                                   'Argument aus dem Materialpool.')
        return None
    try:
        ergebnis = funktion(client, *args)
    except Exception:
        st.session_state.fehler = ('Das hat gerade nicht geklappt. Versuche es noch '
                                   'einmal oder nimm ein Argument aus dem '
                                   'Materialpool.')
        return None
    zaehle()
    st.session_state.fehler = ''
    return ergebnis


# ---------------------------------------------------------------------------
# Kopfbereich
# ---------------------------------------------------------------------------

SCHRITTE = {'rolle': 1, 'argument': 2, 'auswahl': 3, 'aufloesung': 4,
            'abschluss': 5}


def kopf(titel: str):
    nr = SCHRITTE.get(st.session_state.schritt)
    if nr:
        st.markdown(f'<div class="schrittzeile">Schritt {nr} von 5</div>',
                    unsafe_allow_html=True)
    st.subheader(titel)


def rollenhinweis():
    """Leitkriterien im Hauptbereich - auf dem iPad ist die Seitenleiste zu."""
    rolle = st.session_state.rolle
    if rolle and rolle != 'ohne Rolle' and ROLLEN[rolle]:
        st.caption(f'**{rolle}** · Leitkriterien: {" · ".join(ROLLEN[rolle])}')


def restanzeige():
    rest = max(SITZUNGSLIMIT - st.session_state.ki_aufrufe, 0)
    if rest <= 4:
        st.caption(f'Noch {rest} eigene Argumente in dieser Sitzung möglich.')


def seitenleiste():
    with st.sidebar:
        st.markdown('### Diskussionstrainer')
        st.caption(LEITFRAGE)
        rolle = st.session_state.rolle
        if rolle and rolle != 'ohne Rolle':
            st.markdown(f'**Deine Rolle:** {rolle}')
            if ROLLEN[rolle]:
                st.markdown('**Deine Leitkriterien**')
                for k in ROLLEN[rolle]:
                    st.markdown(f'- {k}')
        if st.session_state.technik:
            st.markdown(f'**Technik:** {TECHNIK_ANZEIGE[st.session_state.technik]}')
        if st.session_state.durchgaenge:
            st.caption(f'Geübt: {len(st.session_state.durchgaenge)} Argumente')


# ---------------------------------------------------------------------------
# Zugang
# ---------------------------------------------------------------------------

offen, meldung = freigabe_offen()
if not offen:
    st.title('Diskussionstrainer')
    st.info(meldung)
    st.stop()

erwarteter_code = secret('KLASSENCODE')
if erwarteter_code and not st.session_state.freigeschaltet:
    st.title('Diskussionstrainer')
    st.write('Gib den Code ein, der auf deiner Rollenkarte steht.')
    eingabe = st.text_input('Code', label_visibility='collapsed')
    if st.button('Weiter', type='primary', use_container_width=True):
        if eingabe.strip().lower() == erwarteter_code.strip().lower():
            st.session_state.freigeschaltet = True
            st.rerun()
        else:
            st.error('Der Code stimmt nicht.')
    st.caption('Schreibe hier keine Namen und keine persönlichen Angaben hinein. '
               'Deine Texte werden nicht gespeichert.')
    st.stop()


seitenleiste()

if st.session_state.fehler:
    st.warning(st.session_state.fehler)


# ---------------------------------------------------------------------------
# Schritt 1 - Rolle
# ---------------------------------------------------------------------------

if st.session_state.schritt == 'rolle':
    st.title('Diskussionstrainer')
    st.write('Du übst hier, auf Argumente der Gegenseite zu antworten. Du bekommst '
             'eine Technik vorgegeben und suchst die passende Antwort aus.')
    satz('Wörter mit einer gepunkteten Linie kannst du antippen. Dann erscheint '
         'eine kurze Erklärung – zum Beispiel bei Votum oder Quorum.')
    kopf('🙋 Welche Rolle hast du in der Diskussion?')
    for name in ROLLEN:
        beschriftung = 'Ich habe noch keine Rolle' if name == 'ohne Rolle' else name
        if st.button(beschriftung, key=f'rolle_{name}', use_container_width=True):
            st.session_state.rolle = name
            gehe_zu('argument')
    st.caption('Schreibe im Trainer keine Namen und keine persönlichen Angaben. '
               'Deine Texte werden nicht gespeichert.')


# ---------------------------------------------------------------------------
# Schritt 2 - Argument der Gegenseite
# ---------------------------------------------------------------------------

elif st.session_state.schritt == 'argument':
    kopf('💬 Auf welches Argument willst du antworten?')
    rollenhinweis()
    gs = gegenseite(st.session_state.rolle)

    quelle = st.radio('Woher kommt das Argument?',
                      ['pool', 'selbst'], horizontal=True, key='quelle',
                      format_func=lambda q: '📚 Aus dem Materialpool'
                      if q == 'pool' else '✍️ Selbst schreiben',
                      label_visibility='collapsed')

    if quelle == 'pool':
        if gs:
            seite = gs
            ueberschrift = ('➕ Pro-Argumente' if gs == 'pro'
                            else '➖ Kontra-Argumente')
            st.markdown(f'#### {ueberschrift}')
            st.write('Das sagt die Gegenseite. Genau diese Argumente hörst du in '
                     'der Diskussion.')
        else:
            seite = st.radio('Seite', ['pro', 'kontra'], horizontal=True,
                             key='seite_umschalter',
                             format_func=lambda s: '➕ Pro Volksentscheide'
                             if s == 'pro' else '➖ Kontra Volksentscheide')
        auswahl = fuer_rolle_sortiert(
            [a for a in ARGUMENTE if a['seite'] == seite])
        st.caption('In Klammern steht, welche Gruppe das Argument wahrscheinlich '
                   'bringt.')
        gewaehlt = st.radio(
            'Argument',
            [a['id'] for a in auswahl],
            format_func=arg_beschriftung,
            label_visibility='collapsed',
            key=f'argument_{seite}',
        )
        karte('💬 Das Argument', argument_text(gewaehlt))
        hintergrund_block(gewaehlt)
        if st.button('Weiter mit diesem Argument', type='primary',
                     key='pool_weiter', use_container_width=True):
            starte_runde(gewaehlt, argument_text(gewaehlt), ERWIDERUNGEN[gewaehlt])

    else:
        if gs:
            gegen = 'für' if gs == 'pro' else 'gegen'
            st.write(f'Schreibe ein Argument **{gegen}** bundesweite Volksentscheide, '
                     'das du in der Diskussion erwartest. Dazu werden vier '
                     'Erwiderungen formuliert.')
        else:
            st.write('Schreibe ein Argument für oder gegen bundesweite '
                     'Volksentscheide. Dazu werden vier Erwiderungen formuliert.')
        eigenes = st.text_area('Argument', height=130, max_chars=600,
                               label_visibility='collapsed', key='eigenes_argument',
                               placeholder='Zum Beispiel: Volksentscheide sind '
                               'schlecht, weil …')
        if st.session_state.verstaendnisfrage:
            karte('❓ Eine Frage an dich', st.session_state.verstaendnisfrage,
                  roh=True)
        restanzeige()
        if st.button('Erwiderungen holen', type='primary', key='eig_weiter',
                     use_container_width=True):
            if len(eigenes.strip()) < 15:
                st.error('Schreibe zuerst ein ganzes Argument – mit einem „weil".')
            else:
                with st.spinner('Ich formuliere vier Erwiderungen …'):
                    erg = rufe_ki(trainer.erwiderungen, eigenes.strip(),
                                  st.session_state.rolle)
                if erg is None:
                    st.rerun()
                elif 'verstaendnisfrage' in erg:
                    st.session_state.verstaendnisfrage = erg['verstaendnisfrage']
                    st.rerun()
                else:
                    st.session_state.verstaendnisfrage = ''
                    starte_runde(EIGENE_HERKUNFT, eigenes.strip(), erg)
        st.caption('Die vier Erwiderungen formuliert eine KI. Schreibe keine Namen '
                   'und keine persönlichen Angaben.')

    st.markdown('---')
    materialpool_block()
    if st.session_state.durchgaenge:
        if st.button('🏁 Fertig – für die Rollenkarte', use_container_width=True):
            gehe_zu('abschluss')
    if st.button('Andere Rolle wählen', use_container_width=True):
        gehe_zu('rolle')


# ---------------------------------------------------------------------------
# Schritt 3 - Passende Erwiderung antippen
# ---------------------------------------------------------------------------

elif st.session_state.schritt == 'auswahl':
    technik = st.session_state.technik
    t = TECHNIKEN[technik]
    erw = st.session_state.erw
    eigen = st.session_state.herkunft == EIGENE_HERKUNFT
    kopf('🎯 Welche Antwort passt zu deiner Technik?')

    karte('💬 Das Argument', st.session_state.ausgangsargument, roh=eigen)
    hintergrund_block(st.session_state.herkunft)

    karte(f"{t['emoji']} Deine Technik: {TECHNIK_ANZEIGE[technik]}",
          f"<b>{t['leitfrage']}</b><br>"
          f"<span style=\"font-size:.95rem\">{t['erklaerung']}</span>",
          glossar=False, klasse='technik')

    if st.session_state.falsch:
        st.write('Versuch es noch einmal. Lies die Leitfrage deiner Technik und '
                 'prüfe die übrigen Antworten.')
    else:
        st.write('Alle vier Antworten sind brauchbar. Aber nur **eine** nutzt deine '
                 'Technik. Welche?')

    for n, tk in enumerate(st.session_state.reihenfolge):
        buchstabe = 'ABCD'[n]
        e = erw[tk]
        ist_falsch = tk in st.session_state.falsch
        st.markdown('<div class="zwischenraum"></div>', unsafe_allow_html=True)
        karte(f'Antwort {buchstabe}', e['text'], roh=eigen,
              klasse='falsch' if ist_falsch else '')
        if ist_falsch:
            tt = TECHNIKEN[tk]
            st.markdown(
                f'<div class="hinweis-falsch">✗ Passt nicht zu deiner Technik. '
                f'Diese Antwort nutzt <b>{tt["emoji"]} {TECHNIK_ANZEIGE[tk]}</b> – '
                f'{tt["leitfrage"]}</div>',
                unsafe_allow_html=True)
        elif st.button(f'Antwort {buchstabe} wählen', key=f'wahl_{tk}',
                       use_container_width=True):
            if tk == technik:
                st.session_state.erfolg = ('erster' if not st.session_state.falsch
                                           else 'zweiter')
                gehe_zu('aufloesung')
            st.session_state.falsch.append(tk)
            if len(st.session_state.falsch) >= 2:
                st.session_state.erfolg = 'aufgeloest'
                gehe_zu('aufloesung')
            st.rerun()
        erwiderung_hintergrund(e, f'Antwort {buchstabe}')

    st.markdown('---')
    materialpool_block(st.session_state.herkunft)
    if st.button('Anderes Argument wählen', use_container_width=True):
        technik_zuruecklegen()
        st.session_state.erw = None
        gehe_zu('argument')


# ---------------------------------------------------------------------------
# Schritt 4 - Aufloesung und eigene Worte
# ---------------------------------------------------------------------------

elif st.session_state.schritt == 'aufloesung':
    technik = st.session_state.technik
    t = TECHNIKEN[technik]
    erw = st.session_state.erw
    eigen = st.session_state.herkunft == EIGENE_HERKUNFT
    kopf('✅ Auflösung')

    erfolg = st.session_state.erfolg
    if erfolg == 'erster':
        st.success('Richtig – gleich beim ersten Versuch!')
    elif erfolg == 'zweiter':
        st.success('Richtig – im zweiten Versuch.')
    else:
        st.info('Das war knifflig. Hier ist die passende Antwort.')

    karte('💬 Das Argument', st.session_state.ausgangsargument, roh=eigen)
    karte(f"{t['emoji']} {TECHNIK_ANZEIGE[technik]} – die passende Antwort",
          erw[technik]['text'], roh=eigen, klasse='richtig')
    satz(f"<b>Woran du das erkennst:</b> {t['erklaerung']}")
    erwiderung_hintergrund(erw[technik], 'dieser Antwort')

    with st.expander('🛠️ Alle vier Antworten mit ihren Techniken'):
        for tk in st.session_state.reihenfolge:
            tt = TECHNIKEN[tk]
            karte(f"{tt['emoji']} {TECHNIK_ANZEIGE[tk]}", erw[tk]['text'],
                  roh=eigen, klasse='richtig' if tk == technik else '')
        st.caption('Auf dasselbe Argument kann man also auf vier Arten antworten.')

    st.markdown('#### ✍️ In deinen eigenen Worten (freiwillig)')
    st.write('Wie würdest du das in der Diskussion sagen? Kurz und so, wie du '
             'sprichst. Das kommt am Ende auf deine Rollenkarte.')
    st.text_area('Eigene Worte', height=110, max_chars=400,
                 label_visibility='collapsed',
                 key=f'eigene_{st.session_state.runde}',
                 placeholder='So würde ich es sagen: …')

    if st.button('▶️ Nächstes Argument', type='primary', use_container_width=True):
        sichere_durchgang()
        gehe_zu('argument')
    if st.button('🏁 Fertig – für die Rollenkarte', use_container_width=True):
        sichere_durchgang()
        gehe_zu('abschluss')


# ---------------------------------------------------------------------------
# Schritt 5 - Uebertrag auf die Rollenkarte
# ---------------------------------------------------------------------------

elif st.session_state.schritt == 'abschluss':
    kopf('📋 Für deine Rollenkarte')
    durchgaenge = st.session_state.durchgaenge
    if not durchgaenge:
        st.write('Du hast noch kein Argument fertig geübt.')
        if st.button('Zurück zur Übung', type='primary', use_container_width=True):
            gehe_zu('argument')
        st.stop()

    anzahl = len(durchgaenge)
    sofort = sum(1 for d in durchgaenge if d['erfolg'] == 'erster')
    st.write(f'Du hast **{anzahl}** Argument{"e" if anzahl != 1 else ""} geübt, '
             f'davon **{sofort}** gleich beim ersten Versuch richtig.')
    geuebt = {d['technik'] for d in durchgaenge}
    st.caption('Techniken: ' + ' · '.join(
        f"{TECHNIKEN[tk]['emoji']} {TECHNIK_ANZEIGE[tk]}{' ✓' if tk in geuebt else ''}"
        for tk in TECHNIK_REIHE))

    st.write('Schreib die Antworten **in Stichworten** auf deine Rollenkarte. '
             'In der Diskussion sprichst du frei.')
    for d in durchgaenge:
        wer, was, technik, antwort = rollenkarten_zeile(d)
        eigen = d['herkunft'] not in ARGUMENT_NACH_ID
        was_html = html.escape(was) if eigen else was
        karte(f'Wenn {wer} sagt …',
              f'„{markiere(was_html)}“<br><b>… antworte ich ({technik}):</b> '
              f'{markiere(html.escape(antwort))}',
              glossar=False)

    st.write('Zum Kopieren: Tippe oben rechts im Kasten auf das Kopiersymbol, '
             'oder mache ein Bildschirmfoto.')
    zeilen = ['DISKUSSIONSTRAINER – FÜR MEINE ROLLENKARTE']
    for d in durchgaenge:
        wer, was, technik, antwort = rollenkarten_zeile(d)
        zeilen += ['', f'Wenn {wer} sagt: {was}',
                   f'… antworte ich ({technik}): {antwort}']
    st.code('\n'.join(zeilen), language=None, wrap_lines=True)

    st.markdown('---')
    if st.button('Noch eine Übung machen', use_container_width=True):
        gehe_zu('argument')
