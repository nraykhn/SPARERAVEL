Nama : Nur Alya Khairina
NPM : 2306275701
Kelas : PBP A


# SPARERAVEL
## 🔗 Links
http://nur-alya31-spareravel.pbp.cs.ui.ac.id/
## Tugas 2
### Prosedur Pengembangan Proyek Django
1. **Membuat** *Repository* **GitHub `SPARERAVEL`**
- Melakukan konfigurasi awal Git dan konfigurasi nama pengguna serta E-mail
- Membuat *repository* baru dan menentukan direktori lokal SPARERAVEL
- Menghubungkan *repository* lokal dan *repository* GitHub
2. **Instalasi Django dan Inisiasi Proyek Django**
- Membuat *virtual environment* Python baru dengan menjalankan 
``` bash
python -m venv env
```
- Mengaktifkan *virtual environment* dengan menjalankan 
```bash 
env/Scripts/activate
```
- Membuat folder `requirements.txt` dengan isi *dependencies*.
``` bash
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
- Mengunduh *dependencies* dengan menjalankan *virtual environment* dahulu, lalu jalankan perintah;
```bash
pip install -r requirements.txt
```
- Membuat proyek Django bernama `SPARERAVEL` dengan perintah;
```bash 
django-admin startproject SPARERAVEL .
```
3. **Melakukan Konfigurasi Proyek dan Menjalankan Server**
- Menambahkan string ini pada `ALLOWED_HOSTS` di `setting.py`
```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```
- Jalankan server Django dengan perintah;
```bash
python manage.py runserver
```
- Membuat aplikasi `main` dengan perintah;
```bash
python manage.py startapp main
```
- Menambahkan `main` ke `INSTALLED_APPS` pada file `settings.py` di direktori `SPARERAVEL`
- Melakukan routing pada file `urls.py` di direktori `SPARERAVEL` dengan menambahkan;
```python
from django.contrib import admin
from django.urls import path
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```
- Menambahkan kode di `models.py` menjadi;
```python
from django.db import models


# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
```
- Menjalankan migrasi dengan perintah;
```bash
python manage.py makemigrations 
python manage.py migrate
```
- Membuat template pada file `main.html`
```html
<h1>{{nama_app}}</h1>

<h5>NPM: </h5>
<p>{{ npm }}<p>
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```
- Menambahkan fungsi pada `views.py`;
```python
from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'nama_app' : 'SPARERAVEL',
        'npm' : '2306275701',
        'name': 'Nur Alya Khairina',
        'class': 'PBP A'
    }
    return render(request, "main.html", context)
```
- Melakukan routing pada file `urls.py` pada folder `main`;
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
- Membuat unit test dengan mengisi `tests.py` pada direktori `main` dengan mengisi kode;
```python
from django.test import TestCase
from django.test import TestCase, Client
from django.utils import timezone

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)


    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')


    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)
```
- Menjalankan test dengan perintah;
```bash
python manage.py test
```
4. **Mengunggah Proyek ke** *Repository* **GitHub**
5. **Melakukan Deployment melalui PWS**
- Membuat proyek baru dengan nama `spareravel`
- Menambahkan URL *deployment* PWS pada `ALLOWED_HOSTS` Pada `settings.py` di proyek Django dengan URL `nur-alya31-spareravel.pbp.cs.ui.ac.id`
- Melakukan `git add`,`commit`,`push` setiap ada perubahan.
- Menjalankan perintah;
```bash
git remote add pws http://pbp.cs.ui.ac.id/nur.alya31/spareravel
git branch -M master
git push pws master
git branch -M main
```
- Saat ada perubahan pada proyek, dapat menjalankan perintah di bawah setelah melakukan `git add`,`commit`,`push`;
```bash
git push pws main:master
```


### Essai
**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

![Bagan PBP](https://github.com/user-attachments/assets/c6951068-c4de-45b6-90d3-8e1e01688eb3)


**Jelaskan fungsi** `Git` **dalam pengembangan perangkat lunak!**
- Git memungkinkan banyak developer untuk bekerja sama  dalam mengembangkan suatu perangkat lunak dengan penggunaan *branching*,
- Git memugkinkan melihat kode yang lama dan baru, sehingga dapat mengembalikan ke kode sebelumnya apabila ada keslahan,
- Git memberikan keuntungan bagi pengembang untuk memperbaiki *bug* tanpa takut kode hilang atau semakin salah,
- Setiap perubahan kode, akan secara otomatis diuji oleh Git.

**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
Menurut saya, ini disebabkan fitur-fiturnya yang cocok untuk awal belajar pengembangan perangkat lunak, seperti ORM, *routing* URL yang fleksibel, dan lain sebagainya. Kemudian Django juga membantu pemula dalam mengatur struktur aplikasi karena dalam Django semua sudah diatur dengan standar tertentu. Lalu seperti yang telah saya jelaskan, ORM membantu pemula karena tidak perlu memahami SQL dengan mendalam. 

**Mengapa model pada Django disebut sebagai ORM?**
ORM (Object Relation Mapper) hal ini dikarenakan model tersebut memiliki fungsi untuk menjadi jembatan antara database dan objek python tanpa harus menuliskan SQL Queries. ORM ini memetakan atribut objek ke masing-masing bidang tabel. ORM juga dapat mengambil data dengan cara tersebut.

Referensi
Chen, S., Ahmmed, S., Lal, K., & Deming, C. (2020). Django Web Development Framework: Powering the Modern Web. American Journal of Trade and Policy.


## Tugas 3
## Menjawab Pertanyaan
**Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?**
Data delivery diperlukan karena untuk mengakses informasi yang diperlukan dengan cara yang efisien karena data delivery memiliki integrasi yang baik dalam sebuah platform. Data delivery yang baik dapat memungkinkan suatu platform berjalan tanpa hambatan meskipun penggunanya meningkat. Data delivery merupakan komponen yang penting dalam implementasi platform, karena apabila tidak ada data delivery yang baik, maka akan memengaruhi kegunaan sebuah platform. 

**Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
Menurut saya, JSON lebih baik daripada XML dalam membuat suatu web. Hal ini sudah pasti dikarenakan JSON mempunyai sintaks yang lebih singkat dan mudah untuk dibaca penggunanya. Berbanding terbalik akan XML yang memiliki tag pembukan dan penutup yang membuatnya lebih panjang sintaksnya. Menurut saya, JSON lebih populer karena kelebihannya dalam keringkasan sintaks, kecepatan pemrosesan, dan efiesen. 

**Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?**
Menurut django documentation, is_valid() gitunakan oleh objek form untuk memvalidasi data. Metode ini memeriksa apakah data yang dimasukkan ke dalam form memenuhi aturan validasi yang sudah ditetapkan. Alasan kita membutuhkan method ini karena penting untuk memastikan bahwa data yang dimasukkan oleh user itu sesuai dengan format yang diharapkan. Lalu apabila tidak menggunakan is_valid(), maka data yang tidak sesuai dapat masuk ke database.

**Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
csrf_token sendiri berfungsi untuk mengecek apakah suatu request POST yang diterima server itu berasal dari sumber aplikasi kita sendiri sehingga dapat mencegah pelaku/penyerang dalam mengirim request palsu atas nama user (memanipulasi request). Apabila suatu form Django tidak menerapkan csrf_token, maka aplikasi akan rentan terserang sebuah tindakan berbahaya.  

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).**
**1. Membuat Kerangka Views**
- Membuat folder `templates` dan berkas `base.html` pada direktori utama. Lalu menambahkan isi `base.html` dengan;
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
- Mengubah variabel `TEMPLATES` dengan kode;
```python
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'], # Mengubah baris ini
        ...
    }
]
```
- Mengubah berkas `main.html` dengan kode;
```html
{% extends 'base.html' %}
{% block content %}
<h1>{{nama_app}}</h1>

<h5>NPM: </h5>
<p>{{ npm }}<p>

<h5>Name:</h5>
<p>{{ name }}</p>

<h5>Class:</h5>
<p>{{ class }}</p>
{% endblock content %}
```
**2. Mengubah Primary Key Menjadi UUID**
- Menambahkan kode pada file `models.py`
```python
import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ...
```
- Melakukan migrasi
**3. Membuat Form Input Data dan Menampilkan *Data Product Entry* pada HTML**
- Membuat file baru dengan nama `forms.py` dengan isi;
```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "quantity"]
```
- Menambahkan import pada file `views.py`;
```python
from django.shortcuts import render, redirect   # Menambahkan redirect
from main.forms import ProductForm
from main.models import Product
```
- Menambahkan create_product_entry pada file `views.py`
```python
def create_product_entry(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
- Mengubah isi `show_main` dengan menyesuaikan pada file `views.py`
```python
def show_main(request):
    product_entries = Product.objects.all() # Menambahkan baris ini
    context = {
        'nama_app' : 'SPARERAVEL',
        'npm' : '2306275701',
        'name': 'Nur Alya Khairina',
        'class': 'PBP A',
        'product_entries' : product_entries # Menambahkan baris ini
    }

    return render(request, "main.html", context)
```
- Menambahkan import `create_product_entry` pada `urls.py`
- Menambahkan path ke `urlpatterns` pada `urls.py`
```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
]
```
- Membuat file HTML baru dengan nama `create_product_entry.html` dengan isi;
```html
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
- Lalu menambahkan kode ini pada `main.html`untuk menampilkan data dalam tabel dan tombol untuk menuju form. 
```html
...
{% if not product_entries %}
<p>Belum ada data product pada SPARERAVEL.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Description</th>
    <th>Quantity</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data mood di bawah baris ini 
  {% endcomment %} 
  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.description}}</td>
    <td>{{product_entry.quantity}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product Entry</button>
</a>
{% endblock content %}
```
**4. Mengembalikan Data dalam Bentuk XML, JSON, dan Berdasarkan ID dalam bentuk XML dan JSON**
- Menambahkan beberapa import pada file `views.py`;
```python
from django.http import HttpResponse
from django.core import serializers
```
- Menambahkan beberapa fungsi pada file `views.py`;
```python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- Lalu, menambahkan import fungsi pada `urls.py`
```python
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
```
- Dan, terakhir menambahkan path URL ke dalam `urlpatterns`;
```python
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),

]
```

**Screenshot URL Postman**
XML
![Postman XML](images/Screenshot%20(1748).png)
JSON
![Postman JSON](images/Screenshot%20(1749).png)
XML With ID
![Postman XML with ID](images/Screenshot%20(1750).png)
JSON With ID
![Postman JSON with ID](images/Screenshot%20(1751).png)

## Tugas 4
## Menjawab Pertanyaan
**1. Apa perbedaan antara HttpResponseRedirect() dan redirect()**

**HTTPResponseRedirect()**: Akan menghasilkan kode status HTTP 302 (Found/Moved Temporarily). Kemudian, kita harus untuk menuliskan path-nya secara manual dan lengkap atau absolut. Ini digunakan ketika ingin mengalihkan user untuk ke halaman lain. Contohnya adalah
```python
from django.http import HttpResponseRedirect

return HttpResponseRedirect("http://example.com/")
```
Ini akan mengarahkan user ke "http://example.com/". Hal ini biasanya digunakan setelah selesai/berhasil melakukan sesuatu (user mengirim form).

**redirect()**: Berbeda dengan HTTPResponseRedirect() yang harus menuliskan URL secara manual, redirect dapat memasukkan URL, nama view, atau objek model, kemudian tidak hanya menerima URL atauu path absolut saja. Contohnya
```python
from django.shortcuts import redirect
redirect("/example/")
redirect("home_view")
```

**2. Jelaskan cara kerja penghubungan model Product dengan User!**

Potongan kode di bawah untuk menghubungkan satu product entry dengan satu user. Hubungan ini menggunakan ForeignKey, yang memungkinkan untuk menentukan siapa pemilik product entry tersebut.  
```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Kemudian, on_delete=models.CASCADE membuat program jika user tersebut dihapus, maka semua product yang terkait dengan user tersebut juga akan dihapus.
Pada views, produk yang dimiliki oleh pengguna yang sedang login saat ini akan ditampilkan, dan produk baru yang dibuat oleh pengguna otomatis akan dikaitkan dengan akun pengguna yang sedang login. 

**3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

Perbedaan antara authentication dan authorization adalah, 
Authentication: Untuk memastikan siapa pengguna dengan melakukan verifikasi username dan password yang dilakukan ketika pengguna mencoba masuk ke sistem.
Authorization : Untuk menentukan apa yang bisa dilakukan oleh pengguna dengan memeriksa hak akses dari si pengguna yang dilakukan setelah pengguna berhasil untuk login dan mencoba mengakses resource.

Hal-hal yang dilakukan saat pengguna login yaitu authentication, sistem memeriksa kredensial (username dan password) terhadap database. Setelah berhasil login, Django akan membuatkan session untuk pengguna yang disimpan dalam cookie. 

Menurut, django documentation, sistem autentikasi Django menangani authentication dan authorization. Sistem authentication dengan menggunakan `AuthenticationForm()` yaitu form bawaan yang otomatis memverifikasi kredensial user. Fungsi ini memeriksa apakah data yang dimasukkan sudah cocok dengan yang ada di database. Jika sesuai bisa langsung menggunakan fungsi `login()`. Kemudian, untuk sistemm authorization yaitu dengan menggunakan  
```python
@login_required(login_url='/login')
def show_main(request):
```
Kode di atas mengharuskan pengguna untuk login dulu sebelum bisa mengakses show_main. 

**4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

Django mengingat pengguna yang telah login dengan autentikasi, session, dan juga cookies. Setelah autentikasi berhasil, pengguna akan disimpan di session server-side. Kemudian Django dapat menggunakan cookies untuk menyimpan informasi tambahan seperti last login. Cookies disimpan di perangkat pengguna dan dikirimkan bersama dengan setiap HTTP Request ke server. 

Selain kegunaan di atas, cookies dapat digunakan untuk menyimpan preferensi pengguna, mengenali pengguna sehingga pengguna tidak memerlukan login ulang, jika pada situs e-commerce maka cookies mengelola keranjang belanja pengguna. 

Tidak semua cookies aman untuk digunakan, cookies dapat entan terhadap serangan keamanan jika tidak dikelola dengan baik, sehingga Django memiliki fitur untuk menyimpan informasi sensitif di database bukan di cookies.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

Langkah yang saya implementasikan untuk memenuhi checklist yaitu;
1. Mengaktifkan virtual environment.

2. Menambahkan import dan fungsi register pada `views.py`, 
```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
Kode di atas untuk membuat form tanpa harus menulis kode dari awal. 
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
Kode di atas untuk membuat form registrasi, jika valid akan membuat akun baru lalu akan diarahkan ke halaman login. 

3. Membuat dan mengisi file HTML dengan nama `register.html` pada folder templates.
```html
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
Kode di atas digunakan untuk menampilkan form register, proses input, kemudian juga memanfaatkan csrf_token.
4. Menambahkan kode import dan urlpatterns pada `urls.py`
```python
from main.views import register

 urlpatterns = [
     ...
     path('register/', register, name='register'),
 ]
```
Kode di atas untuk routing fungsi register agar dapat digunakan.

4. Menambahkan import dan fungsi login_user pada file `views.py`
```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
Kode di atas untuk menangani login user, memverifikasi kredensial, jika valid maka akan diarahkan ke halaman utama (show_main). Jika unvalid, maka form login akan ditampilkan lagi.

5. Membuat dan mengisi berkas baru login.html pada folder main/templates.
```html
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
Kode di atas untuk membuat halaman login. Menampilkan form login, memproses input, dan menampilkan pesan. 

6. Menambahkan kode import dan url pattern pada file `urls.py`
```python
from main.views import login_user
urlpatterns = [
   ...
   path('login/', login_user, name='login'),
]
```
Kode di atas untuk routing fungsi login agar dapat digunakan. 

7. Menambahkan import dan fungsi logout_user pada file views.py
```python
from django.contrib.auth import logout
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
Kode di atas untuk menghapus sesi pengguna yang sedang login dan mengarahkan user ke halaman login.

8. Menambahkan potongan kode pada berkas main.html yang berada pada folder main/templates
```html
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```

9. Menambahkan kode import dan url pattern pada file `urls.py`
```python
from main.views import logout_user
urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),
]
```
Kode di atas untuk routing fungsi logout agar dapat digunakan. 

10. Menambahkan kode import dan potongan kode @login_required(login_url='/login') pada file `views.py`
```python
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login')
def show_main(request):
...
```
11. Cek halaman login di http://localhost:8000/

12. Menambahkan kode import dan mengubah kode pada login_user agar dapat menggunakan cookie last login pada file `views.py`
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

...
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
...
```
Kode di atas untuk melakukan login, membuat response, dan membuat cookie last_login dan menambahkan ke dalam response.

13. Mengganti potongan kode pada show_main ke variable context
```python
context = {
    ...
    'last_login': request.COOKIES['last_login'],
}
```
Kode di atas untuk menambahkan last_login agar dapat terlihat di web.

14. Mengubah fungsi logout_user
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
15. Menambahkan potongan kode pada `main.html`
```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

16. Membuat satu akun pada halaman web.

17. Menambahkan kode pada `models.py`
```python
from django.contrib.auth.models import User
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
Kode di atas untuk menghubungkan satu product entry dengan satu user. 

18. Mengubah potongan kode pada fungsi `create_product_entry` pada file `views.py`
```python
def create_product_entry(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
19. Mengubah kode pada variable product_entries dan context menjadi
```python
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)
    context = {
        ...
        'name': request.user.username,
        ...
    }
```

20. Melakukan migrasi model 
```bash
python manage.py makemigrations
```
Memilih `1` saat muncul error pertama dan kedua. 
```bash 
python manage.py migrate
```

21. Menambahkan import pada settings.py dan mengubah variabel DEBUG.
```python
import os
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```

## Tugas 5
## Menjawab Pertanyaan
**1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**
Urutan prioritas pengambilan CSS selector yaitu;
1. Inline styles
2. ID Selector (dengan menggunakan #),
3. Class Selector (dengan menggunakan .), dan
4. Element Selector (tanpa menggunakan # atau .).

Hal ini dibuktikan apabila ketika kita membuat suatu HTML berisikan 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Element selector */
        p {
            color: blue;
        }

        /* Class selector */
        .text {
            color: green;
        }

        /* ID selector */
        #unique {
            color: purple;
        }

        /* Inline style akan menggantikan semua di atas */
    </style>
</head>
<body>
    <p>This is a regular paragraph.</p>
    <p class="text">This is a paragraph with a class.</p>
    <p id="unique" class="text">This is a paragraph with an ID and a class.</p>
    <p id="unique" class="text" style="color: red;">This is a paragraph with an ID, a class, and an inline style.</p>
</body>
</html>
```
maka akan mengeluarkan, 
This is a regular paragraph. (Berwarna biru)
This is a paragraph with a class. (Berwarna hijau)
This is a paragraph with an ID and a class. (Berwarna ungu)
This is a paragraph with an ID, a class, and an inline style. (Berwarna merah)

dalam contoh di atas;
Paragraf pertama akan berwarna biru karena hanya menggunakan type selector p dan tidak ada class, ID, atau inline style. 
Paragraf kedua akan berwarna hijau karena selector class .text lebih spesifik daripada selector elemen p.
Paragraf ketiga akan berwarna ungu karena selector ID #unique lebih spesifik daripada selector class .text dan type selector p.
Paragraf keempat akan berwarna merah karena inline style memiliki prioritas tertinggi dan akan menggantikan aturan dari ID, class, atau type selector.

**2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**
Ada beberapa alasan mengapa responsive design menjadi konsep yang penting, antara lain;
1. Efektivias biaya, dengan responsive design, dapat menghemat biaya dengan menghilangkan biaya untuk membayar situs seluler karena satu responsive design dapat menarik pengunjung dari semua pengguna perangkat yang berbeda. Responsive design memungkinkan pengembang mengelola satu kode sumber yang dapat berjalan di semua perangkat,
2. Meningkatkan pengalaman pengguna, pengguna mendapatkan tampilan yang optimal meskipun perangkat yang digunakan berbeda-beda, sehingga memberikan pengalaman pengguna yang lebih baik dan konsisten,
3. Search engine optimization , atau SEO, adalah strategi yang digunakan oleh banyak perusahaan untuk membantu meningkatkan peringkat mereka di halaman pencarian Google. Apabila suatu web menggunakan responsive design, maka lebih mungkin muncul dalam hasil pencarian yang lebih baik.

Contoh aplikasi yang sudah menerapkan responsive design adalah Tokopedia dan yang belum menerapkan responsive design adalah beberapa situs web pemerintahan.

**3.Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut! Jelaskan konsep flex box dan grid layout beserta kegunaannya!**
Margin, border, dan padding adalah bagian dari box model CSS yang menentukan tata letak dan spacing elemen HTML. Perbedaan antara adalah margin, border, dan padding adalah
1. Margin: Ruang di luar border elemen. Margin mengatur jarak antara elemen yang berbeda (kotak) dan antara elemen (kotak) dengan tepi layar. 
2. Border: Garis yang mengelilingi konten dan padding elemen.
3. Padding: Ruang antara konten elemen dan bordernya. Padding menentukan spasi dalam, yang dapat mengontrol seberapa banyak warna latar belakang terlihat di sekitar konten.
Contoh penggunaannya adalah, misal kita ingin membuat kotak yang memiliki lebar total 350px dan tinggi total 80px;
```css
div {
  width: 320px;
  height: 50px;
  padding: 10px;
  border: 5px solid gray;
  margin: 0;
}
```
Sehingga perhitungannya:
  320px (lebar area konten)
+ 20px (padding kiri + padding kanan)
+ 10px (batas kiri + batas kanan)
= 350px (lebar total)

  50px (tinggi area konten)
+ 20px (padding atas + padding bawah)
+ 10px (batas atas + batas bawah)
= 80px (tinggi total)

Konsep flex box dan grid layout yaitu;
Flexbox adalah model layout satu dimensi yang dirancang untuk menyediakan cara yang lebih efisien dalam mengatur, meratakan, dan mendistribusikan ruang di antara item-item dalam sebuah container, bahkan saat ukurannya tidak diketahui. Flexbox dapat:
1. Membuat layout responsif dengan mudah
2. Mengatur alignment dan distribusi ruang antar item
3. Mengubah urutan tampilan item tanpa mengubah struktur HTML
4. Membuat navigasi dan menu yang fleksibel
5. Menyusun elemen dalam satu baris atau kolom

Grid Layout adalah sistem layout dua dimensi yang memungkinkan developer untuk membuat layout kompleks dengan lebih mudah dan konsisten. Grid membagi container menjadi baris dan kolom.
Grid Layout dapat;
1. Membuat layout kompleks dengan mudah
2. Mengatur konten dalam baris dan kolom secara bersamaan
3. Membuat desain responsifresponsive design yang konsisten
4. Mengelola whitespace dalam layout dengan lebih baik

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**
1. Menambahkan tag `<meta name="viewport">` dalam templates/base.html.
2. Menambahkan kode di bawah ini pada `base.html`;
```html
...
{% endblock meta %}
<script src="https://cdn.tailwindcss.com">
</script>
...
```
3. Menambahkan fungsi baru `edit_product` pada views.py;
```python
def edit_product(request, id):
    product = Product.objects.get(pk = id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```
4. Menambahkan import `view.py`
```python
from django.shortcuts import .., reverse
from django.http import .., HttpResponseRedirect
```
5. Membuat HTML baru dengan `edit_product.html` pada `main/templates`
```html
{% extends 'base.html' %}
{% load static %}
{% block content %}

<h1>Edit Mood</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Product"/>
            </td>
        </tr>
    </table>
</form>
{% endblock %}
```
6. Menambahkan import fungsi `edit_product` pada `urls.py` dan menambahkan path url
```python
from main.views import edit_mood
path('edit-product/<uuid:id>', edit_product,name='edit_product'),
```

7. Menambahkan kode ini pada `main.html` 
```html
<td>
        <a href="{% url 'main:edit_product' product_entry.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
</tr>
```

8. Menambahkan fungsi baru `delete_product` pada `views.py`
```python
def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```

9. Menambahkan import fungsi `delete_product` pada `urls.py` dan menambahkan path url
```python
from main.views import delete_product
path('delete/<uuid:id>', delete_product, name='delete_product'), 
...
```

10. Menambahkan kode di bawah ini ke dalam file `main.html`;
```html
<td>
        <a href="{% url 'main:edit_mood' mood_entry.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
    <td>
        <a href="{% url 'main:delete_mood' mood_entry.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
</tr>
```

11. Membuat HTML baru dengan nama `navbar.html` pada folder `templates/` dan mengisinya dengan kode;
```html
<nav class="bg-gray-800 shadow-lg fixed top-0 left-0 z-40 w-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
            <div class="flex items-center">
                <a href="{% url 'main:show_main' %}" class="text-2xl font-bold text-yellow-500">SPARERAVEL</a>
            </div>
            <div class="hidden md:flex items-center">
                <a href="{% url 'main:show_main' %}" class="block text-gray-300 hover:text-white px-3 py-2 rounded-md text-base font-medium">Home</a>
                <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-base font-medium">Products</a>
                <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-base font-medium">Categories</a>
                <a href="#" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-base font-medium">Cart</a>
                {% if user.is_authenticated %}
                    <span class="text-gray-300 mr-4">Hello, {{ user.username }}</span>
                    <a href="{% url 'main:logout' %}" class="text-center bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded transition duration-300">
                        Logout
                    </a>
                {% else %}
                    <a href="{% url 'main:login' %}" class="text-center bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
                        Login
                    </a>
                    <a href="{% url 'main:register' %}" class="text-center bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded transition duration-300">
                        Register
                    </a>
                {% endif %}
            </div>
            <div class="md:hidden flex items-center">
                <button class="mobile-menu-button">
                    <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                        <path d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
        </div>
    </div>
    
    <div class="mobile-menu hidden md:hidden px-4 w-full">
        <div class="pt-2 pb-3 space-y-1 mx-auto">
        <a href="{% url 'main:show_main' %}" class="block text-gray-300 hover:text-white px-3 py-2 rounded-md text-base font-medium">Home</a>
        <a href="#" class="block text-gray-300 hover:text-white px-3 py-2 rounded-md text-base font-medium">Products</a>
        <a href="#" class="block text-gray-300 hover:text-white px-3 py-2 rounded-md text-base font-medium">Categories</a>
        <a href="#" class="block text-gray-300 hover:text-white px-3 py-2 rounded-md text-base font-medium">Cart</a>
            {% if user.is_authenticated %}
                <span class="block text-gray-300 px-3 py-2">Hello, {{ user.username }}</span>
                <a href="{% url 'main:logout' %}" class="block text-center bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Logout
                </a>
            {% else %}
                <a href="{% url 'main:login' %}" class="block text-center bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
                    Login
                </a>
                <a href="{% url 'main:register' %}" class="block text-center bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded transition duration-300">
                    Register
                </a>
            {% endif %}
        </div>
    </div>
    <script>
        const btn = document.querySelector("button.mobile-menu-button");
        const menu = document.querySelector(".mobile-menu");

        btn.addEventListener("click", () => {
            menu.classList.toggle("hidden");
        });
    </script>
  </nav>
```

12. Menautkan navbar tersebut ke dalam `main.html`, `create_mood_entry.html,` dan `edit_mood.html` yang berada di subdirektori `main/templates/`
```html
{% extends 'base.html' %}
{% block content %}
{% include 'navbar.html' %}
...
{% endblock content%}
```

13. Pada settings.py, tambahkan middleware WhiteNoise.
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
    ...
]
```

14. Konfigurasi pada settings.py dengan menambahkan pada variabel  `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL`;
```python
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static' 
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static' 
```
15. Membuat `global.css` pada `/static/css` 
16. Memodifikasi `base.html` dengan menambahkan kode;
```html
 <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
  </head>
```
17. Modifikasi `global.css` pada `static/css/global.css`;
18. Mengkustomisasi `register.html` pada `main/templates/`
19. Membuat dan mengkustomisasi file `card_info.html` pada `main/templates`
20. Membuat dan mengkustomisasi file `card_product.html` pada `main/templates`
21. Menambahkan `card_info.html`, `card_product.html`, dan `sedih-banget.png` ke template `main.html`
22. Mengkustomisasi `create_mood_entry.html` pada `main/templates/`
23. Mengkustomisasi `edit_product.html` pada `main/templates/`


## Tugas 6
## Menjawab Pertanyaan
**1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**

Manfaat JavaScript antara lain adalah;
1. Memungkinkan elemen pada halaman web menjadi interaktif
2. Memanipulasi struktur, gaya dan konten halaman web secara dinamis melalui Document Object Model
3. Melalui AJAX, JavaScript dapat melakukan permintaan ke server tanpa memuat ulang halaman (asinkron)
4. Mengurangi beban server dan meningkatkan kecepatan aplikasi secara keseluruhan
5. Memungkinkan pengembang menjalankan tugas-tugas tanpa menghambat proses utama (main thread).

**2.Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?**
`await` digunakan bersama fetch() untuk menangani operasi asinkron dengan cara yang lebih mudah dibaca dan dipahami. `await`membuat eksekusi kode berhenti sampai Promise yang dikembalikan oleh fetch() selesai (resolved) atau gagal (rejected).

Apabila kita tidak menggunakan `await`, maka kode akan terus dieksekusi tanpa menunggu fetch() selesai, yang bisa menyebabkan masalah jika kode selanjutnya bergantung pada hasil fetch. fetch() akan langsung mengembalikan Promise, bukan hasil aktual dari permintaan.

Note: *promise* adalah objek yang merepresentasikan penyelesaian atau kegagagalan dalam operasi asinkronus.


**3. Mengapa kita perlu menggunakan decorator `csrf_exempt` pada *view* yang akan digunakan untuk AJAX POST?**
`@csrf_exempt` digunakan untuk menonaktifkan pemeriksaan CSRF pada view yang akan menerima AJAX POST request. Kedua, menggunakan `csrf_exempt` pada *view* tertentu memungkinkan developer untuk lebih mudah menangani permintaan AJAX tanpa harus secara manual menyertakan token CSRF di setiap permintaan. Kemudian, dengan `csrf_exempt`, kita dapat memilih *view* mana yang memerlukan perlindungan tersebut (fleksibel).

**4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (*backend*) juga. Mengapa hal tersebut tidak dilakukan di *frontend* saja?**
Apabila hanya dilakukan di frontend saja, ada kemungkinan dapat di bypass oleh pelaku serangan siber (lebih rentan terhadap serangan). Oleh karena itu menambahkan pembersihan data input di backend juga diperlukan. Verifikasi di backend sebagai pertahanan lapis pertama terhadap serangan XSS, dan lain-lainnya. Validasi di backend memastikan bahwa data yang diterima selalu memenuhi kriteria yang diinginkan. Kemudian pada backend, menjamin konsistensi data karena validasi lebih kompleks. 

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**
1. Menambahkan error message pada view login_user di views.py
2. Membuat fungsi untuk menambahkan product dengan menggunakan AJAX;
a. Menambahkan import `csrf_exempt` dan `require_POST`,
b. Membuat fungsi baru pada views.py dengan nama   `add_product_entry_ajax` dengan mengguakan decorator yang sudah diimport
3. Melakukan routing fungsi `add_product_entry_ajax`; menambahkan import fungsi dan path url
4. Menampilkan data Product dengan fetch();
a. Menghapus baris ini dalam `views.py`
```python
mood_entries = MoodEntry.objects.filter(user=request.user)
```
dan 
```python
'mood_entries': mood_entries,
```
b. Ubah baris pertama pada `show_json` dan `show_xml` di `views.py` dengan;
```python
data = Product.objects.filter(user=request.user)
```
c. Menghapus bagian block conditional `product_entries` lalu menggantinya dengan 
```html
<div id="mood_entry_cards"></div>
```
d. Menambahkan `<script>`, fungsi getProductEntries(), refreshProductEntries().
5. Membuat modal sebagai form 
a. Implementasi modal (Tailwind) pada aplikasi
b. Menambahkan fungsi-fungsi JavaScript seperti showModal() dan hideModal()
c. Menambahkan tombol baru sebagai tombol penambahan data dengan AJAX

6. Menambahkan data Product dengan AJAX
a. Membuat fungsi addProductEntry() pada block `<script>`
b. Menambahkan event listener pada form yang ada di modal untuk menjalankan addProductEntry()

7. Melindungi aplikasi dari XSS
a. Menambahkan import `strip_tags` pada `views.py` dan `forms.py`
b. Menggunakan strip_tags pada fungsi add_product_entry_ajax
c. Menambahkan method clean_(field yang menggunakan strip_tags)

8. Membersihkan data dengan DOMPurify
a. Menambahkan kode ini pada `main.html`
```html
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
```
b. Lalu, menambahkan DOMPurify pada field yang menggunakan strip_tags.