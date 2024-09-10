Nama : Nur Alya Khairina
NPM : 2306275701
Kelas : PBP A


# SPARERAVEL
## 🔗 Links
[![PWS](]("C:\Users\nural\OneDrive\Gambar\Screenshot\Screenshot 2024-09-10 192407.png")](http://nur-alya31-spareravel.pbp.cs.ui.ac.id/)
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


![Gambar Bagan]("C:\Users\nural\Downloads\diagram pbp.png")


**Jelaskan fungsi** `Git` **dalam pengembangan perangkat lunak!**
- Git memungkinkan banyak developer untuk bekerja sama  dalam mengembangkan suatu perangkat lunak dengan penggunaan *branching*,
- Git memugkinkan melihat kode yang lama dan baru, sehingga dapat mengembalikan ke kode sebelumnya apabila ada keslahan,
- Git memberikan keuntungan bagi pengembang untuk memperbaiki *bug* tanpa takut kode hilang atau semakin salah,
- Setiap perubahan kode, akan secara otomatis diuji oleh Git.


**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

Menurut saya, ini disebabkan fitur-fiturnya yang cocok untuk awal belajar pengembangan perangkat lunak, seperti ORM, *routing* URL yang fleksibel, dan lain sebagainya. Kemudian Django juga membantu pemula dalam mengatur struktur aplikasi karena dalam Django semua sudah diatur dengan standar tertentu. Lalu seperti yang telah saya jelaskan, ORM membantu pemula karena tidak perlu memahami SQL dengan mendalam. 


**Mengapa model pada Django disebut sebagai ORM?**

ORM (Object Relation Mapper) hal ini dikarenakan model tersebut memiliki fungsi untuk menjadi jembatan antara database dan objek python tanpa harus menuliskan SQL Queries. ORM ini memetakan atribut objek ke masing-masing bidang tabel. ORM juga dapat mengambil data dengan cara tersebut.
