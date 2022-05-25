from typing import List


class ArtistOccupation:
    def get_job_description(self):
        print("My job is regarded as artistic")


class Musician(ArtistOccupation):
    def perform(self):
        return "I compose songs and sometimes write for other musicians."


class PartyPlanner(ArtistOccupation):
    def plan(self):
        return "My job involves organizing exciting events for people to attend and enjoy."


class Main:
    def __init__(self, artists: List[ArtistOccupation]):
        self.artists = artists

    def print_description(self):
        for artist in self.artists:
            artist.get_job_description()


artists_list = []

rnb_musician = Musician()
artists_list.append(rnb_musician)

birthday_planner = PartyPlanner()
artists_list.append(birthday_planner)

opera_singer = Musician()
artists_list.append(opera_singer)

main_obj = Main(artists_list)
main_obj.print_description()

