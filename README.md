# **YouTube MP3 Downloader**
This Python script downloads YouTube videos as MP3 files using `yt-dlp`.

## **Features**
- Downloads the best available audio quality.
- Converts the audio to MP3 format (192kbps).
- Supports bulk downloading from a text file containing video URLs.
- Uses `yt-dlp` for improved performance and compatibility.

## **Requirements**
Ensure you have the following installed:
- Python 3.x
- `yt-dlp`
- `ffmpeg`

### **Install Dependencies**
Run the following command to install `yt-dlp`:
```sh
pip install yt-dlp
```

You also need to install `ffmpeg` if it's not already available on your system:
- **Windows**: Download from [FFmpeg official site](https://ffmpeg.org/download.html) and add it to your system `PATH`.
- **Linux/macOS**: Install using a package manager, e.g.,
  ```sh
  sudo apt install ffmpeg  # Debian/Ubuntu
  brew install ffmpeg      # macOS
  ```

## **Usage**
### Download a Single Video as MP3
Modify the script to call `download_video_as_mp3(video_url)`, replacing `video_url` with the actual YouTube link.

### Bulk Download from a File
1. Create a text file (e.g., `video_urls.txt`) and list YouTube video URLs, one per line.
2. Run the script:
   ```sh
   python bulk_yt_to_mp3.py
   ```

## **How It Works**
- The script reads video URLs from `video_urls.txt`.
- It downloads the best available audio stream.
- The audio is converted to MP3 format (192kbps) using `ffmpeg`.

## **License**
This project is licensed under the MIT License.

## **Contact** ✉
- E-mail: [velimir.paleksic@gmail.com](velimir.paleksic@gmail.com).
- VexSystems GitHub: [github.com/vexsystems](https://github.com/vexsystems).
- VexSystems Instagram: [@vex.systems](https://www.instagram.com/vex.systems/).