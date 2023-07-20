from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL2
from pyrogram.types import InlineKeyboardButton


def start_button(client, is_fsub=False):
    buttons = []

    if FORCE_SUB_GROUP:
        buttons.append([
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
        ])

    if FORCE_SUB_CHANNEL2:
        buttons.append([
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink3),
        ])

    if FORCE_SUB_CHANNEL and not is_fsub:
        if FORCE_SUB_GROUP:
            buttons[-1].append(
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink)
            )
        else:
            buttons.append([
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ])

    return buttons


def fsub_button(client, message):
    buttons = []

    if FORCE_SUB_GROUP:
        buttons.append([
            InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
        ])

    if FORCE_SUB_CHANNEL2:
        buttons.append([
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink3),
        ])

    if FORCE_SUB_CHANNEL:
        if FORCE_SUB_GROUP:
            buttons[-1].append(
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink)
            )
        else:
            buttons.append([
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ])

    try:
        if message.command and len(message.command) > 1:
            buttons.append([
                InlineKeyboardButton(
                    text="ᴄᴏʙᴀ ʟᴀɢɪ",
                    url=f"https://t.me/{client.username}?start={message.command[1]}",
                )
            ])
    except IndexError:
        pass

    return buttons
