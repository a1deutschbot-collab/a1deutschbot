import logging
import os
import random
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
import requests

# Load environment variables
load_dotenv()

# 100 A1-A2 level quiz questions
quiz_questions = [
    # Articles (ein/eine/einen)
    ("Ich habe ___ Apfel. ", ["ein", "eine", "einen"], 2),
    ("Das ist ___ Haus. ", ["ein", "eine", "ein"], 0),
    ("Wir sehen ___ Hund. ", ["ein", "eine", "einen"], 2),
    ("Sie trinkt ___ Wasser. ", ["ein", "eine", "ein"], 0),
    ("Er isst ___ Brot. ", ["ein", "eine", "ein"], 0),
    ("Ich lese ___ Buch. ", ["ein", "eine", "einen"], 1),
    ("___ Kind spielt. ", ["Der", "Die", "Das"], 2),
    ("Ich sehe ___ Katze. ", ["der", "die", "das"], 1),
    ("___ Mann liest. ", ["Der", "Die", "Das"], 0),
    ("Wir haben ___ Auto. ", ["ein", "eine", "einen"], 1),

    # Prepositions (auf, in, unter, an, neben, hinter, vor)
    ("Das Buch liegt ___ Tisch. ", ["auf", "in", "unter"], 0),
    ("Die Tasche ist ___ Stuhl. ", ["auf", "in", "unter"], 1),
    ("Der Schlüssel ist ___ Tür. ", ["auf", "in", "an"], 2),
    ("Die Katze schläft ___ Sofa. ", ["auf", "in", "unter"], 0),
    ("Das Bild hängt ___ Wand. ", ["auf", "in", "an"], 2),
    ("Der Hund sitzt ___ Baum. ", ["auf", "in", "unter"], 2),
    ("Das Heft ist ___ Schublade. ", ["auf", "in", "unter"], 1),
    ("Die Lampe steht ___ Tisch. ", ["auf", "in", "neben"], 2),
    ("Der Ball rollt ___ Bett. ", ["auf", "in", "unter"], 2),
    ("Das Poster klebt ___ Wand. ", ["auf", "in", "an"], 0),

    # Basic verbs (haben, sein, essen, trinken, lesen, spielen, gehen, kommen)
    ("Ich ___ ein Buch. ", ["habe", "bin", "lesen"], 0),
    ("Er ___ einen Apfel. ", ["hat", "ist", "isst"], 2),
    ("Wir ___ Wasser. ", ["haben", "sind", "trinken"], 2),
    ("___ du Deutsch? ", ["Hast", "Bist", "Lernst"], 2),
    ("Sie ___ ein Auto. ", ["hat", "ist", "fährt"], 0),
    ("___ ihr Hunger? ", ["Habt", "Seid", "Esst"], 1),
    ("Er ___ Fußball. ", ["hat", "ist", "spielt"], 2),
    ("___ du müde? ", ["Hast", "Bist", "Schläfst"], 1),
    ("Wir ___ ins Kino. ", ["haben", "sind", "gehen"], 2),
    ("___ ihr Studenten? ", ["Habt", "Seid", "Lernt"], 1),

    # Adjectives (groß, klein, gut, schön, alt, neu, rot, blau)
    ("Das ist ___ Haus. ", ["ein großes", "eine große", "ein großer"], 0),
    ("Sie hat ___ Hund. ", ["ein kleiner", "eine kleine", "ein kleines"], 1),
    ("Er ist ___ Mann. ", ["ein guter", "eine gute", "ein guter"], 0),
    ("Das ist ___ Buch. ", ["ein altes", "eine alte", "ein alt"], 0),
    ("Wir haben ___ Garten. ", ["ein schöner", "eine schöne", "ein schönes"], 2),
    ("___ Kind lacht. ", ["Das kleine", "Die kleine", "Der kleine"], 0),
    ("Sie trägt ___ Kleid. ", ["ein rotes", "eine rote", "ein rot"], 1),
    ("Er kauft ___ Auto. ", ["ein neues", "eine neue", "ein neu"], 0),
    ("___ Stadt ist schön. ", ["Die große", "Das große", "Der große"], 0),
    ("Ich sehe ___ Baum. ", ["ein hoher", "eine hohe", "ein hohes"], 0),

    # Mixed grammar (articles, verbs, prepositions)
    ("___ trinkt ___ Kaffee. ", ["Er/ein", "Sie/eine", "Wir/einen"], 1),
    ("___ liegt ___ Boden. ", ["Der Ball/auf", "Die Katze/unter", "Das Buch/auf"], 1),
    ("___ spielt ___ Garten. ", ["Das Kind/im", "Der Hund/auf", "Die Frau/im"], 0),
    ("___ isst ___ Apfel. ", ["Er/einen", "Sie/eine", "Wir/ein"], 0),
    ("___ steht ___ Tisch. ", ["Die Lampe/auf", "Der Stuhl/neben", "Das Buch/unter"], 0),
    ("___ hat ___ Hund. ", ["Er/einen", "Sie/eine", "Wir/ein"], 0),
    ("___ geht ___ Schule. ", ["Das Kind/in die", "Der Mann/zur", "Die Frau/in die"], 0),
    ("___ liest ___ Buch. ", ["Er/ein", "Sie/eine", "Wir/ein"], 1),
    ("___ wohnt ___ Berlin. ", ["Er/in", "Sie/auf", "Wir/in"], 2),
    ("___ fährt ___ Auto. ", ["Er/mit dem", "Sie/mit dem", "Wir/mit einem"], 0),

    # A2 level: modal verbs (können, müssen, wollen, dürfen)
    ("Ich ___ schwimmen. ", ["kann", "muss", "will"], 0),
    ("Er ___ nach Hause gehen. ", ["kann", "muss", "darf"], 1),
    ("___ du mir helfen? ", ["Kannst", "Musst", "Willst"], 0),
    ("Wir ___ das machen. ", ["können", "müssen", "wollen"], 1),
    ("___ ihr kommen? ", ["Könnt", "Müsst", "Wollt"], 0),
    ("Sie ___ nicht rauchen. ", ["kann", "muss", "darf"], 2),
    ("___ du das Buch? ", ["Kannst lesen", "Musst lesen", "Willst lesen"], 2),
    ("Er ___ nicht hier sein. ", ["kann", "muss", "darf"], 2),
    ("___ wir gehen? ", ["Können", "Müssen", "Dürfen"], 2),
    ("Ich ___ das nicht. ", ["kann verstehen", "muss verstehen", "will verstehen"], 0),

    # A2 level: past tense (Perfekt)
    ("Ich ___ gestern ___. ", ["habe/gelesen", "bin/gegangen", "habe/gespielt"], 1),
    ("Er ___ ___ Apfel ___. ", ["hat/gegessen/einen", "ist/gegangen/ein", "hat/getrunken/einen"], 0),
    ("Wir ___ ___ Film ___. ", ["haben/gesehen/einen", "sind/gegangen/im", "haben/gesprochen/über"], 0),
    ("___ du ___? ", ["Hast/gelernt", "Bist/gegangen", "Hast/geschlafen"], 0),
    ("Sie ___ ___ Buch ___. ", ["hat/gelesen/ein", "ist/gegangen/ins", "hat/geschrieben/ein"], 0),
    ("___ ihr ___? ", ["Habt/gearbeitet", "Seid/geblieben", "Habt/gesprochen"], 0),
    ("Er ___ ___ Auto ___. ", ["hat/gewaschen/das", "ist/gefahren/mit dem", "hat/repariert/das"], 1),
    ("___ wir ___? ", ["Haben/gesprochen", "Sind/geblieben", "Haben/geessen"], 0),
    ("Ich ___ ___ Brief ___. ", ["habe/geschrieben/einen", "bin/gegangen/zum", "habe/gelesen/einen"], 0),
    ("___ du ___? ", ["Hast/gekocht", "Bist/aufgestanden", "Hast/gearbeitet"], 1),

    # A2 level: dative case (mir, dir, ihm, ihr, uns, euch, ihnen)
    ("Ich gebe ___ das Buch. ", ["dir", "ihm", "ihr"], 0),
    ("Er zeigt ___ den Weg. ", ["mir", "dir", "uns"], 1),
    ("Wir helfen ___. ", ["dir", "ihm", "ihr"], 2),
    ("___ gefällt das. ", ["Mir", "Dir", "Ihm"], 0),
    ("Sie schreibt ___ einen Brief. ", ["mir", "dir", "ihnen"], 2),
    ("___ dankt er? ", ["Wem", "Wen", "Was"], 0),
    ("Ich sage ___ die Wahrheit. ", ["dir", "ihm", "ihr"], 1),
    ("___ gehört das? ", ["Wem", "Wer", "Was"], 0),
    ("Er gibt ___ das Geschenk. ", ["mir", "dir", "ihr"], 2),
    ("___ passt das nicht. ", ["Mir", "Dir", "Ihm"], 0),

    # A2 level: accusative case (mich, dich, ihn, sie, es, uns, euch, sie)
    ("Ich sehe ___. ", ["dich", "ihn", "sie"], 0),
    ("Er kennt ___ nicht. ", ["mich", "dich", "uns"], 1),
    ("Wir besuchen ___. ", ["dich", "ihn", "sie"], 2),
    ("___ mag er? ", ["Mich", "Dich", "Sie"], 2),
    ("Sie fragt ___. ", ["mich", "dich", "ihn"], 2),
    ("___ liebt sie? ", ["Wen", "Was", "Wem"], 0),
    ("Ich rufe ___ an. ", ["dich", "ihn", "sie"], 1),
    ("___ versteht er nicht. ", ["Mich", "Dich", "Uns"], 2),
    ("___ siehst du? ", ["Wen", "Was", "Wem"], 0),
    ("Er hört ___ nicht. ", ["mich", "dich", "uns"], 2),
]

# Your custom prompt
CUSTOM_PROMPT = """
# ROLE
Du bist A1DeutschBot, ein **streng regelbasierter** Deutschlehrer für Anfänger.
Deine Antworten **müssen** diesen Regeln folgen:

# REGELN (PFLICHT!)
1. **Begrüßung:**
   - Erste Nachricht: **"Hallo! Ich bin A1DeutschBot."**
   - **Niemals** abweichen!

2. **Antwortstil:**
   - **Nur Deutsch**, **nur 600 häufigste Wörter**.
   - **Maximal 1 Satz (10-15 Wörter)**.
   - **Immer eine Follow-up-Frage stellen** (z. B.: "Und du?", "Was machst du?").
   - **Keine Wiederholungen!** Jede Antwort muss **unterschiedlich** formuliert sein.

3. **Neue Wörter:**
   - Wenn der Nutzer ein **neues Wort** (nicht in den 600) sagt:
     - Antwort: **"Danke! Ich habe das Wort ‘[Wort]’ gelernt."**
     - Ab jetzt **darfst du das Wort nutzen**.

4. **Quiz nach 2 Nachrichten:**
   - **Ignoriere diese Regel** (Quizzes werden vom Code gesteuert).
"""

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hallo! Ich bin A1DeutschBot.")

async def reply_using_mistral(user_message: str, chat_history: list) -> str:
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
        "temperature": 0.3,  # Balance between creativity and control
        "max_tokens": 20,
    }
    response = requests.post(os.getenv('MISTRAL_API_URL'), headers=headers, json=data)
    logger.info(f"Mistral raw response: {response.json()}")
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        logger.error(f"Mistral API error: {response.text}")
        return "Entschuldigung, ich habe ein Problem. Versuche es später nochmal."

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
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
                feedback = f"Fast! Die richtige Antwort ist {correct_option}."
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
        # Select a quiz that hasn't been used yet in this conversation
        available_quizzes = [q for q in quiz_questions if q not in used_quizzes]
        if not available_quizzes:
            available_quizzes = quiz_questions.copy()  # Reset if all have been used
            used_quizzes = []

        question, options, correct_index = random.choice(available_quizzes)
        used_quizzes.append((question, options, correct_index))
        context.user_data["used_quizzes"] = used_quizzes

        quiz = f"Weißt du die richtige Antwort? {question}(a) {options[0]} (b) {options[1]} (c) {options[2]}"
        if len(options) > 3:
            quiz += f" (d) {options[3]}"
        chat_history.append({"role": "assistant", "content": quiz})
        context.user_data["current_quiz"] = {"question": question, "options": options, "correct_index": correct_index}
        await update.message.reply_text(quiz)
        return

    # Get Mistral's response
    bot_reply = await reply_using_mistral(user_message, chat_history)
    chat_history.append({"role": "assistant", "content": bot_reply})
    await update.message.reply_text(bot_reply)

def main() -> None:
    application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()