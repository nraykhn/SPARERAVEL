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
HTTPResponseRedirect(): Akan menghasilkan kode status HTTP 302 (Found/Moved Temporarily). Kemudian, kita harus untuk menuliskan path-nya secara manual dan lengkap atau absolut. Ini digunakan ketika ingin mengalihkan user untuk ke halaman lain. Contohnya adalah
```python
from django.http import HttpResponseRedirect

return HttpResponseRedirect("http://example.com/")
```
Ini akan mengarahkan user ke "http://example.com/". Hal ini biasanya digunakan setelah selesai/berhasil melakukan sesuatu (user mengirim form).
redirect(): Berbeda dengan HTTPResponseRedirect() yang harus menuliskan URL secara manual, redirect dapat memasukkan URL, nama view, atau objek model, kemudian tidak hanya menerima URL atauu path absolut saja. Contohnya
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



