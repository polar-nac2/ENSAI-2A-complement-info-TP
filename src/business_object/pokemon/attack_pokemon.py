from src

from abstract_personnage import AbstractPersonnage

class Magicien(AbstractPersonnage):
    def __init__(self):
        super().__init__("Throw a fireball", "Use a magic barrier")
       
    def damages(self) -> int:
        return 10

