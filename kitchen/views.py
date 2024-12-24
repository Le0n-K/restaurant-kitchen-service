from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic, View
from django.views.generic import TemplateView

from accounts.models import Chef
from accounts.forms import ChefCreationForm, ChefSearchForm, ChefExperienceUpdateForm
from kitchen.forms import DishForm, DishSearchForm, DishTypeSearchForm
from kitchen.models import Dish, DishType


class IndexView(TemplateView):
    template_name = "kitchen/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_chefs"] = Chef.objects.count()
        context["num_dishes"] = Dish.objects.count()
        context["num_dish_types"] = DishType.objects.count()

        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1
        context["num_visits"] = num_visits + 1

        return context


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
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.select_related("dish_type")

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
    queryset = Chef.objects.prefetch_related("dishes__dish_type")


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


class AssignMeDishView(LoginRequiredMixin, View):
    def post(self, request, pk):
        chef = get_object_or_404(Chef, id=request.user.id)
        dish = get_object_or_404(Dish, id=pk)
        dish.chefs.add(chef)
        return redirect(reverse("kitchen:dish-detail", kwargs={"pk": pk}))


class DeleteMeDishView(LoginRequiredMixin, View):
    def post(self, request, pk):
        chef = get_object_or_404(Chef, id=request.user.id)
        dish = get_object_or_404(Dish, id=pk)
        dish.chefs.remove(chef)
        return redirect(reverse("kitchen:dish-detail", kwargs={"pk": pk}))
