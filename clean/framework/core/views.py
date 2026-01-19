from django.shortcuts import render, redirect
from infrastructure.repositories import DjangoCustomerRepository, DjangoBookRepository
from usecases.customer_usecases import ListCustomersUseCase, CreateCustomerUseCase
from usecases.book_usecases import ListBooksUseCase, CreateBookUseCase

# --- Customer Views ---
def customer_list(request):
    repo = DjangoCustomerRepository()
    use_case = ListCustomersUseCase(repo)
    customers = use_case.execute()
    return render(request, 'core/customer_list.html', {'customers': customers})

def customer_create(request):
    if request.method == 'POST':
        repo = DjangoCustomerRepository()
        use_case = CreateCustomerUseCase(repo)
        use_case.execute(
            id=request.POST['id'],
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return redirect('customer_list')
    return render(request, 'core/customer_form.html')

# --- Book Views ---
def book_list(request):
    repo = DjangoBookRepository()
    use_case = ListBooksUseCase(repo)
    books = use_case.execute()
    return render(request, 'core/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        repo = DjangoBookRepository()
        use_case = CreateBookUseCase(repo)
        use_case.execute(
            title=request.POST['title'],
            author=request.POST['author'],
            price=float(request.POST['price']),
            stock=int(request.POST['stock'])
        )
        return redirect('book_list')
    return render(request, 'core/book_form.html')