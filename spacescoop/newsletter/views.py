from django.shortcuts import render

def subscribe(request):
    return render(request, 'spacescoop/newsletter/subscribe.html', {
            # 'objects': objects,
        })
