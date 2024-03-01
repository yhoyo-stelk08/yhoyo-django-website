from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Food
from .forms import FoodForm

# Create your views here.

# function for index of food_seller
def index(request) :
    food_list = Food.objects.all().order_by('id')
    ctx = {
        'title' : 'We sell food and beverages',
        'food_list' : food_list, 
    }
    # print(food_list)
    return render(request,'food_seller/index.html',ctx)

# function for detail of food
def food_detail(request,food_id) :
    # get food based on food id
    detail = Food.objects.get(id=food_id)
    # print(detail)

    ctx = {
        'title' : 'Item Details',
        'detail' : detail,
    }
    return render(request, 'food_seller/detail.html', ctx)

def food_create(request):
    form_data = FoodForm(request.POST or None)

    if form_data.is_valid() :
        form_data.save()

        return redirect('food_seller:index')
    
    ctx = {
        'title' : 'Add Food Form',
        'form' : form_data,
    }
    return render(request,'food_seller/food_form.html',ctx)

def food_edit(request,food_id):
    food = Food.objects.get(id=food_id)
    form_data = FoodForm(request.POST or None,instance=food)

    if form_data.is_valid() :
        form_data.save()
        return redirect('food_seller:index')
        # return render('food_seller/edit/'+str(food.id))

    ctx = {
        'title' : 'Food Edit Form',
        'form' : form_data,
        'food' : food,
    }

    return render(request,'food_seller/food_form.html',ctx)

def food_delete(request,food_id):
    food = Food.objects.get(id=food_id)

    if request.method == "POST":
        food.delete()
        return redirect('food_seller:index')
    
    ctx = {
        'title' : 'Food Delete Form',
        'food' : food,
    }

    return render(request,'food_seller/food_delete.html',ctx)

# Class Based View for index
class FoodListView(ListView):
    model = Food
    template_name = "food_seller/index.html"
    context_object_name = 'food_list'
    extra_context = {'title': 'We sell food and beverages'}

# class based view for show detail
class FoodDetailView(DetailView):
    model = Food
    template_name = "food_seller/detail.html"
    context_object_name = 'detail'
    extra_content = {'title' : 'Food Detail'}

# class based view to create food
class FoodCreateView(CreateView):
    template_name = 'food_seller/food_form.html'
    form_class = FoodForm
    success_url = '/food_seller/'  # Redirects to food_seller:index upon successful form submission
    extra_context = {'title': 'Add Food Form'}

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        form.save()
        return super().form_valid(form)

# class based view for edit food
class FoodEditView(UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'food_seller/food_form.html'
    success_url = '/food_seller/'  # Redirects to food_seller:index upon successful form submission

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Food Edit Form'
        return context

# class based view to delete food
class FoodDeleteView(DeleteView):
    model = Food
    template_name = "food_seller/food_delete.html"
    success_url = "/food_seller/" # redirect to food_seller:index if the food is sucessfuly deleted

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Food Delete  Form'
        return context
    
    def post(self, request, *args, **kwargs):
        food = self.get_object()
        food.delete()
        return redirect(self.success_url)
