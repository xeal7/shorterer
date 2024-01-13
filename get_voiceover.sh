#!/bin/bash

FILE_NAME=$1
SESSION_ID=$2

python3 tiktok_tts.py -v "en_us_006" -f "$FILE_NAME" --session "$SESSION_ID" --name "voiceover.mp3"
mv voiceover.mp3 output/voiceover.mp3