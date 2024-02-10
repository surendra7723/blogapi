from django.test import TestCase
from django.contrib.auth import get_user_model
from  .models import Post
class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user=get_user_model().objects.create_user(
            username='test',
            email="test@gmail.com",
            password='12345' ,
            )
        cls.post=Post.objects.create(
            author=cls.user,
            title="A good title",
            body='Nice Body Content',
            
        )
    def test_post_model(self):
        self.assertEqual(self.post.author.username,"test")
        self.assertEqual(self.post.title,"A good title")
        self.assertEqual(self.post.body,"Nice Body Content")
        self.assertEqual(str(self.post),"A good title")
    