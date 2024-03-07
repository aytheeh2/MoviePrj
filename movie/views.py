from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Movie
from .forms import MovieForm
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# def home(request):
#     # if request.method=='POST':
#     #     return render(request,'home.html')
#     movies = Movie.objects.all()
#     context = {'movies': movies}
#     return render(request, 'home.html', context)


class MovieList(ListView):
    model = Movie
    template_name = 'index.html'
    context_object_name = 'movies'

# def details(request, pk):
#     movie = Movie.objects.get(id=pk)
#     context = {'movie': movie}
#     return render(request, 'details.html', context)


class MovieDetails(DetailView):
    model = Movie
    template_name = 'details.html'
    context_object_name = 'movie'

# def add_movie(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         year = request.POST['year']
#         description = request.POST['description']
#         image = request.FILES['image']
#         m = Movie.objects.create(
#             title=title, year=year, description=description, image=image)
#         m.save()
#         return home(request)
#     context = None
#     return render(request, 'add_movie.html', context)


# def add_movie1(request):
#     if request.method == 'POST':
#         form = MovieForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         return home(request)
#     form = MovieForm()
#     return render(request, 'add_movie1.html', {'form': form})


class MovieAdd(CreateView):
    model = Movie
    template_name = 'add.html'
    fields = '__all__'
    success_url = reverse_lazy('movie:home')


# def edit_movie(request, pk):
#     m = Movie.objects.get(id=pk)
#     if request.method == 'POST':
#         form = MovieForm(request.POST, request.FILES, instance=m)
#         if form.is_valid():
#             form.save()
#         return home(request)
#     form = MovieForm(instance=m)
#     return render(request, 'edit_movie.html', {'form': form})

class MovieEdit(UpdateView):
    model = Movie
    template_name = 'edit.html'
    fields = '__all__'
    success_url = reverse_lazy('movie:home')


# def delete_movie(request, pk):
#     m = Movie.objects.get(id=pk)
#     m.delete()
#     return home(request)
class MovieDelete(DeleteView):
    model = Movie
    template_name='delete.html'
    context_object_name='movie'
    success_url = reverse_lazy('movie:home')
