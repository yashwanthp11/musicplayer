import pygame
import os

# Initialize pygame
pygame.init()

# Set the path to your music directory
music_dir = music_dir = r'C:\Users\yashw\Downloads'
1

# Create a list of music files in the directory
music_files = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.ogg', '.wav'))]

# Initialize the mixer for audio playback
pygame.mixer.init()

# Create a function to play music
def play_music(file):
    pygame.mixer.music.load(os.path.join(music_dir, file))
    pygame.mixer.music.play()

# Main loop
while True:
    print("\nAvailable Songs:")
    for i, file in enumerate(music_files):
        print(f"{i+1}. {file}")

    choice = input("Enter the song number you want to play (q to quit): ")
    
    if choice == 'q':
        break
    
    try:
        song_number = int(choice)
        if 1 <= song_number <= len(music_files):
            song_to_play = music_files[song_number - 1]
            print(f"Playing: {song_to_play}")
            play_music(song_to_play)
        else:
            print("Invalid song number. Please choose a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid song number or 'q' to quit.")

# Quit pygame
pygame.mixer.quit()
