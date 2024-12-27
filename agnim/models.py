from django.db import models

# Home Section
class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')

    # Save Time When Modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
# About Section
class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career
    
class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)

# Skills Section
class Category(models.Model):
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name
    
class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)

# Portofolio Section
class Portofolio(models.Model):
    image = models.ImageField(upload_to='portofolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Portofolio {self.id}'
    
# Skills Image
class SkillImage(models.Model):
    skill_img = models.ImageField(upload_to='SkillImage/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Image: {self.id}'
    
# Contact
class Contact(models.Model):
    heading = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Contact {self.id}'
    
# Contact Form
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name