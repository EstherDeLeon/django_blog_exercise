from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Post, Comment


# tests para comprbar funcionamiento

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        u = User.objects.create(first_name='Big', last_name='Bob')
        p = Post.objects.create(title='My first post', 
            slug='my-first-post', 
            author=u,
            content='My first post content')
        Comment.objects.create(
            post=p, 
            name='María',
            email = 'maria@gmail.com',
            body = 'My first comment'
            )



    def test_object_name_is_last_name_comma_first_name(self):
        ''' 
        Comprobar que el print del objeto devuelve su título

        '''
        post = Post.objects.first()
        expected_object_name = f'{post.title}'
        self.assertEquals(expected_object_name, str(post))

    def test_slug(self):
        ''' 
        Comprobar el slug 

        '''
        post = Post.objects.first()
        slug = post .slug
        expected_slug = post.title.lower().replace(' ', '-')
        self.assertEquals(expected_slug, slug)

    def test_str_comentario(self):
        ''' 
        Comprobar el print del comentario 

        '''
        c = Comment.objects.first()
        expected_object_name = f'Comment {c.body} by {c.name}'
        self.assertEquals(expected_object_name, str(c))

    def test_get_absolute_url(self):
        ''' 
        Comprobar que el get_absolute_url devuelve la url correcta

        '''
        post = Post.objects.first()
        slug = post.slug
        self.assertEquals(post.get_absolute_url(), f'/{slug}/')
        