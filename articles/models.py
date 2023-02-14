from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Articles(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='Yazar') #Djangonun dacilindeki Auth.User istifade ederek yazdiq.User silinende onun meqalesi de silinecek -on_delete=moldes.Cascade bunu gosterir
    title=models.CharField(max_length=50,verbose_name='Basliq')
    # content=models.TextField(verbose_name='Icerik')
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True)
    article_image=models.FileField(blank=True,null=True,verbose_name='Fotoraf ekleyin')

    def __str__(self):
        return self.title # obyekt melumatlari yerine, admin panelde title gosterilir.Eger bawqa fiel yazilsa,onu gosterecek
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article=models.ForeignKey(Articles,on_delete=models.CASCADE,verbose_name='Makale',related_name='comments')
    comment_author=models.CharField(max_length=50,verbose_name='Isim')
    comment_content=models.CharField(max_length=200,verbose_name='Yorum')
    comment_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']