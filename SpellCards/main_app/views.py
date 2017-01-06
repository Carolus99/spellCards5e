from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html', {'spells':spells})

class Spell:
    def __init__(self, name, level, distance, school):
        self.name = name
        self.level = level
        self.distance = distance
        self.school = school

spells = [
    Spell('Aid', 2, 30, 'Abjuration'),
    Spell('Antimagic Field', 8, 'Self', 'Abjuration'),
    Spell('Blade Barrier', 6, 30, 'Evocation'),
    Spell('Blur', 2, 'Self', 'Illusion')
]
