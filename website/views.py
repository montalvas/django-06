from re import template
from xml.dom.expatbuilder import TEXT_NODE
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "website/index.html"
