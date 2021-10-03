from flask import Blueprint, render_template

import jimi

from plugins.usecase.models import usecase

pluginPages = Blueprint('usecasePages', __name__, template_folder="templates")

@pluginPages.route("/")
def mainPage():
    usecases = usecase._usecase().query(sessionData=jimi.api.g.sessionData,query={})["results"]
    return render_template("usecases.html", CSRF=jimi.api.g.sessionData["CSRF"], usecases=usecases)