#!/bin/bash
cd output 

# generate srt file
whisper "voiceover.mp3" --model "medium" --language "English" --output_format "srt" --word_timestamps "True" --max_words_per_line 1

# add audio to video
ffmpeg \
    -i background.mp4 -i voiceover.mp3\
    -c:v copy \
    -map 0:v -map 1:a \
    -y output.mp4 

# add subtitles to video
ffmpeg -i output.mp4 -vf "subtitles=voiceover.srt:force_style='Fontname=Komika Axis,Alignment=10,PrimaryColour=&H03fcff,Fontsize=35'" output_srt.mp4