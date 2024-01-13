# Reddit Post to Video Converter

Currently the concept is to scrape subreddits and convert the text posts to short form videos.

# TODO:

- [ ] Complete generate_video.sh script by adding arguments, making it executable, etc.
- [x] Find free tts service to generate audio
- [ ] Fully automate finding posts and generating the videos
- [ ] Make videos HQ at 1080p
- [ ] Add front-end
- [ ] Add actual back-end
- [ ] Make repo user friendly (lol)

## Required Installations

- python packages: Can be installed via requirements.txt eg:`pip install -r /path/to/requirements.txt`
- [whisper](https://github.com/openai/whisper): For generating the subtitle srt files
- [ffmpeg](https://ffmpeg.org/): To render the subtitles onto the video
- [Komika Axis Font](https://www.dafont.com/komika-axis.font): Current font being used for the subtitles

It's also necessary to save a background video right now, named as background.mp4 in the output directory.

# How to Find Session ID for TikTok:

1. Open TikTok webapp www.TikTok.com
2. Open dev tools
3. Naviagte to "Application" section
4. Go to storage --> cookies --> https://www.tiktok.com
5. Search "sessionid"
6. Copy value and set as TIKTOK_SESSION_ID environment variable
