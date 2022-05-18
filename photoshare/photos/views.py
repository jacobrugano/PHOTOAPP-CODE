from django.shortcuts import render,redirect
from .models import Category, Photo

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    return render(request, 'photos/gallery.html', {'categories':categories, 'photos':photos})

def addPhoto(request):
    categories = Category.objects.all() #To query and capture all the categories where to add the photos

    if request.method == 'POST': #To check the request method from the form
        data = request.POST #To get the form data from the request
        images = request.FILES.getlist('images') #To get the image from the request in the form
                                                 # 'images' is the input name in the add.html

        if data['category'] != 'none': #To check if there is a category inside data captured above in the request
                                         # none is the input field value in the html file
            category = Category.objects.get(id=data['category']) #To get AND SET the category if it is there.
        elif data['category_new'] != '': #So if there was a value sent for the category when creating a new category
            category, created = Category.objects.get_or_create(   # To Create the category inputted
                                                    #Assigning the created category to but has to have the name created
                name=data['category_new'])
        else:
            category = None #To make it okay for an image not to be in a category

#To create the photo object
        for image in images: #To loop through the images
            photo = Photo.objects.create( #To create the photo 
                category=category, #To set the category since we have a parent child relationship
                description=data['description'], #To set the description from the data captured
                image=image, #To set the image as captured at the top of this page
            )

        return redirect('gallery') #To redirect a user back to the homepage after creating the photo

    context = {'categories': categories} #To use to loop through the categories in add.html select dropdown
    return render(request, 'photos/add.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo':photo})

