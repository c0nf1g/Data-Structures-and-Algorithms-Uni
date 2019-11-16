class Clip:
    def __init__(self,
                 artist,
                 name,
                 duration,
                 view):

        self.artist = artist
        self.name = name
        self.duration = duration
        self.view = view

    def __repr__(self):
        return 'Clip(Artist: {}, Name: {}, Duration: {}, Views: {})'\
            .format(self.artist,
                    self.name,
                    self.duration,
                    self.view)
