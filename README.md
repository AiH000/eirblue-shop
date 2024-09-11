# eirblue-shop

Link PWS: http://aisyah-hastomo-eirblue.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat projek Django baru
        - Membuat repositori baru pada git
        - Mengaktifkan virtual environment pada folder lokal
        - Menginstal depedencies pada requirements.txt
        - Membuat projek Django dengan perintah: django-admin startproject eirblue-shop .
    - Membuat aplikasi dengan nama 'main' pada proyek tersebut.
        - Menjalankan perintah: python manage.py startapp main
    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        - Mendaftarkan aplikasi 'main' dengan menambahkan 'main' pada 'INSTALLED_APPS' pada settings.py
    - Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut: name, price, description.
        - Mengimport models pada models.py
        - Membuat class Product
        - Menambahkan atribut: name, price, dan description pada class Product.
        - Menjalankan perintah makemigrations dan migrate.
    - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        - Menambahkan fungsi show_main pada views.py
        - Menambahkan dictionary 'context' yang memberikan value pada atribut dari model
        - Menambahkan return render(request, "main.html", context)
    - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        - Menambahkan import path dari django.urls pada urls.py
        - Menambahkan import show_main dari views.py (main.views)
        - Mengisi urls.py dengan app_name dan fungsi path()
    - Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        - Menekan tombol 'Create New Project' pada web PWS
        - Mengisi nama projek dengan 'eirblue_shop' lalu 'Create New Project'
        - Menyimpan username dan password dari PWS
        - Menambahkan url deployment PWS pada 'ALLOWED_HOST' di settings.py
        - Melakukan git add, commit, push pada github
        - Melakukan perintah dari PWS dan mengisi credential saat push ke PWS


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
 ______       _______                  _________    add, update, delete data    ___________
|      |     |       |  http request  |         |             -->              |  model.py |
|      |     |       |       -->      |         |             <--              |___model___|
|      |     |urls.py|                | view.py |       requested data
| user | --> |  web  |                |  view   |
|      |     |       |                |         |        dynamic data           __________
|      |     |       |       <--      |         |             -->              |   html   |
|______|     |_______| requested page |_________|             <--              |_template_|
                                                          data input            


3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git membantu dalam kontrol versi. Git menyimpan semua versi dari proyek setiap kali 'push'. Git memungkinkan penggunanya memantau revisi yang terjadi pada proyeknya seiring pengembangan perangkat lunaknya.


4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena Django fleksibel, dapat digunakan dalam web development, menggunakan bahasa python, dan dapat digunakan dalam kebanyakan OS.

5. Mengapa model pada Django disebut sebagai ORM?
Karena developer dapat berinteraksi dengan basis data relasional dengan python tanpa harus menulisnya pada SQL
