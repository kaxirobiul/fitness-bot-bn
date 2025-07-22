import telebot
from datetime import datetime

# 🔁 এখানে তোমার BotFather থেকে নেওয়া টোকেন বসাও
TOKEN = '8041959839:AAEHcsnDUIO3bET_6nPl3-N-CO8UczcpwR4'
bot = telebot.TeleBot(TOKEN)

# 🌅 Start Command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🌟 স্বাগতম ফিটনেস ও ডায়েট বটে!\n\nকমান্ডসমূহ:\n/diet - আজকের ডায়েট প্ল্যান\n/exercise - আজকের এক্সারসাইজ\n/weight - ওজন ট্র্যাক করুন\n/tips - স্বাস্থ্য টিপস")

# 🥗 Diet Command
@bot.message_handler(commands=['diet'])
def send_diet(message):
    diet = "🍚 সকালের খাবার:\n- ১ টা সিদ্ধ ডিম\n- ১ টা ড্রাই রুটি\n\n🍲 দুপুর:\n- ১ কাপ ভাত\n- ১৫০g চিকেন/মাছ\n- সবজি\n\n🥗 রাত:\n- ১ টা স্যালাড\n- ১ টা ডিম\n- ১ গ্লাস দুধ\n\n💧 পানি পান: ৮-১০ গ্লাস"
    bot.reply_to(message, diet)

# 🏋️ Exercise Command
@bot.message_handler(commands=['exercise'])
def send_exercise(message):
    exercise = "🏃 আজকের ব্যায়াম:\n\n1. ২০ মিনিট হাঁটা\n2. ১৫ বার স্কোয়াট\n3. ১০ বার পুশ-আপ\n4. ৩০ সেকেন্ড প্ল্যাঙ্ক\n\n✅ নিয়মিত করলেই ওজন কমবে!"
    bot.reply_to(message, exercise)

# 🧠 Tips Command
@bot.message_handler(commands=['tips'])
def send_tips(message):
    tips = "🧠 স্বাস্থ্য টিপস:\n\n- খাওয়ার ৩০ মিনিট আগে পানি পান করো\n- রাতে বেশি খাবার পরিহার করো\n- পর্যাপ্ত ঘুম খুব দরকার\n- মোবাইল স্ক্রিন টাইম কমাও"
    bot.reply_to(message, tips)

# 📊 Weight Tracker (simple)
@bot.message_handler(commands=['weight'])
def track_weight(message):
    now = datetime.now()
    bot.reply_to(message, f"📅 আজকের তারিখ: {now.strftime('%d-%m-%Y')}\n⚖️ তোমার বর্তমান ওজন লিখে রাখো (উদা: 85kg)। ভবিষ্যতে তুলনা করতে পারবে!")

# 🔁 Loop to keep bot running
print("✅ Bot চলছে...")
bot.infinity_polling()