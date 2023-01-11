from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Post



class PostVistasTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        u = User.objects.create(first_name='Big', last_name='Bob')
        for x in range(10):
            Post.objects.create(title=f'My post {x}', slug=f'my-post-{x}', author=u, content=f'This is my post {x}')

    def test_listado(self):
        ''' 
        Comprobar que el listado devuelve 200 y que el template es el correcto

        '''
        #página inicial
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

        #admin
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 302)

        #primer post
        p = Post.objects.first()
        slug = p.slug
        response = self.client.get(f'/{slug}/')
        self.assertEquals(response.status_code, 200)