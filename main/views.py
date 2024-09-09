from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Romeo and Juliet',
        'author' : 'William Shakespeare',
        'genre' : 'Romance',
        'price' : 200000,
        'stock' : 13,
        'description' : '''Romeo and Juliet is a tragedy written by William Shakespeare 
                        early in his career about the romance between two Italian youths 
                        from feuding families.''',
    }

    return render(request, "main.html", context)