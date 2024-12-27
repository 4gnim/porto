from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portofolio, SkillImage, Contact
from .forms import FormContact
    
def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portofolio
    portofolios = Portofolio.objects.all()

    # Skill Image
    skill_img = SkillImage.objects.latest('updated')

    # Contact
    contact = Contact.objects.latest('updated')

    # Contact Form
    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            form.save()  # Simpan data ke database
            # return render(request, 'contact_success.html')  # Halaman sukses
    else:
        form = FormContact()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portofolios': portofolios,
        'skill_img': skill_img,
        'contact': contact,
        'form': form,
    }


    return render(request, 'index.html', context)