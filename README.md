# eirblue-shop

Link PWS: http://aisyah-hastomo-eirblueshop.pbp.cs.ui.ac.id/

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


#############################################################################################################################################

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Untuk mengirimkan data dari suatu stack ke stack lainnya.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Keduanya memiliki kelebihannya masing-masing. JSON lebih ringan dan cepat daripada XML. Namun, XML memiliki fitur yang tidak ada pada JSON seperti namspaces dan attributes. Untuk memilih mana yang lebih baik, harus mempertimbangkan apa yang dibutuhkan platform, seperti data strukturnya dan performa yang dibutuhkan.
    JSON lebih populer karena mudah dibaca dan ringan sehingga saat data delivery lebih cepat.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    is_valid digunakan untuk memvalidasi isi form sehingga dapat terhindari terjadinya error saat pemrosesan form.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    csrf_token dibutuhkan untuk memberikan token yang rahasia, unik, dan tidak dapat diprediksi nilainya pada objek model untuk menghindari adanya serangan CSRF (Cross-Site Request Forgery). Jika csrf_token tidak digunakan, maka ID dari objek model dapat dienumerasi dan ini akan menjadi celah keamanan form Django. Penyerang dapat memanfaatkannya untuk mendapatkan autentikasi palsu dan melakukan hal yang tidak diinginkan pada situs.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat input form untuk menambahkan objek model pada app sebelumnya.
        - Buat berkas forms.py pada direktori main
        - Pada forms.py, import ModelForm dan Product
        - Buat class yang inherit ModelForm dan beri variabel model dan fields
        - Pada views.py di direktori main, buat fungsi create_product yang memvalidasi form dan return hasil render
        - Tambahkan product pada show_main yang mengambil seluruh objek Product
        - Pada urls.py import fungsi create_product
        - Tambahkan path untuk mengakses fungsi create_product dalam variabel urlpatterns
        - Buat berkas create_product pada main/templates
    - Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
        - Pada views.py di direktori main, buat fungsi show_xml, show_json, show_xml_by_id, show_json_by_id
        - Fungsi show_xml dan show_json akan mengambil semua data objek product dan return hasil serialize data menjadi format xml dan json.
        - Fungsi show by id memiliki kegunaan yang sama hanya saja juga menerima parameter id dan akan memfilter data sesuai id
    - Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
        - Import keempat fungsi ke dalam urls.py pada direktori main
        - Tambahkan path url setiap fungsi pada urlpatterns
     
![show_xml](https://github.com/user-attachments/assets/b963c1ec-8b41-42a3-a61e-8c1375a03a7b)
![show_json](https://github.com/user-attachments/assets/47c3b24f-1c9a-45a8-aa05-d5a91ebb22a0)
![show_xml_by_id](https://github.com/user-attachments/assets/981e3282-1a05-44ac-986f-618a78b3acfa)
![show_json_by_id](https://github.com/user-attachments/assets/13144117-5985-494e-a444-bcea5626ef85)




