class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name.title()

    def __str__(self):
        return f'Nome: {self._name} - Ano: {self.year} - Likes: {self._likes}'

class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'Nome: {self._name} - Ano: {self.year} - Duração: {self.duration}min - Likes: {self._likes}'
 

class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons
    
    def __str__(self):
        return f'Nome: {self._name} - Ano: {self.year} - Temporadas: {self.seasons} - Likes: {self._likes}'

class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs
    
    def __getitem__(self, item):
        return self._programs[item]

    @property
    def listing(self):
        return self._programs
    
    def __len__(self):
        return len(self._programs)
