from django.shortcuts import render_to_response, HttpResponse
from django.core.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
import utils

def main(self):
    return render_to_response("main.haml")

def csv_to_xform(request):
    csv_data = request.POST.get(request.POST.keys()[0])

    survey = utils.create_survey_from_csv_text(csv_data)

    return HttpResponse(survey.to_xml())