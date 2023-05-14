import random
import json

class GallopingGolf():
    def __init__(self):
        self.data = None

        self.total_strokes = 0
        self.hole_strokes = 0

        self.putt = 4

        self.load_in_data()
        

    def load_in_data(self):
        file = open('bin/dice.json', 'r')
        self.data = json.load(file)

    def play_hole(self):
        holed_out = False
        shot = 0
        # print(self.data[shot])
        self.hole_strokes = 0

        while holed_out == False:
            strokes = self.data[shot]['options']
            roll = self.roll()
            stroke = strokes[roll]
            self.hole_strokes += stroke['strokes']
            print(stroke['name'])
            # stroke = strokes[roll]
            # print(stroke.name)
            if stroke['ends'] == True:
                break
            if stroke['skip_to_putt']:
                break
            shot += 1
            if shot >= 4:
                break

        if stroke['ends'] == False:
            strokes = self.data[self.putt]['options']
            roll = self.roll()
            stroke = strokes[roll]
            self.hole_strokes += stroke['strokes']
            print(stroke['name'])
            

        self.total_strokes += self.hole_strokes
        print("Total Strokes ", self.hole_strokes)


    def roll(self):
        return random.randint(0, 5)

