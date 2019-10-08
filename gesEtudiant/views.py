from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from gesEtudiant.models import Etudiant

# Create your views here.

# @login_required
def etudiant_details(request):
    # etudiant = get_object_or_404(Etudiant, pk=pk)
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiant_detail.html',{'etudiants':etudiants})
