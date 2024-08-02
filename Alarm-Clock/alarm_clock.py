import datetime
import time
import pygame

def set_alarm(alarm_time):
    print(f"Setting alarm for {alarm_time}...")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            pygame.mixer.init()
            pygame.mixer.music.load("alarm_sound.mp3")  # Ensure 'alarm_sound.mp3' is in the same directory
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():  # Wait for the music to finish playing
                time.sleep(1)
            break
        time.sleep(1)

def main():
    alarm_time = input("Enter the time to set the alarm (HH:MM:SS): ")
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")

main()
