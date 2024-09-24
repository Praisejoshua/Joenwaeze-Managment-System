from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Managment
from .forms import ManagementForm
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

class SystemListView(ListView):
    model = Managment
    template_name = "managment.html"
    context_object_name = "object_list"


# defining the data that will be fetched when the page is loaded
    def get_queryset(self):
        return Managment.objects.all()

# this is used to add extra data to form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['form'] = ManagementForm()  # Add the form to the context
        return context

    def post(self, request, *args, **kwargs):
        form = ManagementForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new management entry
            return HttpResponseRedirect(self.request.path_info) #after the data has been added they'll be returned to the same page
        
        context = self.get_context_data(form=form)  #if the form isn't valid and returns with the data filed
        return self.render_to_response(context)

# UpdateView to handle the editing 
class ManagementUpdateView(UpdateView):
    model = Managment
    fields = ["seller_name", "Weight", "amount", "date"] 
    template_name = "managment_form.html"
    success_url = reverse_lazy('managment_list') 


# DeleteView to handle deletion
class ManagementDeleteView(DeleteView):
    model = Managment
    template_name = "managment_confirm_delete.html"
    success_url = reverse_lazy('managment_list')  
