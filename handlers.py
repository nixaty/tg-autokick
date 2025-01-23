from aiogram import types, enums
from aiogram import Router
from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.types import ChatMemberUpdated, Message
import texts


router = Router()


@router.message()
async def message_handler(msg: Message):
    bot_member = await msg.chat.get_member(msg.bot.id)

    if (msg.content_type == enums.ContentType.LEFT_CHAT_MEMBER) or (msg.content_type == enums.ContentType.NEW_CHAT_MEMBERS):
        if bot_member.can_delete_messages:
            await msg.delete()


@router.chat_member()
async def chat_member_handler(event: ChatMemberUpdated):
    new_member = event.new_chat_member
    bot_member = await event.chat.get_member(event.bot.id)

    if (not event.invite_link) and (event.from_user.id == new_member.user.id):
        if bot_member.can_restrict_members:
            if isinstance(event.new_chat_member, types.ChatMemberMember):
            
                await event.bot.ban_chat_member(event.chat.id, new_member.user.id)
                await event.bot.unban_chat_member(event.chat.id, new_member.user.id)
