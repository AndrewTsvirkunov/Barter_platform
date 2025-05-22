from django.shortcuts import render, redirect, get_object_or_404
from .models import Ad, ExchangeProposal
from .forms import AdForm, ExchangeProposalForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import AdSerializer, ExchangeProposalSerializer
from django.core.paginator import Paginator

# CRUD для объявлений
def create_ad(request):
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('ad_list')
    else:
        form = AdForm()
    return render(request, 'ads/create_ad.html', {'form': form})

def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)
    if request.method == "POST":
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads/edit_ad.html', {'form': form})

def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)
    ad.delete()
    return redirect('ad_list')

def ad_list(request):
    ads = Ad.objects.all()

    # Фильтрация
    title_query = request.GET.get('search', '')
    if title_query:
        ads = ads.filter(title__icontains=title_query) | ads.filter(description__icontains=title_query)

    # Пагинация
    paginator = Paginator(ads, 5) #  5 объявлений на странице
    page = request.GET.get('page')
    ads = paginator.get_page(page)

    return render(request, 'ads/ad_list.html', {'ads': ads})

# API представления
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


class ExchangeProposalViewSet(viewsets.ModelViewSet):
    queryset = ExchangeProposal.objects.all()
    serializer_class = ExchangeProposalSerializer
    permission_classes = [IsAuthenticated]

# def create_exchange_proposal(request):
#     if request.method == "POST":
#         form = ExchangeProposalForm(request.POST)
#         if form.is_valid():
#             proposal = form.save(commit=False)
#             proposal.ad_sender = get_object_or_404(Ad, id=request.POST['ad_sender_id'])
#             proposal.save()
#             return redirect('ad_list')
#     else:
#         form = ExchangeProposalForm()
#     return render(request, 'ads/create_exchange_proposal.html', {'form': form})