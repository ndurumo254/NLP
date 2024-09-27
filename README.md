# NLP
open AI in Django python framework


# Start by understanding word embedding
In modern day search engine vector search is used

Words are converted in numerics and represented in vector format

This is what is known as word embedding

This vector representation is inform of numpy array


# Django setup
create django project using   `djang-admin startproject ...name`  for this case my project name is talknlp

create django app  using `python manage.py startapp ....name`  the name of my app is blog

# Create database table

class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField
    timestamp=models.DateTimeField(auto_now_add=True)

Here i have 3 column. title,content and timestamp