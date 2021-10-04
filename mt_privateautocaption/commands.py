#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) StarKing Developers

import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

USERNAME=Config.BOT_USERNAME


# start_Msg, help_msg, about_msg
# Team Mo Tect
MT = "@StarKingBots"
CP = "{file_name}"


@Client.on_message(filters.private & filters.command("start"))
async def start_meg(client, update):
    text = f"""<b> 👋Hello {update.from_user.mention}\n\nI am StarKing AutoCaption bot\n\nAll you have to do is add me to your channel and I will show you my power\n\nFor more info check help Button\n\n {MT}</b>"""
    reply_markup =  InlineKeyboardMarkup( [[
        InlineKeyboardButton("help🆘", callback_data="heroku"),
        InlineKeyboardButton("PSA Movies🎥", url="https://t.me/PSALK")
        ],[
        InlineKeyboardButton("✒ Current Caption", callback_data="currentcaption")
        ]]
    )
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

@Client.on_callback_query(filters.regex(r"^(heroku|about|motech|currentcaption)$"))
async def callback_data(client, update: CallbackQuery):

    query_data = update.data

    if query_data == "heroku":
        buttons = [[
            InlineKeyboardButton("🎥 PSA LK 🎥", url="https://t.me/PSALK"),
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("❌️Close", callback_data="motech"),
            InlineKeyboardButton("About↗️", callback_data="about")
            ]]

        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            f"""<b>🔻AutoCaption Bot🔻\n\nIf you want to change your Caption,\nChange it from Heroku.\n\nHeroku 👉 https://dashboard.heroku.com\n\n🎥Join to Our PSA LK channel for get latest PSA Rips./\n\n {MT}</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    if query_data == "currentcaption":
        buttons = [[
            InlineKeyboardButton("🎥 PSA LK 🎥", url="https://t.me/PSALK"),
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("❌️Close", callback_data="motech"),
            InlineKeyboardButton("About↗️", callback_data="about")
            ]]

        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            f"""<b><u>🔻Current Caption</u>🔻\n\n<code>Name: {CP}\n\n@PSALKSERIES</code>\n\n'Current Caption' is not stable.😅 I'll give you, **Custom Caption** mode in next update.♥\n\n🎥Join to Our PSA LK channel for get latest PSA Rips.\n\n {MT}</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    if query_data == "about":
        buttons = [[
            InlineKeyboardButton("🎥 PSA LK 🎥", url="https://t.me/StarKingBots"),
            ],[
            InlineKeyboardButton("🏠Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("🔙Back", callback_data="heroku"),
            InlineKeyboardButton("❌️Close", callback_data="motech")
            ]]

        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            """<b>➪ Bot Name: StarKing AutoCaptionBot</b>\n\n➪ <b>Framework : Pyrogram</b>\n\n➪<b> Language : Python</b>\n\n➪<b> Server : StarKing Cloud</b> \n\n<b>➪ Version : 1.5.0</b>\n\n<b>➪ Developer :  @MrTonyStarKing</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "motech":
        await update.message.delete()
