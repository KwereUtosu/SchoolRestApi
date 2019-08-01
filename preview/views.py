from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from .models import School
from .serializer import SchoolSerializer
from django.views import generic
from .models import Contact
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


# Create your views here.

def IndexView(request):
    # query_list = Report_item.objects.filter(publish=True)
    # query = request.GET.get('q')
    # if query:
    #     query_list = query_list.filter(Q(title__icontains=query) |
    #                                    Q(item_type__icontains=query) |
    #                                    Q(location__icontains=query) |
    #                                    Q(Description__icontains=query)).distinct()
    #
    # paginator = Paginator(query_list, 5)
    # page = request.GET.get('page')
    # try:
    #     qs = paginator.page(page)
    # except PageNotAnInteger:
    #     qs = paginator.page(1)
    # except EmptyPage:
    #     qs = paginator.page(paginator.num_pages)
    title = "Home-Back My Item"
    context = {
        "object_list": "hello"
    }

    return render(request, "preview/indexx.html", context)

class AllSchools(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def post(self, request, format=None):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SchoolView(APIView):

    def get(self, request, pk, format=None):
        try:
            school = School.objects.dates(pk=pk)
            serializer = SchoolSerializer(school)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        school = School.objects.dates(pk=pk)
        school.delete()
        return Response(status=status.HTTP_200_OK)

# class Contact_page(generic.DetailView):
#     model = Contact
#     # fields = ['name', 'email', 'query']
#     # slug_field = 'name'
#     # slug_url_kwarg = 'name'
#     # template_name = 'contacthelp.html'
#     # context_object_name = 'contact'
#     # success_url = reverse_lazy('index')
#     # return render(request, "static_page/about_us.html", {"title": title})
#     def contacthelp_request(request, primary_key):
#         book = get_object_or_404(Contact, pk=primary_key)
#         return(render(request, 'contacthelp.html'))

class ContactDetailView(generic.CreateView):
    model = Contact
    paginate_by = 2
    fields = ['name', 'email', 'query', 'image']
    success_url = reverse_lazy('index')

    # def contact_detail_view(request, primary_key):
    #     book = get_object_or_404(Contact, pk=primary_key)
    #     return render(request, 'contacthelp.html', context={'book': book})
