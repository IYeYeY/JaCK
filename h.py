from pyrogram import Client

api_id = 28509955
api_hash = "4388e8e3adff0695399f439dcae25436"
bot_token = "7731817398:AAHvalp5MphnewYhIbOnhvTD2R3EawcbXCY"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
