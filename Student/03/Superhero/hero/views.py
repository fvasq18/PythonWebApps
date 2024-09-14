from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class SpidermanView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spiderman',
            'body': 'My name is Peter Parker',
            'image': '/static/images/spiderman.jpg'
        }


class BatmanView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'BatMan',
            'body': 'My name is Bruce Wayne',
            'image': '/static/images/batman.jpg'
        }


class SuperManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'SuperMan',
            'body': 'My name is Clark Kent',
            'image': '/static/images/superman.jpg'
        }
