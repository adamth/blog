from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post, Like
from .forms import PostForm, CommentForm


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    liked = post.liked(request.user.id)
    return render(request, 'blog/post/detail.html', {'post': post, 'liked': liked, 'form': form})


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
    return render(request, 'blog/post/edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/post/{}'.format(post.pk))
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post/edit.html', {'form': form})


def register(request):
    if request.method == 'POST':
        # Get the user input from the form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user if the form is valid
            form.save()
            # Get the users credentials to log them in and redirect to the home page
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'blog/registration/register.html', {'form': form, 'heading': 'Register'})


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/registration/signin.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('index')


def post_like(request, pk):
    if request.user.is_authenticated:
        like = Like()
        like.author = request.user
        like.post = Post.objects.get(pk=pk)
        like.save()
        return redirect('/post/{}'.format(pk))
    else:
        return redirect('sign_in')


def post_comment(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = Post.objects.get(pk=pk)
                comment.save()
    else:
        return redirect('sign_in')
    return redirect('/post/{}'.format(pk))
