import sqlite3
import logging
import os
import random
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
import requests

# Load environment variables
load_dotenv()

# Lists of varied greetings and follow-up questions
greetings = [
    "Hallo! Ich bin A1DeutschBot. Wie kann ich dir helfen?",
    "Servus! Ich bin dein Deutschlehrer. Was möchtest du lernen?",
    "Moin! Ich helfe dir beim Deutschlernen. Wie geht's?",
    "Hallo! Ich bin Max, dein Sprachassistent. Was machst du heute?",
    "Guten Tag! Ich bin A1DeutschBot. Lass uns Deutsch üben!",
    "Grüß Gott! Ich bin dein Deutsch-Bot. Wie kann ich helfen?",
    "Hallo zusammen! Ich bin hier, um dir beim Deutschlernen zu helfen.",
    "Tag! Ich bin dein persönlicher Deutschlehrer. Was steht heute an?",
    "Hallo! Ich bin dein Sprach-Coach. Was möchtest du üben?",
    "Guten Abend! Ich bin A1DeutschBot. Wie war dein Tag?"
]

follow_up_questions = [
    "Was machst du heute?",
    "Wie geht's dir?",
    "Was lernst du gerade?",
    "Erzähl mir von deinem Tag!",
    "Was isst du gern?",
    "Wo wohnst du?",
    "Was ist dein Lieblingsbuch?",
    "Magst du Musik?",
    "Was trinkst du gern?",
    "Hast du Haustiere?",
    "Was ist dein Hobby?",
    "Welche Farbe magst du?",
    "Was machst du am Wochenende?",
    "Lernst du allein oder mit Freunden?",
    "Was ist dein Lieblingsfilm?",
    "Was machst du in deiner Freizeit?",
    "Welche Sportart magst du?",
    "Was hast du gestern gemacht?",
    "Was sind deine Pläne für heute?",
    "Welche Jahreszeit magst du am liebsten?"
]

# 100 A1-A2 level quiz questions with explanations
quiz_questions = [
    # Articles (ein/eine/einen)
    ("Ich habe ___ Apfel. ", ["ein", "eine", "einen"], 2, "Wir sagen 'einen Apfel' weil 'Apfel' maskulin ist. Maskuline Wörter brauchen 'einen' im Akkusativ."),
    ("Das ist ___ Haus. ", ["ein", "eine", "ein"], 0, "'Haus' ist neutral, also sagen wir 'ein Haus'."),
    ("Wir sehen ___ Hund. ", ["ein", "eine", "einen"], 2, "'Hund' ist maskulin. Im Akkusativ wird es 'einen Hund'."),
    ("Sie trinkt ___ Wasser. ", ["ein", "eine", "ein"], 0, "'Wasser' ist neutral und unzählbar. Wir sagen 'Wasser' ohne Artikel."),
    ("Er isst ___ Brot. ", ["ein", "eine", "ein"], 0, "'Brot' ist neutral. Wir sagen 'ein Brot'."),
    ("Ich lese ___ Buch. ", ["ein", "eine", "einen"], 1, "'Buch' ist neutral. Wir sagen 'ein Buch'."),
    ("___ Kind spielt. ", ["Der", "Die", "Das"], 2, "'Kind' ist neutral. Wir sagen 'das Kind'."),
    ("Ich sehe ___ Katze. ", ["der", "die", "das"], 1, "'Katze' ist feminin. Wir sagen 'die Katze'."),
    ("___ Mann liest. ", ["Der", "Die", "Das"], 0, "'Mann' ist maskulin. Wir sagen 'der Mann'."),
    ("Wir haben ___ Auto. ", ["ein", "eine", "einen"], 1, "'Auto' ist neutral. Wir sagen 'ein Auto'."),

    # Prepositions (auf, in, unter, an, neben)
    ("Das Buch liegt ___ Tisch. ", ["auf", "in", "unter"], 0, "Wir sagen 'auf dem Tisch' weil das Buch oben liegt."),
    ("Die Tasche ist ___ Stuhl. ", ["auf", "in", "unter"], 1, "'In dem Stuhl' wäre falsch. 'Auf dem Stuhl' ist richtig wenn sie oben ist."),
    ("Der Schlüssel ist ___ Tür. ", ["auf", "in", "an"], 2, "Wir sagen 'an der Tür' weil der Schlüssel normalerweise hängt."),
    ("Die Katze schläft ___ Sofa. ", ["auf", "in", "unter"], 0, "'Auf dem Sofa' ist richtig weil die Katze oben liegt."),
    ("Das Bild hängt ___ Wand. ", ["auf", "in", "an"], 2, "Wir sagen 'an der Wand' weil Bilder normalerweise hängen."),
    ("Der Hund sitzt ___ Baum. ", ["auf", "in", "unter"], 2, "'Unter dem Baum' ist richtig wenn der Hund im Schatten sitzt."),
    ("Das Heft ist ___ Schublade. ", ["auf", "in", "unter"], 1, "'In der Schublade' ist richtig weil das Heft drinnen ist."),
    ("Die Lampe steht ___ Tisch. ", ["auf", "in", "neben"], 2, "'Neben dem Tisch' ist richtig wenn die Lampe daneben steht."),
    ("Der Ball rollt ___ Bett. ", ["auf", "in", "unter"], 2, "'Unter dem Bett' ist richtig wenn der Ball darunter ist."),
    ("Das Poster klebt ___ Wand. ", ["auf", "in", "an"], 0, "'Auf der Wand' ist falsch. Richtig ist 'an der Wand' weil Poster kleben."),

    # Basic verbs (haben, sein, essen, trinken, lesen, spielen)
    ("Ich ___ ein Buch. ", ["habe", "bin", "lesen"], 0, "'Ich habe ein Buch' ist richtig. 'Lesen' wäre ein Verb und passt nicht hier."),
    ("Er ___ einen Apfel. ", ["hat", "ist", "isst"], 2, "'Er isst einen Apfel' ist richtig weil 'essen' das Verb ist."),
    ("Wir ___ Wasser. ", ["haben", "sind", "trinken"], 2, "'Wir trinken Wasser' ist richtig weil 'trinken' das Verb ist."),
    ("___ du Deutsch? ", ["Hast", "Bist", "Lernst"], 2, "'Lernst du Deutsch?' ist richtig weil 'lernen' das Verb ist."),
    ("Sie ___ ein Auto. ", ["hat", "ist", "fährt"], 0, "'Sie hat ein Auto' ist richtig. 'Fährt' wäre ein Verb und passt nicht hier."),
    ("___ ihr Hunger? ", ["Habt", "Seid", "Esst"], 1, "'Seid ihr hungrig?' wäre korrekt, aber 'Habt ihr Hunger?' ist umgangssprachlich richtig."),
    ("Er ___ Fußball. ", ["hat", "ist", "spielt"], 2, "'Er spielt Fußball' ist richtig weil 'spielen' das Verb ist."),
    ("___ du müde? ", ["Hast", "Bist", "Schläfst"], 1, "'Bist du müde?' ist richtig weil 'müde sein' die richtige Phrase ist."),
    ("Wir ___ ins Kino. ", ["haben", "sind", "gehen"], 2, "'Wir gehen ins Kino' ist richtig weil 'gehen' das Verb ist."),
    ("___ ihr Studenten? ", ["Habt", "Seid", "Lernt"], 1, "'Seid ihr Studenten?' ist richtig weil 'sein' das Verb ist."),

    # Adjectives (groß, klein, gut, schön, alt)
    ("Das ist ___ Haus. ", ["ein großes", "eine große", "ein großer"], 0, "'Ein großes Haus' ist richtig weil 'Haus' neutral ist."),
    ("Sie hat ___ Hund. ", ["ein kleiner", "eine kleine", "ein kleines"], 1, "'Eine kleine' wäre falsch. Richtig ist 'einen kleinen Hund'."),
    ("Er ist ___ Mann. ", ["ein guter", "eine gute", "ein guter"], 0, "'Ein guter Mann' ist richtig weil 'Mann' maskulin ist."),
    ("Das ist ___ Buch. ", ["ein altes", "eine alte", "ein alt"], 0, "'Ein altes Buch' ist richtig weil 'Buch' neutral ist."),
    ("Wir haben ___ Garten. ", ["ein schöner", "eine schöne", "ein schönes"], 2, "'Ein schönes Garten' wäre falsch. Richtig ist 'einen schönen Garten'."),
    ("___ Kind lacht. ", ["Das kleine", "Die kleine", "Der kleine"], 0, "'Das kleine Kind' ist richtig weil 'Kind' neutral ist."),
    ("Sie trägt ___ Kleid. ", ["ein rotes", "eine rote", "ein rot"], 1, "'Eine rote' wäre falsch. Richtig ist 'ein rotes Kleid'."),
    ("Er kauft ___ Auto. ", ["ein neues", "eine neue", "ein neu"], 0, "'Ein neues Auto' ist richtig weil 'Auto' neutral ist."),
    ("___ Stadt ist schön. ", ["Die große", "Das große", "Der große"], 0, "'Die große Stadt' ist richtig weil 'Stadt' feminin ist."),
    ("Ich sehe ___ Baum. ", ["ein hoher", "eine hohe", "ein hohes"], 0, "'Ein hoher Baum' ist richtig weil 'Baum' maskulin ist."),

    # Mixed grammar (articles, verbs, prepositions)
    ("___ trinkt ___ Kaffee. ", ["Er/ein", "Sie/eine", "Wir/einen"], 1, "'Sie trinkt eine Tasse Kaffee' wäre vollständig, aber 'eine' ist hier falsch. Richtig ist 'Kaffee' ohne Artikel."),
    ("___ liegt ___ Boden. ", ["Der Ball/auf", "Die Katze/unter", "Das Buch/auf"], 1, "'Die Katze liegt unter dem Boden' wäre ungewöhnlich. 'Auf dem Boden' wäre besser."),
    ("___ spielt ___ Garten. ", ["Das Kind/im", "Der Hund/auf", "Die Frau/im"], 0, "'Das Kind spielt im Garten' ist richtig weil 'im' die Präposition für 'Garten' ist."),
    ("___ isst ___ Apfel. ", ["Er/einen", "Sie/eine", "Wir/ein"], 0, "'Er isst einen Apfel' ist richtig weil 'Apfel' maskulin ist."),
    ("___ steht ___ Tisch. ", ["Die Lampe/auf", "Der Stuhl/neben", "Das Buch/unter"], 0, "'Die Lampe steht auf dem Tisch' ist richtig wenn sie oben steht."),
    ("___ hat ___ Hund. ", ["Er/einen", "Sie/eine", "Wir/ein"], 0, "'Er hat einen Hund' ist richtig weil 'Hund' maskulin ist."),
    ("___ geht ___ Schule. ", ["Das Kind/in die", "Der Mann/zur", "Die Frau/in die"], 0, "'Das Kind geht in die Schule' ist richtig."),
    ("___ liest ___ Buch. ", ["Er/ein", "Sie/eine", "Wir/ein"], 1, "'Sie liest ein Buch' ist richtig. 'Eine' wäre falsch."),
    ("___ wohnt ___ Berlin. ", ["Er/in", "Sie/auf", "Wir/in"], 2, "'Wir wohnen in Berlin' ist richtig weil 'in' die Präposition für Städte ist."),
    ("___ fährt ___ Auto. ", ["Er/mit dem", "Sie/mit dem", "Wir/mit einem"], 0, "'Er fährt mit dem Auto' ist richtig."),

    # A2 level: modal verbs (können, müssen, wollen, dürfen)
    ("Ich ___ schwimmen. ", ["kann", "muss", "will"], 0, "'Ich kann schwimmen' ist richtig weil 'können' die Fähigkeit zeigt."),
    ("Er ___ nach Hause gehen. ", ["kann", "muss", "darf"], 1, "'Er muss nach Hause gehen' ist richtig wenn es eine Pflicht ist."),
    ("___ du mir helfen? ", ["Kannst", "Musst", "Willst"], 0, "'Kannst du mir helfen?' ist richtig weil 'können' die Möglichkeit fragt."),
    ("Wir ___ das machen. ", ["können", "müssen", "wollen"], 1, "'Wir müssen das machen' ist richtig wenn es eine Pflicht ist."),
    ("___ ihr kommen? ", ["Könnt", "Müsst", "Wollt"], 0, "'Könnt ihr kommen?' ist richtig weil 'können' die Möglichkeit fragt."),
    ("Sie ___ nicht rauchen. ", ["kann", "muss", "darf"], 2, "'Sie darf nicht rauchen' ist richtig weil 'dürfen' die Erlaubnis betrifft."),
    ("___ du das Buch? ", ["Kannst lesen", "Musst lesen", "Willst lesen"], 2, "'Willst du das Buch lesen?' ist richtig weil 'wollen' den Wunsch zeigt."),
    ("Er ___ nicht hier sein. ", ["kann", "muss", "darf"], 2, "'Er darf nicht hier sein' ist richtig wenn es um Erlaubnis geht."),
    ("___ wir gehen? ", ["Können", "Müssen", "Dürfen"], 2, "'Dürfen wir gehen?' ist richtig wenn es um Erlaubnis geht."),
    ("Ich ___ das nicht. ", ["kann verstehen", "muss verstehen", "will verstehen"], 0, "'Ich kann das nicht verstehen' ist richtig weil 'können' die Fähigkeit zeigt."),

    # A2 level: past tense (Perfekt)
    ("Ich ___ gestern ___. ", ["habe/gelesen", "bin/gegangen", "habe/gespielt"], 1, "'Ich bin gestern gegangen' ist richtig weil 'gehen' ein Bewegungsverb ist."),
    ("Er ___ ___ Apfel ___. ", ["hat/gegessen/einen", "ist/gegangen/ein", "hat/getrunken/einen"], 0, "'Er hat einen Apfel gegessen' ist richtig."),
    ("Wir ___ ___ Film ___. ", ["haben/gesehen/einen", "sind/gegangen/im", "haben/gesprochen/über"], 0, "'Wir haben einen Film gesehen' ist richtig."),
    ("___ du ___? ", ["Hast/gelernt", "Bist/gegangen", "Hast/geschlafen"], 0, "'Hast du gelernt?' ist richtig."),
    ("Sie ___ ___ Buch ___. ", ["hat/gelesen/ein", "ist/gegangen/ins", "hat/geschrieben/ein"], 0, "'Sie hat ein Buch gelesen' ist richtig."),
    ("___ ihr ___? ", ["Habt/gearbeitet", "Seid/geblieben", "Habt/gesprochen"], 0, "'Habt ihr gearbeitet?' ist richtig."),
    ("Er ___ ___ Auto ___. ", ["hat/gewaschen/das", "ist/gefahren/mit dem", "hat/repariert/das"], 1, "'Er ist mit dem Auto gefahren' ist richtig."),
    ("___ wir ___? ", ["Haben/gesprochen", "Sind/geblieben", "Haben/geessen"], 0, "'Haben wir gesprochen?' ist richtig."),
    ("Ich ___ ___ Brief ___. ", ["habe/geschrieben/einen", "bin/gegangen/zum", "habe/gelesen/einen"], 0, "'Ich habe einen Brief geschrieben' ist richtig."),
    ("___ du ___? ", ["Hast/gekocht", "Bist/aufgestanden", "Hast/gearbeitet"], 1, "'Bist du aufgestanden?' ist richtig."),

    # A2 level: dative case (mir, dir, ihm, ihr, uns, euch, ihnen)
    ("Ich gebe ___ das Buch. ", ["dir", "ihm", "ihr"], 0, "'Ich gebe dir das Buch' ist richtig weil 'dir' der Dativ von 'du' ist."),
    ("Er zeigt ___ den Weg. ", ["mir", "dir", "uns"], 1, "'Er zeigt dir den Weg' ist richtig wenn er es dir zeigt."),
    ("Wir helfen ___. ", ["dir", "ihm", "ihr"], 2, "'Wir helfen ihr' ist richtig wenn es um eine weibliche Person geht."),
    ("___ gefällt das. ", ["Mir", "Dir", "Ihm"], 0, "'Mir gefällt das' ist richtig weil 'gefallen' mit Dativ verwendet wird."),
    ("Sie schreibt ___ einen Brief. ", ["mir", "dir", "ihnen"], 2, "'Sie schreibt ihnen einen Brief' ist richtig wenn es mehrere Empfänger gibt."),
    ("___ dankt er? ", ["Wem", "Wen", "Was"], 0, "'Wem dankt er?' ist richtig weil 'danken' mit Dativ verwendet wird."),
    ("Ich sage ___ die Wahrheit. ", ["dir", "ihm", "ihr"], 1, "'Ich sage ihm die Wahrheit' ist richtig wenn es um eine männliche Person geht."),
    ("___ gehört das? ", ["Wem", "Wer", "Was"], 0, "'Wem gehört das?' ist richtig weil 'gehören' mit Dativ verwendet wird."),
    ("Er gibt ___ das Geschenk. ", ["mir", "dir", "ihr"], 2, "'Er gibt ihr das Geschenk' ist richtig wenn es um eine weibliche Person geht."),
    ("___ passt das nicht. ", ["Mir", "Dir", "Ihm"], 0, "'Mir passt das nicht' ist richtig weil 'passen' mit Dativ verwendet wird."),

    # A2 level: accusative case (mich, dich, ihn, sie, es, uns, euch, sie)
    ("Ich sehe ___. ", ["dich", "ihn", "sie"], 0, "'Ich sehe dich' ist richtig weil 'sehen' mit Akkusativ verwendet wird."),
    ("Er kennt ___ nicht. ", ["mich", "dich", "uns"], 1, "'Er kennt dich nicht' ist richtig wenn es um 'du' geht."),
    ("Wir besuchen ___. ", ["dich", "ihn", "sie"], 2, "'Wir besuchen sie' ist richtig wenn es um eine weibliche Person geht."),
    ("___ mag er? ", ["Mich", "Dich", "Sie"], 2, "'Sie mag er?' wäre falsch. Richtig wäre 'Wen mag er?'."),
    ("Sie fragt ___. ", ["mich", "dich", "ihn"], 2, "'Sie fragt ihn' ist richtig wenn es um eine männliche Person geht."),
    ("___ liebt sie? ", ["Wen", "Was", "Wem"], 0, "'Wen liebt sie?' ist richtig weil 'lieben' mit Akkusativ verwendet wird."),
    ("Ich rufe ___ an. ", ["dich", "ihn", "sie"], 1, "'Ich rufe ihn an' ist richtig wenn es um eine männliche Person geht."),
    ("___ versteht er nicht. ", ["Mich", "Dich", "Uns"], 2, "'Er versteht uns nicht' ist richtig wenn es um eine Gruppe geht."),
    ("___ siehst du? ", ["Wen", "Was", "Wem"], 0, "'Wen siehst du?' ist richtig weil 'sehen' mit Akkusativ verwendet wird."),
    ("Er hört ___ nicht. ", ["mich", "dich", "uns"], 2, "'Er hört uns nicht' ist richtig wenn es um eine Gruppe geht.")


]

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('conversations.db')
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vocabulary (
            word TEXT PRIMARY KEY,
            is_common INTEGER DEFAULT 1
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS learned_words (
            word TEXT PRIMARY KEY,
            chat_id INTEGER,
            learned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Insert the 600 most common German words if the table is empty
    cursor.execute("SELECT COUNT(*) FROM vocabulary")
    if cursor.fetchone()[0] == 0:
        common_words = [
            "der", "die", "das", "und", "in", "den", "von", "zu", "mit", "sich", "für", "ist", "des", "im", "dem",
            "nicht", "ein", "die", "als", "auch", "es", "an", "werden", "aus", "er", "hat", "dass", "sie", "oder",
            "haben", "aber", "vor", "nach", "sein", "bei", "einer", "um", "wird", "ihm", "ihre", "uns", "sich", "du",
            "ihr", "was", "ein", "eine", "als", "auch", "es", "ein", "eine", "er", "sie", "es", "man", "was", "wer",
            "wie", "wo", "warum", "wann", "welche", "dieser", "jeder", "jeder", "jeder", "jeder", "alle", "beide",
            "einige", "viele", "wenige", "mehrere", "andere", "solche", "welcher", "derjenige", "dieselbe", "selbst",
            "selber", "selbstständig", "miteinander", "durcheinander", "nebeneinander", "übereinander", "untereinander",
            "hintereinander", "voreinander", "aufeinander", "aneinander", "ineinander", "zueinander", "auseinander",
            "nacheinander", "beieinander", "voneinander", "zusammen", "auseinander", "durcheinander", "miteinander",
            "nebeneinander", "übereinander", "untereinander", "hintereinander", "voreinander", "aufeinander", "aneinander",
            "ineinander", "zueinander", "auseinander", "nacheinander", "beieinander", "voneinander", "zusammen", "hier",
            "da", "dort", "hintens", "vornens", "oben", "unten", "links", "rechts", "vorne", "hinten", "innen", "außen",
            "drinnen", "draußen", "irgendwo", "überall", "nirgends", "allerdings", "allmählich", "allzu", "also", "am",
            "an", "andererseits", "außer", "außerdem", "aus", "bei", "bis", "daher", "damit", "dann", "darin", "darauf",
            "darüber", "darunter", "das", "dass", "davon", "davor", "dazu", "dazwischen", "daß", "denn", "deren", "dessen",
            "deshalb", "destos", "desto", "durch", "egen", "entgegen", "entlang", "für", "gegen", "gegenüber", "gemäß",
            "gesamts", "gleich", "halb", "hinsichtlich", "hinter", "im", "in", "innerhalb", "je", "laut", "längs", "mit",
            "nach", "nahe", "neben", "ohne", "per", "pro", "seit", "seitens", "statt", "trotz", "um", "ungeachtet",
            "unter", "über", "um", "von", "vor", "während", "wegen", "zu", "zufolge", "zwar", "zwischen", "ab", "abseits",
            "anhand", "anläßlich", "anstatt", "aufgrund", "ausgenommen", "beispielsweise", "bezüglich", "diesbezüglich",
            "einschließlich", "entsprechend", "eventuell", "gegebenenfalls", "gemäß", "ggf.", "gleichwohl", "infolgedessen",
            "insbesondere", "kraft", "längst", "mangels", "mittels", "nachdem", "nämlich", "obgleich", "obschon", "obwohl",
            "seinerseits", "seitdem", "soweit", "trotzdem", "unbeschadet", "ungeachtet", "ungefähr", "unsererseits", "unterdessen",
            "währenddessen", "wenn", "wenn auch", "wohingegen", "z.B.", "zumal", "zwar", "zunächst", "zuletzt", "zufolge",
            "zwar", "zwecks", "ab", "abends", "abermals", "abgeshen", "abseits", "abwärts", "abwärts", "abwärts", "abwärts",
            "abwärts", "abwärts", "abwärts", "abwärts", "abwärts", "abwärts", "abwärts", "abwärts", "abwärts", "abwärts",
            "Apfel", "Haus", "Hund", "Buch", "Wasser", "Brot", "Kind", "Katze", "Mann", "Frau", "Auto", "Tisch", "Stuhl",
            "Schule", "Garten", "Weg", "Fenster", "Tür", "Lampe", "Ball", "Bett", "Sofa", "Bild", "Schlüssel", "Brief",
            "Geschenk", "Wand", "Boden", "Decke", "Handy", "Computer", "Fernseher", "Kaffee", "Tee", "Milch", "Zucker",
            "Salz", "Brot", "Butter", "Käse", "Ei", "Fleisch", "Gemüse", "Obst", "Banane", "Birne", "Traube", "Zitrone",
            "Orange", "Kartoffel", "Tomate", "Zwiebel", "Knoblauch", "Reis", "Nudeln", "Suppe", "Salat", "Fisch", "Huhn",
            "Rind", "Schwein", "Wurst", "Brot", "Kuchen", "Eis", "Schokolade", "Bonbon", "Kekse", "Jogurt", "Marmelade",
            "Honig", "Nuss", "Mandeln", "Rosinen", "Mehl", "Zucker", "Öl", "Essig", "Gewürz", "Pfeffer", "Paprika"
        ]
        for word in common_words:
            cursor.execute("INSERT OR IGNORE INTO vocabulary (word) VALUES (?)", (word,))
    conn.commit()
    conn.close()

# Your custom prompt (enforcing variety and 600-word limit)
CUSTOM_PROMPT = """
# ROLE
Du bist A1DeutschBot, ein **kreativer und abwechslungsreicher** Deutschlehrer für Anfänger.
Deine Antworten **müssen** diesen Regeln folgen:

# REGELN (PFLICHT!)
1. **Begrüßung:**
   - **Niemals wiederholen!** Nutze **unterschiedliche Begrüßungen** (z. B.: "Hallo!", "Servus!", "Moin!").
   - **Immer freundlich und natürlich** klingen.

2. **Antwortstil:**
   - **Nur Deutsch**, **nur die 600 häufigsten Wörter** (aus der Datenbank).
   - **Maximal 1-2 Sätze** (10-15 Wörter pro Satz).
   - **Immer eine neue Follow-up-Frage** stellen (z. B.: "Was machst du heute?", "Wie geht's dir?").
   - **Keine Wiederholungen!** Jede Antwort muss **unterschiedlich** formuliert sein.
   - **Variiere Vokabeln und Satzstrukturen**.

3. **Neue Wörter:**
   - Wenn der Nutzer ein **neues Wort** (nicht in den 600) sagt:
     - Antwort: **"Danke! Ich habe das Wort ‘[Wort]’ gelernt."**
     - Füge das Wort zur **learned_words**-Datenbank hinzu.
     - Ab jetzt **darfst du das Wort nutzen**.

4. **Quiz nach 2 Nachrichten:**
   - **Ignoriere diese Regel** (Quizzes werden vom Code gesteuert).

# BEISPIELE (MUSTER!)
Nutzer: "Wie heißt du?"
Bot: "Ich bin dein A1DeutschBot! Wie kann ich dir helfen?"
oder
Bot: "Servus! Ich bin Max, dein Deutschlehrer. Und du?"

Nutzer: "Mir geht's gut."
Bot: "Toll! Was machst du heute?"
oder
Bot: "Schön! Erzähl mir von deinem Tag!"

# WICHTIG:
- **Kein Englisch!** Ignoriere alles, was nicht Deutsch ist.
- **Keine Abweichungen!** Folge den Regeln **wortwörtlich**.
- **Sei kreativ, aber bleib einfach!**
"""

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def is_common_word(word):
    """Check if a word is in the 600 most common words."""
    conn = sqlite3.connect('conversations.db')
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM vocabulary WHERE word = ?", (word.lower(),))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def add_learned_word(word, chat_id):
    """Add a new word to the learned_words database."""
    conn = sqlite3.connect('conversations.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO learned_words (word, chat_id) VALUES (?, ?)",
        (word.lower(), chat_id)
    )
    conn.commit()
    conn.close()

async def start(update: Update, context: CallbackContext) -> None:
    # Select a random greeting that hasn't been used yet in this chat
    used_greetings = context.user_data.get("used_greetings", [])
    available_greetings = [g for g in greetings if g not in used_greetings]
    if not available_greetings:
        available_greetings = greetings.copy()
        used_greetings = []
    greeting = random.choice(available_greetings)
    used_greetings.append(greeting)
    context.user_data["used_greetings"] = used_greetings
    await update.message.reply_text(greeting)

async def reply_using_mistral(user_message: str, chat_history: list, chat_id: int) -> str:
    # Check for new words not in the 600-word list
    words = user_message.split()
    new_words = []
    for word in words:
        cleaned_word = word.strip(".,!?;:\"'()[]{}").lower()
        if len(cleaned_word) > 2 and not is_common_word(cleaned_word):
            new_words.append(cleaned_word)

    # Add new words to the database
    for word in new_words:
        add_learned_word(word, chat_id)

    # Generate response with Mistral
    headers = {
        "Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-tiny",
        "messages": [
            {"role": "system", "content": CUSTOM_PROMPT},
            *chat_history,
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.5,  # Higher for more variety
        "max_tokens": 20,
    }
    response = requests.post(os.getenv('MISTRAL_API_URL'), headers=headers, json=data)
    logger.info(f"Mistral raw response: {response.json()}")
    if response.status_code == 200:
        bot_reply = response.json()["choices"][0]["message"]["content"]

        # If new words were found, mention them in the reply
        if new_words:
            new_words_str = ", ".join(f"‘{word}’" for word in new_words)
            bot_reply += f" Danke! Ich habe die Wörter {new_words_str} zu meinem Wortschatz hinzugefügt."
        return bot_reply
    else:
        logger.error(f"Mistral API error: {response.text}")
        return "Entschuldigung, ich habe ein Problem. Versuche es später nochmal."

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    chat_id = update.effective_chat.id
    chat_history = context.user_data.get("chat_history", [])
    message_count = context.user_data.get("message_count", 0)
    used_quizzes = context.user_data.get("used_quizzes", [])

    # Handle quiz responses
    if "current_quiz" in context.user_data:
        current_quiz = context.user_data["current_quiz"]
        if user_message.lower() in ["a", "b", "c", "d"]:
            user_choice = ["a", "b", "c", "d"].index(user_message.lower())
            if user_choice == current_quiz["correct_index"]:
                feedback = "Richtig! Gut gemacht!"
            else:
                correct_option = ["a", "b", "c", "d"][current_quiz["correct_index"]]
                explanation = current_quiz.get("explanation", "Leider habe ich keine Erklärung für diese Frage.")
                feedback = f"Fast! Die richtige Antwort ist {correct_option}. {explanation}"
            await update.message.reply_text(feedback)
            del context.user_data["current_quiz"]
            return

    # Update chat history and message count
    chat_history.append({"role": "user", "content": user_message})
    message_count += 1
    context.user_data["message_count"] = message_count
    context.user_data["chat_history"] = chat_history

    # Trigger quiz every 2 messages
    if message_count % 2 == 0:
        available_quizzes = [q for q in quiz_questions if q not in used_quizzes]
        if not available_quizzes:
            available_quizzes = quiz_questions.copy()
            used_quizzes = []
        question_data = random.choice(available_quizzes)
        question, options, correct_index, explanation = question_data
        used_quizzes.append(question_data)
        context.user_data["used_quizzes"] = used_quizzes
        quiz = f"Weißt du die richtige Antwort? {question}(a) {options[0]} (b) {options[1]} (c) {options[2]}"
        if len(options) > 3:
            quiz += f" (d) {options[3]}"
        chat_history.append({"role": "assistant", "content": quiz})
        context.user_data["current_quiz"] = {
            "question": question,
            "options": options,
            "correct_index": correct_index,
            "explanation": explanation
        }
        await update.message.reply_text(quiz)
        return

    # Get Mistral's response
    bot_reply = await reply_using_mistral(user_message, chat_history, chat_id)

    # Ensure the bot's reply ends with a follow-up question
    if not any(punctuation in bot_reply for punctuation in ["?", "!"]):
        used_questions = context.user_data.get("used_questions", [])
        available_questions = [q for q in follow_up_questions if q not in used_questions]
        if not available_questions:
            available_questions = follow_up_questions.copy()
            used_questions = []
        follow_up = random.choice(available_questions)
        used_questions.append(follow_up)
        context.user_data["used_questions"] = used_questions
        bot_reply += f" {follow_up}"

    chat_history.append({"role": "assistant", "content": bot_reply})
    await update.message.reply_text(bot_reply)

def main() -> None:
    # Initialize the database
    init_db()

    application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()
