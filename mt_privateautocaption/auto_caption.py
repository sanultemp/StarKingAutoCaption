#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) StarKing Developers

import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

CAPTION_TEXT=Config.CAPTION
BUTTON_TEXT=Config.BUTTON_TEXT
URL_LINK=Config.URL_LINK


@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    kopp, _ = get_file_id(message)
    await message.edit(f"Name: <code>{kopp.file_name}</code>\n\n<b>{CAPTION_TEXT}</b>")

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                return obj, obj.file_id
