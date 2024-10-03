import soco
import sys
import argparse


def getSpeaker():
    # Get the Sonos speaker
    for zone in soco.discover():
        if zone.player_name == "Sonos Move":
            sonos = zone
            break
    return sonos


def changeVolume(sonos, volume:int):
    # Change the volume of the speaker
    sonos.volume = volume


def main(volume:int=3, event:str=None):
    sonos = getSpeaker()
    changeVolume(sonos, volume)

    if event:
        match event:
            case "play":
                sonos.play()
            case "stop":
                sonos.stop()
            case "pause":
                sonos.pause()
            case "next":
                sonos.next()
            case "previous":
                sonos.previous()
            case _:
                print("Invalid event")
                sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--volume", type=int, default=3)
    parser.add_argument("-e", "--event", type=str, default=None)
    args = parser.parse_args()

    main(args.volume, args.event)
