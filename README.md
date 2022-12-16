# YouTube Download Toolkit

This toolkit is based on [yt-dlp](https://github.com/yt-dlp/yt-dlp) which is keeping up to date with the inactive [youtube-dlc](https://github.com/blackjack4494/yt-dlc). The aim of this toolkit is to ease the use of `yt-dlp`. In particular, the first version of this toolkit focuses on two functions, as follows:

- Download video and audio in best format
- Download video and audio in best format *together with subtitle*

## Dependencies

`yt-dlp` is the important dependency of this program, together with `ffmpeg` libraries. If you are using macOS or Linux, you can install the two dependencies via [`brew`](https://brew.sh/) which is a popular package manager for macOS or Linux. In case of Microsoft Windows, you can download the executable file of `yt-dlp` at [here](https://github.com/yt-dlp/yt-dlp/releases/).

## How to use the program

Don't worry, this program is easy to use 😉

You can print the help by executing `$ python ytdl.py -h` command in Terminal/CMD environment.

If you want to download a YouTube video in the best audio and video format, you execute the following command:

`$ python ytdl.py "YOUTUBE_URL"`

Example: `$ python ytdl.py "https://www.youtube.com/watch?v=q2viJSYyKio"`

If the video has subtitles, including the auto generated one, you can download the video and audio in the best format together with its subtitle in `vtt` format. The command is as follows:

`$ python ytdl.py --sub "YOUTUBE_URL"`

Example: `$ python ytdl.py --sub "https://www.youtube.com/watch?v=q2viJSYyKio"`

## Add `ytdl.py` to system path

I recommend you add the `ytdl.py` program to the system path, so you can run the program from any directory. If you don't know how to do, you should refer to these documents below:

- macOS: [https://support.apple.com/en-vn/guide/terminal/apd382cc5fa-4f58-4449-b20a-41c53c006f8f/mac](https://support.apple.com/en-vn/guide/terminal/apd382cc5fa-4f58-4449-b20a-41c53c006f8f/mac)
- Microsoft Windows: [https://www.java.com/en/download/help/path.html](https://www.java.com/en/download/help/path.html)

## Update Logs

**[December 17, 2022]** Release the beta version, which is implemented in Python. The final release will be made available in more programming languages such as C/C++, Ruby.

