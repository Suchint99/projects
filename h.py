import tkinter as tk
from tkinter import scrolledtext

def show_transcript(transcript):
    window = tk.Tk()
    window.title("YouTube Transcript")
    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20)
    text_area.insert(tk.INSERT, transcript)
    text_area.config(state=tk.DISABLED)
    text_area.pack()
    window.mainloop()

if __name__ == "__main__":
    youtube_url = input("Enter YouTube URL: ")
    output_path = "."

    print("Downloading audio...")
    audio_path = download_audio(youtube_url, output_path)
    print("Transcribing audio...")
    transcript = transcribe_audio(audio_path)
    
    show_transcript(transcript)




