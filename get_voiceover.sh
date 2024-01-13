#!/bin/bash

# HOW TO FIND SESSION ID:
# 1. Open TikTok webapp www.TikTok.com
# 2. Open dev tools
# 3. Naviagte to "Application" section
# 4. Go to storage --> cookies --> https://www.tiktok.com
# 5. Search "sessionid"
# 6. Copy value and use as argument

FILE_NAME=$1
SESSION_ID=$2

python3 tiktok_tts.py -v "en_us_006" -f "$FILE_NAME" --session "$SESSION_ID" --name "voiceover.mp3"
mv voiceover.mp3 output/voiceover.mp3