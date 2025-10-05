# B1 Level Quiz Questions
b1_quiz_questions = [
    # Konjunktiv II (würde, hätte, wäre)
    ("Ich ___ gern mehr Zeit. ", ["habe", "hätte", "würde haben"], 1, "'Ich hätte gern mehr Zeit' ist Konjunktiv II und drückt einen Wunsch aus."),
    ("Er ___ das nicht tun. ", ["wird", "würde", "hat"], 1, "'Er würde das nicht tun' ist Konjunktiv II für hypothetische Situationen."),
    ("___ du mir helfen? ", ["Kannst", "Würdest", "Hast"], 1, "'Würdest du mir helfen?' ist die höfliche Form von 'Kannst du mir helfen?'."),
    ("Wir ___ das Problem gelöst. ", ["haben", "hätten", "würden haben"], 1, "'Wir hätten das Problem gelöst' ist Konjunktiv II für irreale Situationen."),
    ("___ du mehr Geld, was würdest du kaufen? ", ["Hättest", "Hast", "Würdest haben"], 0, "'Hättest du mehr Geld' leitet eine hypothetische Frage ein."),

    # Präteritum (regelmäßige und unregelmäßige Verben)
    ("Gestern ___ ich ins Kino. ", ["gehe", "ging", "bin gegangen"], 1, "'Ging' ist das Präteritum von 'gehen'."),
    ("Er ___ gestern ein Buch. ", ["liest", "las", "hat gelesen"], 1, "'Las' ist das Präteritum von 'lesen'."),
    ("Wir ___ letzes Jahr nach Berlin. ", ["fahren", "fuhren", "sind gefahren"], 1, "'Fuhren' ist das Präteritum von 'fahren'."),
    ("___ du gestern den Film? ", ["Siehst", "Sahst", "Hast gesehen"], 1, "'Sahst' ist das Präteritum von 'sehen'."),
    ("Sie ___ mir gestern eine E-Mail. ", ["schreibt", "schrieb", "hat geschrieben"], 1, "'Schrieb' ist das Präteritum von 'schreiben'."),

    # Passiv (Präsens und Präteritum)
    ("Der Brief ___ gestern geschrieben. ", ["wird", "wurde", "ist"], 1, "'Wurde' ist Präteritum Passiv von 'schreiben'."),
    ("Das Auto ___ repariert. ", ["wird", "wurde", "ist"], 0, "'Wird' ist Präsens Passiv von 'reparieren'."),
    ("___ das Fenster geöffnet? ", ["Wird", "Wurde", "Ist"], 0, "'Wird' ist die richtige Form für Präsens Passiv."),
    ("Die Aufgabe ___ schnell erledigt. ", ["wird", "wurde", "ist"], 0, "'Wird' ist Präsens Passiv für regelmäßige Handlungen."),
    ("Das Haus ___ 1990 gebaut. ", ["wird", "wurde", "ist"], 1, "'Wurde' ist Präteritum Passiv für abgeschlossene Handlungen."),

    # Relativsätze (der, die, das)
    ("Das ist das Buch, ___ ich gestern gekauft habe. ", ["das", "das ich", "welches"], 0, "'Das' ist der richtige Relativpronomen für Neutrum."),
    ("Der Mann, ___ dort steht, ist mein Lehrer. ", ["der", "die", "das"], 0, "'Der' ist der richtige Relativpronomen für Maskulinum."),
    ("Die Frau, ___ ich gestern getroffen habe, heißt Anna. ", ["die", "der", "das"], 0, "'Die' ist der richtige Relativpronomen für Femininum."),
    ("Die Kinder, ___ im Garten spielen, sind meine Nachbarn. ", ["die", "der", "das"], 0, "'Die' ist der richtige Relativpronomen für Plural."),
    ("Das ist der Stift, ___ ich suche. ", ["den", "der", "das"], 0, "'Den' ist Akkusativ für Maskulinum."),

    # Konjunktionen (weil, obwohl, damit, wenn)
    ("Ich lerne Deutsch, ___ ich nach Deutschland ziehen will. ", ["weil", "obwohl", "damit"], 2, "'Damit' zeigt den Zweck der Handlung an."),
    ("___ es regnet, gehe ich spazieren. ", ["Weil", "Obwohl", "Damit"], 1, "'Obwohl' zeigt einen Gegensatz an."),
    ("Ich rufe dich an, ___ du Bescheid weißt. ", ["weil", "obwohl", "damit"], 2, "'Damit' zeigt den Zweck der Handlung an."),
    ("___ du Zeit hast, können wir uns treffen. ", ["Weil", "Wenn", "Damit"], 1, "'Wenn' leitet eine Bedingung ein."),
    ("Er kommt nicht, ___ er krank ist. ", ["weil", "obwohl", "damit"], 0, "'Weil' zeigt den Grund an."),

    # Präpositionen mit Dativ/Akkusativ (Wechselpräpositionen)
    ("Das Bild hängt ___ der Wand. ", ["an", "auf", "in"], 0, "'An der Wand' ist richtig, weil 'hängen' Dativ verlangt."),
    ("Ich stelle die Vase ___ den Tisch. ", ["auf", "an", "in"], 0, "'Auf den Tisch' ist Akkusativ, weil 'stellen' eine Bewegung beschreibt."),
    ("Der Schlüssel liegt ___ dem Tisch. ", ["auf", "an", "in"], 0, "'Auf dem Tisch' ist Dativ, weil 'liegen' eine Position beschreibt."),
    ("Sie setzt sich ___ den Stuhl. ", ["auf", "an", "in"], 0, "'Auf den Stuhl' ist Akkusativ, weil 'setzen' eine Bewegung beschreibt."),
    ("Das Buch liegt ___ der Tasche. ", ["in", "auf", "an"], 0, "'In der Tasche' ist Dativ, weil 'liegen' eine Position beschreibt."),

    # Reflexivverben (sich waschen, sich freuen, sich interessieren)
    ("Ich ___ morgens immer. ", ["wasche", "wasche mich", "wäsche"], 1, "'Wasche mich' ist das Reflexivverb 'sich waschen'."),
    ("Er ___ über das Geschenk. ", ["freut", "freut sich", "ist froh"], 1, "'Freut sich' ist das Reflexivverb 'sich freuen'."),
    ("___ du für Politik? ", ["Interessierst", "Interessierst dich", "Magst"], 1, "'Interessierst dich' ist das Reflexivverb 'sich interessieren'."),
    ("Wir ___ auf die Party. ", ["freuen", "freuen uns", "sind glücklich"], 1, "'Freuen uns' ist das Reflexivverb 'sich freuen'."),
    ("___ ihr euch auf den Urlaub? ", ["Freut", "Freut ihr", "Freut ihr euch"], 2, "'Freut ihr euch' ist das Reflexivverb 'sich freuen'."),

    # N-Deklination (der Student, die Studentin)
    ("Der ___ kommt aus Spanien. ", ["Student", "Studentin", "Schüler"], 0, "'Student' ist die maskuline Form."),
    ("Die ___ studiert Medizin. ", ["Student", "Studentin", "Schülerin"], 1, "'Studentin' ist die feminine Form."),
    ("___ Herr Müller ist mein Professor. ", ["Der", "Die", "Das"], 0, "'Der' ist der richtige Artikel für 'Herr'."),
    ("___ Frau Schmidt unterrichtet Mathematik. ", ["Der", "Die", "Das"], 1, "'Die' ist der richtige Artikel für 'Frau'."),
    ("___ Kinder spielen im Garten. ", ["Der", "Die", "Das"], 1, "'Die' ist der richtige Artikel für Plural 'Kinder'."),

    # Adjektivdeklination (der gute Mann, das schöne Haus)
    ("Das ist ___ schöne Blume. ", ["ein", "eine", "ein"], 1, "'Eine schöne Blume' ist richtig, weil 'Blume' feminin ist."),
    ("Er ist ___ guter Freund. ", ["ein", "eine", "ein"], 0, "'Ein guter Freund' ist richtig, weil 'Freund' maskulin ist."),
    ("Wir haben ___ großes Haus. ", ["ein", "eine", "ein"], 2, "'Ein großes Haus' ist richtig, weil 'Haus' neutral ist."),
    ("Sie trägt ___ roten Mantel. ", ["ein", "eine", "ein"], 2, "'Ein roter Mantel' wäre Nominativ, aber hier brauchen wir Akkusativ: 'einen roten Mantel'."),
    ("Ich sehe ___ alten Baum. ", ["ein", "eine", "ein"], 0, "'Einen alten Baum' ist Akkusativ für maskuline Nomen."),

    # Futur I (werden + Infinitiv)
    ("Morgen ___ ich nach Berlin fahren. ", ["fahre", "werde fahren", "bin gefahren"], 1, "'Werde fahren' ist Futur I für zukünftige Handlungen."),
    ("___ du mir später helfen? ", ["Hilfst", "Wirst helfen", "Kannst helfen"], 1, "'Wirst helfen' ist die Futur-Form von 'helfen'."),
    ("Wir ___ das Problem lösen. ", ["lösen", "werden lösen", "haben gelöst"], 1, "'Werden lösen' ist Futur I für zukünftige Handlungen."),
    ("___ ihr morgen kommen? ", ["Kommt", "Werdet kommen", "Könnt kommen"], 1, "'Werdet kommen' ist die Futur-Form von 'kommen'."),
    ("Sie ___ die Prüfung bestehen. ", ["besteht", "wird bestehen", "hat bestanden"], 1, "'Wird bestehen' ist Futur I für zukünftige Handlungen."),

    # Indirekte Fragen (ob, was, wo, wie)
    ("Ich weiß nicht, ___ er kommt. ", ["wann", "ob", "wie"], 1, "'Ob' leitet eine indirekte Ja/Nein-Frage ein."),
    ("Kannst du mir sagen, ___ das Buch liegt? ", ["wo", "was", "wie"], 0, "'Wo' fragt nach dem Ort."),
    ("Weißt du, ___ er heißt? ", ["wie", "was", "wo"], 0, "'Wie' fragt nach dem Namen."),
    ("Ich frage mich, ___ sie das schafft. ", ["ob", "wann", "wie"], 0, "'Ob' leitet eine indirekte Ja/Nein-Frage ein."),
    ("Er hat gefragt, ___ spät es ist. ", ["wie", "was", "wo"], 0, "'Wie spät' fragt nach der Uhrzeit."),

    # Genitiv (des Mannes, der Frau)
    ("Das ist das Auto ___ Vaters. ", ["des", "der", "den"], 0, "'Des Vaters' ist Genitiv für Maskulinum."),
    ("___ Kindes Spielzeug liegt dort. ", ["Des", "Der", "Die"], 0, "'Des Kindes' ist Genitiv für Neutrum."),
    ("Die Tasche ___ Freundin ist rot. ", ["des", "der", "den"], 1, "'Der Freundin' ist Genitiv für Femininum."),
    ("___ Mannes Hut ist schwarz. ", ["Des", "Der", "Die"], 0, "'Des Mannes' ist Genitiv für Maskulinum."),
    ("Das ist das Haus ___ Nachbarn. ", ["des", "der", "den"], 0, "'Des Nachbarn' ist Genitiv für Maskulinum."),

    # Partizip I und II (laufend, gelaufen)
    ("Das ___ Kind ist mein Neffe. ", ["laufende", "gelaufene", "rennende"], 0, "'Laufende' ist Partizip I von 'laufen'."),
    ("___ Buch habe ich gestern gelesen. ", ["Das gelesene", "Das lesende", "Das lesbare"], 0, "'Das gelesene' ist Partizip II von 'lesen'."),
    ("Die ___ Frau ist meine Tante. ", ["lachende", "gelachte", "weinende"], 0, "'Lachende' ist Partizip I von 'lachen'."),
    ("___ Haus wurde verkauft. ", ["Das gebaute", "Das bauende", "Das verkaufende"], 0, "'Das gebaute' ist Partizip II von 'bauen'."),
    ("Der ___ Hund gehört mir. ", ["bellende", "gebellte", "heulende"], 0, "'Bellende' ist Partizip I von 'bellen'."),

    # Konjunktiv I (indirekte Rede)
    ("Er sagt, er ___ müde. ", ["ist", "sei", "wäre"], 1, "'Sei' ist Konjunktiv I für indirekte Rede."),
    ("Sie meint, sie ___ das nicht gewusst. ", ["hat", "habe", "hätte"], 1, "'Habe' ist Konjunktiv I für indirekte Rede."),
    ("Er behauptet, er ___ das Buch gelesen. ", ["hat", "habe", "hätte"], 1, "'Habe' ist Konjunktiv I für indirekte Rede."),
    ("Sie sagt, sie ___ morgen kommen. ", ["wird", "werde", "würde"], 1, "'Werde' ist Konjunktiv I für indirekte Rede."),
    ("Er erklärt, er ___ das Problem lösen. ", ["kann", "könne", "kürde"], 1, "'Könne' ist Konjunktiv I für indirekte Rede."),

    # Präpositionen mit Genitiv (während, wegen, trotz)
    ("___ des Regens bleiben wir zu Hause. ", ["Wegen", "Trotz", "Während"], 0, "'Wegen' verlangt Genitiv und zeigt den Grund an."),
    ("___ der Prüfung war ich nervös. ", ["Wegen", "Trotz", "Während"], 2, "'Während' zeigt eine zeitliche Überlappung an."),
    ("___ seiner Krankheit kommt er nicht. ", ["Wegen", "Trotz", "Während"], 0, "'Wegen' verlangt Genitiv und zeigt den Grund an."),
    ("___ des Lärms kann ich nicht schlafen. ", ["Wegen", "Trotz", "Während"], 0, "'Wegen' verlangt Genitiv und zeigt den Grund an."),
    ("___ aller Mühe hat er es nicht geschafft. ", ["Wegen", "Trotz", "Während"], 1, "'Trotz' verlangt Genitiv und zeigt einen Gegensatz an."),

    # Infinitiv mit 'zu' (versuchen zu, hoffen zu)
    ("Ich versuche, ___ pünktlich zu sein. ", ["zu", "um", "für"], 0, "'Zu' leitet den Infinitiv ein nach 'versuchen'."),
    ("Er hofft, ___ die Prüfung zu bestehen. ", ["zu", "um", "für"], 0, "'Zu' leitet den Infinitiv ein nach 'hoffen'."),
    ("Wir planen, ___ im Sommer zu verreisen. ", ["zu", "um", "für"], 0, "'Zu' leitet den Infinitiv ein nach 'planen'."),
    ("Sie vergisst, ___ die Tür abzuschließen. ", ["zu", "um", "für"], 0, "'Zu' leitet den Infinitiv ein nach 'vergessen'."),
    ("Er beginnt, ___ Deutsch zu lernen. ", ["zu", "um", "für"], 0, "'Zu' leitet den Infinitiv ein nach 'beginnen'."),

    # Nebensätze mit 'dass', 'weil', 'obwohl'
    ("Ich denke, ___ du recht hast. ", ["dass", "weil", "obwohl"], 0, "'Dass' leitet einen Nebensatz ein, der eine Aussage enthält."),
    ("___ es regnet, bleibe ich zu Hause. ", ["Dass", "Weil", "Obwohl"], 1, "'Weil' leitet einen kausalen Nebensatz ein."),
    ("___ ich müde bin, gehe ich ins Bett. ", ["Dass", "Weil", "Obwohl"], 1, "'Weil' leitet einen kausalen Nebensatz ein."),
    ("___ du nicht kommst, mache ich es allein. ", ["Dass", "Weil", "Obwohl"], 0, "'Dass' wäre hier falsch. Richtig wäre 'Falls' oder 'Wenn'."),
    ("___ er krank ist, arbeitet er weiter. ", ["Dass", "Weil", "Obwohl"], 2, "'Obwohl' leitet einen konzessiven Nebensatz ein."),

    # Passiv mit Modalverben (kann gemacht werden, muss gelöst werden)
    ("Das Problem ___ gelöst werden. ", ["kann", "muss", "soll"], 0, "'Kann gelöst werden' ist Passiv mit Modalverb für Möglichkeit."),
    ("Die Aufgabe ___ bis morgen erledigt werden. ", ["kann", "muss", "soll"], 1, "'Musst erledigt werden' ist Passiv mit Modalverb für Pflicht."),
    ("___ das Fenster geöffnet werden? ", ["Kann", "Muss", "Soll"], 0, "'Kann geöffnet werden' ist Passiv mit Modalverb für Möglichkeit."),
    ("Der Brief ___ heute noch abgeschickt werden. ", ["kann", "muss", "soll"], 1, "'Muss abgeschickt werden' ist Passiv mit Modalverb für Pflicht."),
    ("Die Übung ___ von allen gemacht werden. ", ["kann", "muss", "soll"], 2, "'Soll gemacht werden' ist Passiv mit Modalverb für Aufforderung."),

    # Konjunktiv II (Vergangenheit)
    ("Ich ___ gern mehr gereist. ", ["habe", "hätte", "würde"], 1, "'Hätte' ist Konjunktiv II von 'haben' für irreale Wünsche in der Vergangenheit."),
    ("___ du mehr Zeit gehabt, was hättest du gemacht? ", ["Hättest", "Hast", "Würdest haben"], 0, "'Hättest' leitet eine irreale Bedingung in der Vergangenheit ein."),
    ("Er ___ das nicht gesagt. ", ["hat", "hätte", "würde"], 1, "'Hätte' ist Konjunktiv II von 'haben' für irreale Aussagen in der Vergangenheit."),
    ("___ ihr das gewusst, hättet ihr anders gehandelt. ", ["Hättet", "Wüsstet", "Würdet wissen"], 0, "'Hättet' leitet eine irreale Bedingung in der Vergangenheit ein."),
    ("Sie ___ gern länger geblieben. ", ["ist", "wäre", "hat"], 1, "'Wäre' ist Konjunktiv II von 'sein' für irreale Wünsche in der Vergangenheit."),

    # Adjektivdeklination (mit unbestimmtem Artikel)
    ("Das ist ___ interessantes Buch. ", ["ein", "eine", "ein"], 2, "'Ein interessantes Buch' ist richtig, weil 'Buch' neutral ist."),
    ("Er hat ___ neue Idee. ", ["ein", "eine", "ein"], 1, "'Eine neue Idee' ist richtig, weil 'Idee' feminin ist."),
    ("Wir brauchen ___ großen Tisch. ", ["ein", "eine", "ein"], 0, "'Einen großen Tisch' wäre Akkusativ, aber hier brauchen wir Nominativ: 'ein großer Tisch'."),
    ("___ schöne Blume habe ich dir mitgebracht. ", ["Ein", "Eine", "Ein"], 1, "'Eine schöne Blume' ist richtig, weil 'Blume' feminin ist."),
    ("Er ist ___ guter Schüler. ", ["ein", "eine", "ein"], 0, "'Ein guter Schüler' ist richtig, weil 'Schüler' maskulin ist."),

    # Präpositionen mit Akkusativ/Dativ (Wechselpräpositionen)
    ("Ich hänge das Bild ___ die Wand. ", ["an", "auf", "in"], 0, "'An die Wand' ist Akkusativ, weil 'hängen' hier eine Bewegung beschreibt."),
    ("Das Bild hängt ___ der Wand. ", ["an", "auf", "in"], 0, "'An der Wand' ist Dativ, weil 'hängen' hier eine Position beschreibt."),
    ("Ich stelle die Vase ___ den Tisch. ", ["auf", "an", "in"], 0, "'Auf den Tisch' ist Akkusativ, weil 'stellen' eine Bewegung beschreibt."),
    ("Die Vase steht ___ dem Tisch. ", ["auf", "an", "in"], 0, "'Auf dem Tisch' ist Dativ, weil 'stehen' eine Position beschreibt."),
    ("Ich lege das Buch ___ die Tasche. ", ["in", "auf", "an"], 0, "'In die Tasche' ist Akkusativ, weil 'legen' eine Bewegung beschreibt."),

    # Reflexivpronomen (mich, dich, sich, uns, euch)
    ("Ich wasche ___. ", ["mich", "mir", "mein"], 0, "'Mich' ist Akkusativ für das Reflexivpronomen."),
    ("Er freut ___ über das Geschenk. ", ["sich", "ihm", "ihn"], 0, "'Sich' ist das Reflexivpronomen für die 3. Person."),
    ("___ interessierst du? ", ["Dich", "Dir", "Für dich"], 0, "'Dich' wäre Akkusativ, aber hier brauchen wir 'Dich' für 'sich interessieren'."),
    ("Wir freuen ___ auf den Urlaub. ", ["uns", "unsere", "unser"], 0, "'Uns' ist das Reflexivpronomen für die 1. Person Plural."),
    ("___ könnt ihr nicht konzentrieren? ", ["Euch", "Ihr", "Euer"], 0, "'Euch' ist das Reflexivpronomen für die 2. Person Plural."),

    # Vergleichsformen (Komparativ und Superlativ)
    ("Dieses Buch ist ___ als jenes. ", ["interessant", "interessanter", "am interessantesten"], 1, "'Interessanter' ist der Komparativ von 'interessant'."),
    ("Er ist ___ Schüler in der Klasse. ", ["der gute", "der bessere", "der beste"], 2, "'Der beste' ist der Superlativ von 'gut'."),
    ("___ Problem ist das. ", ["Das große", "Das größere", "Das größte"], 1, "'Das größere' ist der Komparativ von 'groß'."),
    ("Sie läuft ___ von allen. ", ["schnell", "schneller", "am schnellsten"], 2, "'Am schnellsten' ist der Superlativ von 'schnell'."),
    ("___ Haus ist das dort? ", ["Das hohe", "Das höhere", "Das höchste"], 2, "'Das höchste' ist der Superlativ von 'hoch'."),

    # Temporale Präpositionen (seit, während, bis)
    ("___ einer Stunde warte ich hier. ", ["Seit", "Während", "Bis"], 0, "'Seit' zeigt den Beginn einer Handlung an."),
    ("___ des Films habe ich geschlafen. ", ["Seit", "Während", "Bis"], 1, "'Während' zeigt eine zeitliche Überlappung an."),
    ("Ich bleibe hier ___ du kommst. ", ["seit", "während", "bis"], 2, "'Bis' zeigt das Ende einer Handlung an."),
    ("___ drei Jahren wohne ich hier. ", ["Seit", "Während", "Bis"], 0, "'Seit' zeigt den Beginn einer andauernden Handlung an."),
    ("___ der Pause trinke ich Kaffee. ", ["Seit", "Während", "Bis"], 1, "'Während' zeigt eine zeitliche Überlappung an."),
]
