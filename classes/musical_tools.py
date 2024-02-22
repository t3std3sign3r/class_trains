class MusicalTool:
    def __init__(self, owner, type_tool):
        self.owner = owner
        self.type_tool = type_tool

    state = 'tuned'
    color = 'black'

    def play(self):
        return f'{self.owner} is playing on me'

    def tune(self):
        return f'{self.owner} is tuning me'


class WindTool(MusicalTool):
    def replace_mouthpiece(self):
        return f'{self.owner} is replacing mouthpiece'


trumpet = WindTool('Mary', 'wind')
print(trumpet.__dict__)
print(trumpet.state)
