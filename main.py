from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 30
PROMISED_UP = 5


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
upload_speed = float(bot.up)
download_speed = float(bot.down)

if upload_speed<float(PROMISED_UP) or download_speed< float(PROMISED_DOWN):
    print("The speed is good bruv, no need to tweet")
    bot.tweet_at_provider()





























