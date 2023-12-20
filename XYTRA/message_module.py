# modules/message_module.py

import os
import requests
import logging
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from config import GPT_API_URL

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def process_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text

    if update.message.voice:
        try:
            processing_audio_message = update.message.reply_text("Listening to your voice...")

            file_id = update.message.voice.file_id
            file = update.message.bot.get_file(file_id)
            ogg_path = 'audio.ogg'
            file.download(ogg_path)

            wav_path = 'audio.wav'
            convert_command = f'ffmpeg -i {ogg_path} -vn -acodec pcm_s16le -ar 44100 -ac 2 {wav_path}'
            os.system(convert_command)

            audio = AudioSegment.from_wav(wav_path)
            chunks = split_on_silence(audio, silence_thresh=-40)

            recognizer = sr.Recognizer()
            recognized_text = ""

            converting_text_message = update.message.reply_text("Converting voice to text...")

            for i, chunk in enumerate(chunks):
                chunk.export(f'chunk_{i}.wav', format='wav')
                with sr.AudioFile(f'chunk_{i}.wav') as source:
                    audio_data = recognizer.record(source)
                    try:
                        text = recognizer.recognize_google(audio_data)
                        recognized_text += f"{text} "
                    except sr.UnknownValueError:
                        pass

            os.remove(ogg_path)
            os.remove(wav_path)
            for i in range(len(chunks)):
                os.remove(f'chunk_{i}.wav')

            if recognized_text.strip():
                user_input = recognized_text.strip()

        except Exception as e:
            logger.error(f"Error processing voice message: {str(e)}")

    processing_message = update.message.reply_text("Please wait, generating answer...")

    try:
        response = requests.get(f"{GPT_API_URL}/?question={user_input}")

        if response.status_code == 200:
            result = response.json()

            if "join" in result:
                del result["join"]

            answer = result.get("answer", "No answer received from ChatGPT.")
            button_text = "BHOOLA"
            button_url = "https://t.me/CODERS_ZONE"

            keyboard = [[InlineKeyboardButton(button_text, url=button_url)]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            processing_message.edit_text(answer, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)

        else:
            processing_message.edit_text("Error communicating with ChatGPT API.")

    except requests.exceptions.RequestException as e:
        processing_message.edit_text(f"Error: {str(e)}. Please try again later.")

    except Exception as e:
        processing_message.edit_text(f"Unexpected error: {str(e)}. Please try again later.")
    finally:
        processing_audio_message.delete()
        converting_text_message.delete()
          
