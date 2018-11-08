from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Comentario, Pessoa
from .forms import PostForm, ComentarioForm, PessoaForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    form = ComentarioForm()
    return render(request, 'blog/post_detail.html', {'post': post , 'form' : form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post = Post.objects.get(pk=pk)
    post.delete()
    return post_list(request)

def comentario_new(request):
    form = ComentarioForm(request.POST)
    c = form.save(commit=False)
    c.post = get_object_or_404(Post, pk=request.POST['post'])
    c.save()

    return redirect('post_detail', pk=request.POST['post'])

def comentario_delete(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario = Comentario.objects.get(pk=pk)
    post = comentario.post.pk
    comentario.delete()
    return redirect('post_detail', pk=post)

def comentario_edit(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.save()
            return redirect('post_detail',  pk=comentario.post.pk)
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'blog/post_edit.html', {'form': form})

def pessoa_detail(request):
    pessoa = get_object_or_404(Pessoa, pk=request.user.pk)
    #print(request.user.pk)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.save()
            return render(request, 'blog/pessoa_detail.html', {'pessoa': pessoa, 'form': form})
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'blog/pessoa_detail.html', {'pessoa': pessoa , 'form' : form})

def pessoanew(request):
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.save()
            return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        form = PessoaForm()
    return render(request, 'blog/pessoa_detail.html', {'form': form})



