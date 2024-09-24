from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = 'index.html'



class SpidermanView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spiderman',
            'body': 'My name is Peter Parker',
            'image': '/static/images/spiderman.jpg',
            'strengths': 'Strengths: Super Strenght, Spider Sense, Sticky',
            'weaknesses': 'Weaknesses: Young, and water '
        }


class BatmanView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'BatMan',
            'body': 'My name is Bruce Wayne',
            'image': '/static/images/batman.jpg',
            'strengths':'Strenghts: Rich, Smart, Strong',
            'weaknesses': 'Weaknesses: No Superpower, His parents'
        }


class SuperManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'SuperMan',
            'body': 'My name is Clark Kent',
            'image': '/static/images/superman.jpg',
            'strengths':'Strenghts: Super Stength, Flight, Laser',
            'weaknesses': 'Weaknesses: Kryptonite'
        }
    
class FlashView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Flash',
            'body': 'My name is Barry Allen',
            'image': '/static/images/flash.jpg',
            'strengths':'Strenghts: Fast, Durable',
            'weaknesses': 'Weaknesses: extreme heat and cold'
        }
    

class BlackPantherView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Black Panther',
            'body': 'My name is King TChalla',
            'image': '/static/images/black_panther.jpg',
            'strengths':'Strenghts: Rich, Smart, Vibranium',
            'weaknesses': 'Weaknesses: Limited abilities, emotional attachments'
        }
