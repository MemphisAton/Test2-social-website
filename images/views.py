from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import ImageCreateForm
from .models import Image


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image})


@login_required  # предотвращает доступ неаутентифицированных пользователей
def image_create(request):
    '''
    представление хранения изображений на сайте
    '''
    if request.method == 'POST':
        # форма отправлена
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # данные в форме валидны
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # назначить текущего пользователя элементу
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')
            # перенаправить к представлению детальной информации о только что созданном элементе
            return redirect(new_image.get_absolute_url())
    else:
        # скомпоновать форму с данными, предоставленными букмарклетом методом GET
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})


@login_required  # предотвращает доступ неаутентифицированных пользователей
@require_POST  # возвращает объект HttpResponseNotAl lowed (код состояния, равный 405), в случае если HTTP-запрос выполнен не методом POST.
def image_like(request):
    image_id = request.POST.get('id')  # ИД объекта изображения, над которым пользователь выполняет действие
    action = request.POST.get('action')  # действие, которое пользователь хочет выполнить. like либо unlike.
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})
