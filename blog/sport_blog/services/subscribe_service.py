# from blog.sport_blog.models import Author
# from django.http import JsonResponse
#
# from django.shortcuts import get_object_or_404, render


# def api_subscribe(request):
#     author_id = request.GET["author_id"]
#     email_to = request.GET["email_to"]
#
#     get_object_or_404(Author, pk=author_id)
#
#     subscribe_process(author_id, email_to)
#
#     data = {'author_id': author_id}
#     return JsonResponse(data, safe=False)


# def posts_subscribe(request):
#     author_id = request.GET["author_id"]
#     email_to = request.GET["email_to"]
#
#     subscribe_process(author_id, email_to)
#
#     return render(request, 'sport_blog/subscribe.html', context=context)


# def subscribe_process(author_id, email_to):
#     subscribe(author_id, email_to)
#     # notify(email_to)
