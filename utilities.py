import srt
import translators as ts
import whisper
from dict import lang, translators
from whisper.utils import write_srt
from pathlib import Path
from moviepy.editor import *


def video_audio(user_input, audio_name):
    video = VideoFileClip(user_input)
    audio = video.audio
    audio.write_audiofile(f'temp/audio/{audio_name}.mp3')
    video.close()


def whisper_run():
    filename = "original_audio.mp3"
    input_directory = "temp/audio"
    input_file = f"{input_directory}/{filename}"

    model = whisper.load_model("base")
    result = model.transcribe(input_file)
    output_directory = "temp/subtitles"

    with open(Path(output_directory) / ("original_audio" + ".srt"), "w") as srt:
        write_srt(result["segments"], file=srt)


def translator(option1, option2, option3):
    with open('temp/subtitles/original_audio.srt', 'r') as f:
        srt_text = f.read()

    srt_generator = srt.parse(srt_text)

    with open(f'temp/subtitles/output_{option2}.srt', 'w', encoding="utf-8") as f:
        temp = []
        for subtitle in srt_generator:
            # Translate the subtitle text
            result = ts.translate_text(subtitle.content, translator=translators[option3], from_language=lang[option1],
                                       to_language=lang[option2])

            # Update the subtitle text with the translated text
            subtitle.content = result

            # Appending to temp list
            temp.append(subtitle)

        # Write the updated subtitle to the output file
        f.write(srt.compose(temp))
