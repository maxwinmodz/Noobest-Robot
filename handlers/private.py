from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**Hey, I'm {bn} π΅

I'm Private music of @Anurag_1711 For group's voice call. Developed by [π»π ππ«πͺπΆπ‘](https://t.me/Anurag_1711).

If you want to add this Bot in your group Contact @Anurag_1711**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π»π ππ«πͺπΆπ‘", url="https://t.me/Anurag_1711")
                  ],[ 
                    InlineKeyboardButton(
                        "π»ππ₯π’π¨π£", url="https://t.me/TheDenominators_xD"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**π‘πΌπΌπ―π²ππ π₯πΌπ―πΌπ π’π»πΉπΆπ»π²β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π»πππ’π¨π§ π ππ«πͺπΆπ‘", url="https://t.me/ABOUTMAXWiN")
                ]
            ]
        )
   )


