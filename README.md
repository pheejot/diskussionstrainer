# Diskussionstrainer

Übungs-App zu den vier Konter-Techniken aus dem Politikunterricht (UE „Direkte Demokratie", Block B03). Die Schüler antworten auf ein Argument der Gegenseite und bekommen eine Rückmeldung als drei Ampeln plus höchstens zwei Hinweise.

Einsatz: Selbstlernen zwischen B03 Teil 2 und der Fishbowl-Diskussion in B04, etwa 30 Minuten, auf Schul-iPads.

**Es wird nichts gespeichert.** Keine Namen, keine Serverablage, keine Lehrerübersicht. Die Schülertexte gehen an die OpenAI-API und werden danach verworfen.

---

## Dateien

| Datei | Inhalt |
| --- | --- |
| `app.py` | Oberfläche und Ablaufsteuerung |
| `trainer.py` | die drei KI-Aufrufe mit Systemanweisung und JSON-Schema |
| `argumente.py` | die vier Techniken, die 19 Pool-Argumente, die fünf Rollen |
| `wissensbasis.md` | verdichteter Materialpool, geht in jeden KI-Aufruf |
| `requirements.txt` | Streamlit und das OpenAI-SDK |
| `.streamlit/secrets.toml.example` | Vorlage für die Einstellungen |

---

## Einrichten

1. Repository auf GitHub anlegen und die Dateien hochladen.

   `app.py`, `trainer.py`, `argumente.py`, `wissensbasis.md`, `requirements.txt`, `README.md` und `.gitignore` lassen sich per Drag-and-drop hochladen.

   Für den Ordner `.streamlit` geht das nicht: **Add file → Create new file**, als Dateinamen `.streamlit/config.toml` eintippen — der Schrägstrich legt den Ordner mit an — Inhalt einfügen, **Commit**. Dasselbe für `.streamlit/secrets.toml.example`.

   Die Datei `secrets.toml` selbst gehört **nicht** ins Repository. Nur die `.example`-Vorlage; die echten Werte werden in Streamlit eingetragen.
2. Auf `share.streamlit.io` eine App aus dem Repository erstellen, Hauptdatei `app.py`.
3. Unter **Settings → Secrets** eintragen:

```toml
OPENAI_API_KEY = "sk-..."
KLASSENCODE = "volksentscheid"
FREIGABE_START = "2026-09-15"
FREIGABE_ENDE = "2026-09-17"
```

4. Im OpenAI-Konto ein niedriges Ausgabelimit setzen. Das ist die einzige Bremse, die auch bei einem Fehler in der App greift.
5. Die entstandene Adresse selbst einmal durchklicken, dann an die Klasse geben.

---

## Einstellungen

**Freigabefenster.** `FREIGABE_START` und `FREIGABE_ENDE` im Format `JJJJ-MM-TT`. Außerhalb des Fensters zeigt die App einen Hinweis und stellt keine Anfragen. Beide Zeilen sind optional. Zum Ändern die Secrets in der Streamlit-Oberfläche bearbeiten; die App startet danach von selbst neu.

**Klassencode.** `KLASSENCODE` steht auf der Rollenkarte. Zeile entfernen = jeder mit dem Link kommt hinein.

**Limits.** Oben in `app.py`:

```python
SITZUNGSLIMIT = 12   # KI-Antworten pro Schülersitzung
TAGESGRENZE  = 400   # KI-Antworten pro Tag für die gesamte App
```

**Modell.** Oben in `trainer.py`: `MODELL = 'gpt-5.6-luna'`. Reicht die Qualität nicht, hier auf `gpt-5.6-terra` wechseln — das kostet etwa das Zehnfache, bei 20 Schülern immer noch wenige Euro.

---

## Was die App kostet

Pro Aufruf gehen rund 10.100 Tokens konstante Vorlage hinein (Anweisung plus Wissensbasis), dazu etwa 200 Tokens Schülertext; heraus kommen 400 bis 1.000 Tokens. Bei 20 Schülern und höchstens 12 Rückmeldungen je Sitzung liegt das Ganze mit GPT-5.6 Luna zwischen etwa 0,10 und 0,75 Euro für die Klasse. Klassencode und Limits sind deshalb Missbrauchsschutz, keine Kostenbremse.

---

## Zwei bekannte Grenzen

**Die Tagesgrenze überlebt keinen Neustart.** Streamlit Community Cloud startet den Container bei Inaktivität neu, danach zählt die App wieder bei null. Als Bremse gegen einen durchgedrehten Link reicht das; eine verlässliche Abrechnung ist es nicht. Dafür bräuchte es einen externen Speicher.

**Der Zustand hängt am Browser.** Jeder Schüler hat seine eigene Sitzung — genau so soll es sein. Wer die Seite neu lädt, beginnt aber von vorn. Deshalb liegt das Ergebnis am Ende zum Kopieren bereit und wird sofort auf die Rollenkarte übertragen.

---

## Fachliche Grundlage

Alles Fachliche stammt aus dem Materialpool-Vault „Volksentscheide – Diskussionsvorbereitung", veröffentlicht unter <https://publish.obsidian.md/volksentscheide-recherche/00_START/00_LEITFRAGE>. `wissensbasis.md` ist ein verdichteter Auszug daraus: die vier Bausteine eines guten Arguments, die elf Kriterien, die vier Techniken im Vault-Wortlaut, 19 Argumente mit Gegenstrang und Erwiderungsidee, 17 Belege und ein Glossar.

Die KI behandelt **nur** die Belege aus Abschnitt 7 der Wissensbasis als belegt. Alles andere, was wie ein Beleg klingt, wird als ungeprüft markiert und der Schüler nach der Quelle gefragt.

**Wenn sich der Vault ändert, muss `wissensbasis.md` nachgezogen werden.** Die IDs `P1`–`P10`, `K1`–`K9` und `B-…` sind die Schnittstelle zwischen App, Wissensbasis und KI und sollten stabil bleiben.
