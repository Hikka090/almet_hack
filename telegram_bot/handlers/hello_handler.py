from aiogram import types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import F
from telegram_bot.routers.hello_router import hello_router as router

@router.message(Command("start"))
async def handle_start_command(msg: Message):
  await msg.answer(text="Привет 😉. Сейчас мы придумываем темы")