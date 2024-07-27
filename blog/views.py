from datetime import date

from django.shortcuts import render

all_posts = [
    { # AI photo
        "slug": "AI",
        "image": "ai1.png",
        "author": "Evyatar",
        "date": date(2024, 7, 15),
        "title": "AI",
        "excerpt": "What is AI?",
        "content": """
        Lorem ipsum, dolor sit amet consectetur adipisicing elit.
        Eaque hic necessitatibus maiores doloremque nihil,
        id facere blanditiis quibusdam totam? Aut animi repellat libero.
        Natus debitis beatae, totam quibusdam sequi adipisci!
        """
    },
    { # Mathematics photo 
        "slug": "Applied-Math",
        "image": "math1.jpg",
        "author": "Evyatar",
        "date": date(2024, 7, 15),
        "title": "Applied Mathematics",
        "excerpt": "",
        "content": """
        Lorem ipsum, dolor sit amet consectetur adipisicing elit.
        Eaque hic necessitatibus maiores doloremque nihil,
        id facere blanditiis quibusdam totam? Aut animi repellat libero.
        Natus debitis beatae, totam quibusdam sequi adipisci!
        """
    },
    {# programming photo 
        "slug": "programming-page",
        "image": "programming.png",
        "author": "Evyatar",
        "date": date(2023, 7, 15),
        "title": "Programming Languages",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't eben prepared for what happened whilst I was enjoying the view!",
        "content": """
        Lorem ipsum, dolor sit amet consectetur adipisicing elit.
        Eaque hic necessitatibus maiores doloremque nihil,
        id facere blanditiis quibusdam totam? Aut animi repellat libero.
        Natus debitis beatae, totam quibusdam sequi adipisci!
        """
    }
]


def get_date(post):
    return post['date']

# Create your views here.

def starting_page (request):
    sorted_posts = sorted(all_posts ,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render (request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render (request, "blog/all-posts.html", {
        "all_posts": all_posts # Add all_posts variable to all_posts template 
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render (request, "blog/post-detail.html", {
        "post": identified_post
    })