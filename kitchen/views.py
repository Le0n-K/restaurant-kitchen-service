from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Chef
from kitchen.forms import ChefCreationForm, ChefExperienceUpdateForm, DishForm, ChefSearchForm, DishSearchForm, \
    DishTypeSearchForm
from kitchen.models import Dish, DishType


# @login_required
def index(request):
    """View function for the home page of the site."""

    num_chefs = Chef.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_chefs": num_chefs,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = DishTypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish_type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish_type-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.all().select_related("dish_type")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Dish.objects.all()
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class ChefListView(LoginRequiredMixin, generic.ListView):
    model = Chef
    paginate_by = 5
    template_name = "kitchen/chef_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ChefListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = ChefSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Chef.objects.all()
        form = ChefSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class ChefDetailView(LoginRequiredMixin, generic.DetailView):
    model = Chef
    template_name = "kitchen/chef_detail.html"
    queryset = Chef.objects.all().prefetch_related("dishes__dish_type")


class ChefCreateView(LoginRequiredMixin, generic.CreateView):
    model = Chef
    template_name = "kitchen/chef_form.html"
    success_url = reverse_lazy("kitchen:chef-list")
    form_class = ChefCreationForm


class ChefDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Chef
    template_name = "kitchen/chef_confirm_delete.html"
    success_url = reverse_lazy("kitchen:chef-list")


class ChefUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Chef
    template_name = "kitchen/chef_form.html"
    success_url = reverse_lazy("kitchen:chef-list")
    form_class = ChefExperienceUpdateForm


@login_required
def assign_me_dish(request, pk):
    if request.method == "POST":
        chef = Chef.objects.get(id=request.user.id)
        dish = Dish.objects.get(id=pk)
        dish.chefs.add(chef)

    return redirect("kitchen:dish-detail", pk=pk)


@login_required
def delete_me_dish(request, pk):
    if request.method == "POST":
        chef = Chef.objects.get(id=request.user.id)
        dish = Dish.objects.get(id=pk)
        dish.chefs.remove(chef)

    return redirect("kitchen:dish-detail", pk=pk)
