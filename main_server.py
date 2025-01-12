from flask import Flask, render_template, request
from weather_file import get_current_weather
from waitress import serve
import asyncio
from telegram import Update, Bot, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/weather")
def get_weather():
    # from the html class id which is city we request it as an arugement so we can from our python code we can put in values to the html layout
    city = request.args.get("city")

    # check for empty st onlyrings or strings with omly space
    # the .strip will remove space from a users input
    if not bool(city.strip()):
        city = "kansas city"

    weather_data = get_current_weather(city)

    # city is not found by API
    if not weather_data["cod"] == 200:
        return render_template("city_not_found.html")

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data ['main']['temp']: .1f}",
        feels_like=f"{weather_data['main']['feels_like']: 1f}",
    )

# Replace with your actual Telegram Bot Token
TOKEN = "7431630043:AAHAgm1fQRGVCJVgPFPvpXXUAx2Ni1LpG_I"
BOT_USERNAME = "@Phenom001bot"

bot = Bot(token=TOKEN)
application = Application.builder().token(TOKEN).concurrent_updates(True).rate_limiter(None).build()

# START COMMAND HANDLER
async def start_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chat_id = update.message.chat_id

        # Inline Buttons
        inline_keyboard = [
            [InlineKeyboardButton("Register Now", callback_data="register")],
            [InlineKeyboardButton("Learn More", callback_data="learn_more")]
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard)

        Learn = "/help"
        Register = "/register"

        reply_keyboard = [[Learn, Register]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

        await update.message.reply_text('Hey there! I am Your Phenom Assistant™😊', reply_markup=markup)
        await asyncio.sleep(2)

        await update.message.reply_text(
            "Are you curious on knowing what Phenom is and how you can earn with it?\nWell, don't worry anymore because I got you covered😃"
        )
        await asyncio.sleep(3)

        await update.message.reply_text(
            "Get Acquainted with Phenom! 🤩\n\nI can provide you with in-depth knowledge about how Phenom operates and the numerous benefits of having a Phenom account. Let's dive right in and get you acquainted with the advantages Phenom offers!"
        )
#https://drive.google.com/uc?export=download&id=13zQo6CYogj-c6Gn1TMpsK5vlowGzELE-
        video_url = "https://drive.google.com/uc?export=download&id=1JndlKQSI6VEv7LojoxaMFgkmUAnQ-4RA"
        v_caption = (
            "⭕ HOW CAN I ASSIST YOU TODAY?\n\n\n♻️ Help\n\n♻️ Register\n\n🔥Imagine Making Money By Just Playing Games And Tapping On Phenom 😱.\n"
            "Working for someone is good, but working for yourself is better. As a human being, learning to sell should be your ultimate priority.\n"
            "Humans buy every day.\n\nThose who sell make all the money. Do you want to make sales while you sleep? That's where PHENOM comes in, giving you the opportunity to make money online through different means.\n\nClick on Learn to know more about Phenom\n\n                      OR\n\n Click Register to get started now!"
        )
        await asyncio.sleep(3)
        await context.bot.send_video(chat_id=chat_id, video=video_url, caption=v_caption, parse_mode='Markdown', reply_markup=inline_markup)
    except Exception as e:
        print(f"Error in start_comm: {e}")

# HOW BENEFIX WORKS COMMAND HANDLER
async def how_benefix_works_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chat_id = update.message.chat_id
        #https://drive.google.com/uc?export=download&id=1rpyx2TpWKPLJExlnnHqQ776gsXOS0UxO
        img_url2 = 'https://drive.google.com/uc?export=download&id=1hA78j0YsfEXNBXX20XITZTytdeFMnEHx'

        # Inline Buttons
        inline_keyboard = [
            [InlineKeyboardButton("Register Now", callback_data="register")]
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard)

        # Keyboard Buttons
        Learn = "/help"
        Register = "/register"

        reply_keyboard = [[Learn, Register]]
        markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
        caption2 =("Phenom is NOT a Pyramid scheme, neither is it a Rob peter to pay paul program!\n\nAt Phenom, everything we do is 100% legitimate. We employ diverse, sustainable methods to generate funds and ensure our users are paid reliably.\n\nAbove are some of our methods of generating revenue🏦\nWe operate with complete transparency and are committed to maintaining the trust of our members.\nEvery process is carefully designed to ensure long term sustainability and fairness.\nJoin Phenom today and be rest assured that any amount of money you make, you’ll definitely get paid 🤝💰")

        
        await context.bot.send_photo(chat_id=chat_id, photo=img_url2, caption=caption2, reply_markup=markup)
        await update.message.reply_text(
                    "        *💜 PHENOM EARNING STRUCTURE SIMPLIFIED* ⬇️\n\n"
                    "REGISTRATION FEE IS  ₦8000\n\n"
                    "▫️After registration, you'll receive a welcome bonus of ₦7000 instantly to your dashboard.\n\n"
                    "You can borrow loan with phenom loan to start up that small business you have always wanted to start"
                    "▫️You earn ₦2000 daily when you participate in Phenom Quiz\n\n"
                    "▫️You earn N1,500 per 1k views on the Phenom Tiktok Monetization\n\n"
                    "▫️ You'll earn N500 daily by mining the Phenom Coin/ppt\n\n"
                    "▫️You also earn N1,000 daily by claiming rewards - RewardRush\n\n"
                    "▫️ Affiliate commission: N7,100\n"
                    "➖ Indirect bonus: N200\n"
                    "➖2nd indirect: N100\n"
                    "- Phenom Loan: this feature enables users to get financial support from Phenom without collateral\n\n"
                    "- ⁠You can also Mine phenom coin with your mobile phone and earn in Dollars\n\n"
                    "Referral is *NOT* compulsory.\n"
                    "Withdrawal is on Monday, Wednesday, and Fridays 5 pm to 6 pm with a Minimum of 14K\n"
                    "Click *Register* to get started now\n",reply_markup=inline_markup
                )

    except Exception as e:
        print(f"Error in how_benefix_works_comm: {e}")

# REGISTRATION COMMAND HANDLER
async def benefix_registration_comm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chat_id = update.message.chat_id
        #https://drive.google.com/uc?export=download&id=1KMTBHzPuBcLIC9GQuedvK46aSBaVFDuR
        img_url3 = 'https://drive.google.com/uc?export=download&id=1c2T0H6vzA-v8zQfka1XIqU3oOtT8HTDe'

        message0 = (
            "Thank you for choosing Phenom, your premier digital marketing platform! We’re thrilled to have you join us.\n\n"
            "Registration fee is ₦8,000 if there was a discount please send it the exact amount⏳. You can register securely by chatting our Recommended Verified Phenom Agent, ensuring a fast, safe, and secure Registration process.\n\n"
            "NOTE: After Successful Registration, You Are Required To Take Your Proof Of Payment **PHOTO** And Head Back To The Phenom App To Complete Your Phenom Account Registration\n\n(Invalid Payment Proofs Will Be Rejected)"
        )
        await asyncio.sleep(2)
        await context.bot.send_photo(chat_id=chat_id, photo=img_url3, caption=message0, parse_mode='Markdown')
        await asyncio.sleep(3)
        await update.message.reply_text("Hold On We're Connecting You With Our Verified Agent....")
        await asyncio.sleep(12)
        await update.message.reply_text(
            "Hey dear") 
        await asyncio.sleep(1)
        await update.message.reply_text(
            "I am gift, the agent currently on sit and I will be the one to process your Phenom registration.") 
        await asyncio.sleep(1)
        await update.message.reply_text(
            "To proceed with your account creation or purchase your coupon code, kindly make payment to the account details below ⬇️ \n\n"
            "\n\nPAY HERE FOR FAST REGISTRATION👇🏻\n\n"
            "Registration is N8,000 or (special discount of 7,500). \n\n"
            "                       Ibrahim gift\n"
            "                       2074213416\n"
            "                       KUDA\n____\n\n"
            "After payment, send your Proof Of Payment for confirmation. Immediately your payment is confirmed, your account will be created/activated and sent to you."
        )
        await asyncio.sleep(3)
        await update.message.reply_text(
            "📌Note: Our Support team is active 24/7 to validate your payment. Once validated, your account will be activated immediately, and you will be automatically added to our official VIP Group. Ensure you keep your username and password safe, as these will be required to log in to your Phenom account.\n\n"
            "📞 CONTACT OUR OFFICIAL SUPPORT TEAM: 💢[Contact Us](https://t.me/BenefixVerificationTeam?text=%0AHey%20Phenom%20Team,%20I%20Am%20Interested%20In%20Phenom,%20Please%20I%20Need%20Guide%20On%20How%20%20I%20Can%20Get%20Started%20With%20Phenom)💢\n\n"
            "Be rest assured, with Phenom, your registration process is fast, safe, and very secure. We’re excited to help you start your journey with us!\n\n"
            "Warm regards, The Phenom Team",
            parse_mode='Markdown'
        )
        await asyncio.sleep(3)
    except Exception as e:
        print(f"Error in benefix_registration_comm: {e}")

# HANDLE MESSAGES
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        print("Received a message")
        message_type: str = update.message.chat.type
        text: str = update.message.text
        print(f'user({update.message.chat.id} in {message_type}: "{text}")')

        if message_type == "group":
            if BOT_USERNAME in text:
                new_text: str = text.replace(BOT_USERNAME, "").strip()
                response: str = handle_response(new_text)
            else:
                return
        else:
            response: str = handle_response(text)

        print("bot:", response)
        await update.message.reply_text(response)
    except Exception as e:
        print(f"Error in handle_message: {e}")
# INLINE BUTTON CALLBACK HANDLER
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    try:
        if query.data == "register":
            await benefix_registration_comm(query, context)
        elif query.data == "learn_more":
            await how_benefix_works_comm(query, context)
    except Exception as e:
        print(f"Error in button_callback: {e}")

# RESPONSE HANDLER
def handle_response(text: str) -> str:
    processed: str = text.lower()
    if "phenom" in processed:
        return "TO REGISTER FOR YOUR PHENOM ACCOUNT PLEASE USE THE COMMAND /register \n\n OR\n\n TO KNOW MORE ABOUT PHENOM USE THE COMMAND /help😊"
    if "account" in processed:
        return (
            "TO HAVE AN ACCOUNT WITH PHENOM, IT'S COMPULSORY YOU MAKE A ONE TIME FEE PAYMENT OF N8,000.\n\n"
            "BUT GUESS WHAT!🤩\n"
        "WE ARE HOSTING AN EXCLUSIVE DISCOUNT OF N7,500 INSTEAD OF N8,000."
        )
    else:
        return "Sorry, I didn't understand that. Use /help to see available commands."

# MAIN FUNCTION
def main():
    application.add_handler(CommandHandler("start", start_comm))
    application.add_handler(CommandHandler("help", how_benefix_works_comm))
    application.add_handler(CommandHandler("register", benefix_registration_comm))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
     serve(main(), host="0.0.0.0", port=8000)
