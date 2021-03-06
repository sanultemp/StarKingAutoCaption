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
    text = f"""<b> ๐Hello {update.from_user.mention}\n\nI am StarKing AutoCaption bot\n\nAll you have to do is add me to your channel and I will show you my power\n\nFor more info check help Button\n\n {MT}</b>"""
    reply_markup =  InlineKeyboardMarkup( [[
        InlineKeyboardButton("help๐", callback_data="heroku"),
        InlineKeyboardButton("PSA Movies๐ฅ", url="https://t.me/flixcimaslk")
        ],[
        InlineKeyboardButton("โ Current Caption", callback_data="currentcaption")
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
            InlineKeyboardButton("๐ฅ ยฐ๐๐๐๐ซ ๐๐๐ก๐๐ ๐ยฐ ๐ฅ", url="https://t.me/flixcimaslk"),
            ],[
            InlineKeyboardButton("๐ Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("โ๏ธClose", callback_data="motech"),
            InlineKeyboardButton("Aboutโ๏ธ", callback_data="about")
            ]]

        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            f"""<b>๐ปAutoCaption Bot๐ป\n\nIf you want to change your Caption,\nChange it from Heroku.\n\nHeroku ๐ https://dashboard.heroku.com\n\n๐ฅJoin to Our ยฐ๐๐๐๐ซ ๐๐๐ก๐๐ ๐ยฐ channel for get latest Movies./\n\n {MT}</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    if query_data == "currentcaption":
        buttons = [[
            InlineKeyboardButton("๐ฅ ยฐ๐๐๐๐ซ ๐๐๐ก๐๐ ๐ยฐ ๐ฅ", url="https://t.me/flixcimaslk"),
            ],[
            InlineKeyboardButton("๐ Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("โ๏ธClose", callback_data="motech"),
            InlineKeyboardButton("Aboutโ๏ธ", callback_data="about")
            ]]

        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            f"""<b><u>๐ปCurrent Caption</u>๐ป\n\n<code>{CP}\n\n๐๐๐๐ซ ๐๐๐ก๐๐ ๐ โขยฐ\n@Flix_CinemaSL</code>\n\n'Current Caption' is not stable.๐ I'll give you, **Custom Caption** mode in next update.โฅ\n\n๐ฅJoin to Our ยฐ๐๐๐๐ซ ๐๐๐ก๐๐ ๐ยฐ channel for get latest Movies.\n\n {MT}</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    if query_data == "about":
        buttons = [[
            InlineKeyboardButton("๐ฅ ยฐ๐๐๐๐ซ ๐๐๐ก๐๐ ๐ยฐ ๐ฅ", url="https://t.me/flixcimaslk"),
            ],[
            InlineKeyboardButton("๐ Home", url=f"https://t.me/{USERNAME}?start=start"),
            InlineKeyboardButton("๐Back", callback_data="heroku"),
            InlineKeyboardButton("โ๏ธClose", callback_data="motech")
            ]]

        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.edit_text(
            """<b>โช Bot Name: StarKing AutoCaptionBot</b>\n\nโช <b>Framework : Pyrogram</b>\n\nโช<b> Language : Python</b>\n\nโช<b> Server : StarKing Cloud</b> \n\n<b>โช Version : 1.5.0</b>\n\n<b>โช Developer :  @MrTonyStarKing</b>""",
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "motech":
        await update.message.delete()
