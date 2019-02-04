########################################################################################
## SERWERY SYSTEMOW ##
########################################################################################
class SerwerySystemowListView(generic.ListView):
    template_name = 'umowy/serwerysystemow_list.html'
    context_object_name = 'serwerysystemow_list'

    def get_queryset(self):
        return SerwerySystemow.objects.all()


class SerwerySystemowDetailView(generic.DetailView):
    model = SerwerySystemow
    template_name = 'umowy/serwerysystemow_detail.html'


class SerwerySystemowCreateView(CreateView):
    template_name = 'umowy/systemy_form.html'
    fields = ['serwer', 'system']
    model = SerwerySystemow

    # fields = ['nazwa','opis_systemu','baza_danych','oprogramowanie','data_wsparcia']


class SerwerySystemowUpdateView(UpdateView):
    template_name = 'umowy/systemy_form.html'
    model = SerwerySystemow
    fields = ['serwer', 'system']


class SerwerySystemowDeleteView(DeleteView):
    model = SerwerySystemow
    success_url = reverse_lazy('umowy:serwerysystemow_list')


########################################################################################
## UMOWY ##
########################################################################################
class UmowyListView(generic.ListView):
    template_name = 'umowy/umowy_list.html'
    context_object_name = 'umowy_list'

    def get_queryset(self):
        return UmowyUtrzymaniowe.objects.all()


class UmowyDetailView(generic.DetailView):
    model = UmowyUtrzymaniowe
    template_name = 'umowy/umowy_detail.html'


class UmowyCreateView(CreateView):
    template_name = 'umowy/umowyutrzymaniowe_form.html'
    model = UmowyUtrzymaniowe
    form_class = UmowaForm


class UmowyUpdateView(UpdateView):
    model = UmowyUtrzymaniowe
    form_class = UmowaForm
    template_name = 'umowy/umowyutrzymaniowe_form.html'


class UmowyDeleteView(DeleteView):
    model = UmowyUtrzymaniowe
    success_url = reverse_lazy('umowy:umowy_list')


########################################################################################
## BAZY_DANYCH ##
########################################################################################
class BazyDanychListView(generic.ListView):
    template_name = 'umowy/bazy_list.html'
    context_object_name = 'bazy_list'

    def get_queryset(self):
        return BazyDanych.objects.all()


class BazyDanychDetailView(generic.DetailView):
    model = BazyDanych
    template_name = 'umowy/bazy_detail.html'


class BazyDanychCreateView(CreateView):
    model = BazyDanych
    fields = ['nazwa', 'wersja', 'licencja']
    template_name = 'umowy/bazy_form.html'


class BazyDanychUpdateView(UpdateView):
    model = BazyDanych
    fields = ['nazwa', 'wersja', 'licencja']
    template_name = 'umowy/bazy_form.html'


class BazyDanychDeleteView(DeleteView):
    model = BazyDanych
    success_url = reverse_lazy('umowy:bazy_list')


########################################################################################
## ADMINISTRATORZY ##
########################################################################################
class AdministratorzyListView(generic.ListView):
    template_name = 'umowy/administratorzy_list.html'
    context_object_name = 'administratorzy_list'

    def get_queryset(self):
        return Administratorzy.objects.all()


class AdministratorzyDetailView(generic.DetailView):
    model = Administratorzy
    template_name = 'umowy/administratorzy_detail.html'


class AdministratorzyCreateView(CreateView):
    model = Administratorzy
    fields = ['imie', 'nazwisko']
    template_name = 'umowy/administratorzy_form.html'


class AdministratorzyUpdateView(UpdateView):
    model = Administratorzy
    fields = ['imie', 'nazwisko']
    template_name = 'umowy/administratorzy_form.html'


class AdministratorzyDeleteView(DeleteView):
    model = Administratorzy
    success_url = reverse_lazy('umowy:administratorzy_list')


########################################################################################
## SERWERY ##
########################################################################################
class SerweryListView(generic.ListView):
    template_name = 'umowy/serwery_list.html'
    context_object_name = 'serwery_list'

    def get_queryset(self):
        return Serwery.objects.all()


class SerweryDetailView(generic.DetailView):
    model = Serwery
    template_name = 'umowy/serwery_detail.html'


class SerweryCreateView(CreateView):
    model = Serwery
    fields = ['nazwa', 'hostname', 'system_operacyjny', 'wersja', 'adres', 'fizyczny_wirtualny']
    template_name = 'umowy/serwery_form.html'


class SerweryUpdateView(UpdateView):
    model = Serwery
    fields = ['imie', 'nazwisko']
    template_name = 'umowy/serwery_form.html'


class SerweryDeleteView(DeleteView):
    model = Serwery
    success_url = reverse_lazy('umowy:serwery_list')


########################################################################################
## USERS ##
########################################################################################
class UserFormView(View):
    form_class = UserForm
    template_name = 'umowy/user_registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # clean(normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('umowy:login')
        return render(request, self.template_name, {'form': form})





