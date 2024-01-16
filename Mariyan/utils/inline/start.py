from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from Mariyan import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⚡ 𝐀ᴅᴅ 𝐌𖾔 𝐓𖽙 𝐘ᴏ𝞄૨ 𝐁𖽖𐌱ᵧ 🌟",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="💋 𝐇𖽞𖾘𖽳 😼",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🌟𝐒𖽞𖾓𖾓ᛧ𖾚ꞔ𖾗⚡", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌟𝐌𖽖𖽹𖽨𖾓𖽖ᛧ𐬜𖽞𖽸❤️‍🩹", user_id=OWNER),
            InlineKeyboardButton(
                text="⚡𝐒𖽪𖽳𖽳𖽙𖽸𖾓💛", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⚡ 𝐀ᴅᴅ 𝐌𖾔 𝐓𖽙 𝐘ᴏ𝞄૨ 𝐆𖽸𖽙𖽪𐌛 🌟",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🩹𝐇𖽞𖾘𖽳😼", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="ᴍᴀɪɴᴛᴀɪɴᴇʀ", user_id=OWNER),
            InlineKeyboardButton(
                text="⚡𝐒𖽪𖽳𖽳𖽙𖽸𖾓👑", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🌟𝐒𖽙𖽪𖽸𖽽𖽞 𝐂𖽙𖽴𖽞💋", url=f"{config.UPSTREAM_REPO}"
                )
        ],
     ]
    return buttons
