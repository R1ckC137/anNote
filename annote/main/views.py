from django.shortcuts import render
from django.db.models import Q
from .forms import WriteForm, ReadForm
from .models import Annote


def main(request):
    error = ''
    if request.method == 'POST':
        if 'create' in request.POST:
            form = WriteForm(request.POST)
            if form.is_valid():
                annote = form.save()
                data = {'link': annote.link}
                return render(request, 'main/success_write.html', data)
            else:
                error = 'Form is not valid'
        else:
            form = ReadForm(request.POST)
            if form.is_valid():
                link = form.cleaned_data['link']
                annote = Annote.objects.filter(Q(link=link)).first()
                if annote:
                    # Проверяем, прочитана ли уже записка
                    read_note = Annote.objects.filter(Q(annote=annote)).first()
                    if read_note:
                        error = 'Note has already been read'
                    else:
                        # Если записка еще не прочитана, создаем новую запись в ReadNote
                        read_note = Annote.objects.create(annote=annote)
                        data = {'annote': annote.annote}
                        return render(request, 'main/success_read.html', data)
                else:
                    error = 'Note not found'
            else:
                error = 'Form is not valid'

    write_form = WriteForm()
    read_form = ReadForm()

    data = {
        'write_form': write_form,
        'read_form': read_form,
        'error': error
    }

    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
