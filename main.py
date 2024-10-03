import soco
import sys
import argparse

class Speaker:
    def __init__(self, name:str="Sonos Move"):
        self.sonos = self.getSpeaker(name)

    def getSpeaker(self, name:str):
        # Get the Sonos speaker
        for zone in soco.discover():
            if zone.player_name == name:
                sonos = zone
                break
        return sonos

    def changeVolume(self, volume:int):
        # Change the volume of the speaker
        self.sonos.volume = volume

    def main(self, volume:int, event:str=None):
        if volume:
            self.changeVolume(volume)

        if event:
            match event:
                case "play":
                    self.sonos.play()
                case "stop":
                    self.sonos.stop()
                case "pause":
                    self.sonos.pause()
                case "next":
                    self.sonos.next()
                case "previous":
                    self.sonos.previous()
                case _:
                    print("Invalid event")
                    sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--volume", type=int, help="Set the volume level (0-100)")
    parser.add_argument("-e", "--event", type=str, choices=["play", "stop", "pause", "next", "previous"], help="Control playback events")
    args = parser.parse_args()

    speaker = Speaker()
    speaker.main(args.volume, args.event)
