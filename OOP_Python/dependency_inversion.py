from abc import ABC, abstractmethod


class Communicable(ABC):
    @abstractmethod
    def transmission(self):
        pass

    @abstractmethod
    def prevention(self):
        pass


class Vaccination:
    def __init__(self, communicable: Communicable):
        self.disease = communicable

    def inform_mode_transmission(self):
        print("This disease is dangerous")
        self.disease.transmission()


class COVID(Communicable):

    def transmission(self):
        print("COVID - is transmitted via droplets from an infected person or animal to another.")

    def prevention(self):
        print("COVID - reduce infection by:\n * Wearing a nose mask. \n * Regular use hand sanitizer")


class Hantavirus(Communicable):
    def transmission(self):
        print("Hantavirus - is a rodent-borne disease that affects humans.")

    def prevention(self):
        print("Hantavirus - reduce infection by:\n * Avoid air-borne dust when areas with rodents droppings are cleaned.")


obj_covid = COVID()
obj_hanta = Hantavirus()

vaccination_1 = Vaccination(obj_covid)
vaccination_1.inform_mode_transmission()

vaccination_2 = Vaccination(obj_hanta)
vaccination_2.inform_mode_transmission()