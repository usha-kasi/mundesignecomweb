from django.shortcuts import render, get_object_or_404
from .models import Collection, Piece

def index(request):
    """
    View function for the home page of the site.
    """
    all_collection = Collection.objects.all()
    context = {
        'all_collection': all_collection,
    }
    return render(request, "staticPages/staticPagestemplate.html", context)

def details(request, staticPages_id):
    """
    View function for a single collection or piece.
    """
    piece = get_object_or_404(Piece, id=staticPages_id)
    context = {
            'piece': piece,
        }
    return render(request, "staticPages/detail.html", context)
