# eirblue-shop

TUGAS 2

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
TUGAS 3

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


#############################################################################################################################################
TUGAS 4

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
HttpResponseRedirect hanya bisa menerima url sebagai argumentnya, sedangkan redirect bisa menerima views, models, maupun urls sebagai argumentnya.

2. Jelaskan cara kerja penghubungan model Product dengan User!
User harus diimport ke models.py dan ditambahkan sebagai salah satu attribute dari class Product. Pada views.py, tambahkan pada fungsi create_product sehingga saat pengisian form, object product akan menyimpan user yang sedang login sebagai atribut usernya.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah proses untuk memeriksa apakah user adalah benar. Authorization adalah untuk menentukan level of access dari user dan memberikan akses pada user sesuai level tersebut.
Authentication dan authorization kedua-duanya dilakukan saat pengguna login.
Django mengimplementasi authentication dengan meminta dan menyocokkan informasi username dan password pada login dengan user yang ada pada data.
Django mengimplementasi authorization dengan login_required atau permission_required.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan cookies untuk melakukan holding state. Session ID akan disimpan sebagai cookies pada klien kemudian dipetakan ke suatu struktur data pada sisi web server.
Cookies juga dapat menyimpan informasi terkait user selain session ID. Cookies juga dapat menyimpan preferences. Data yang disimpan pada cookies seharusnya aman, namun third-party cookies dapat membahayakan karena informasi personal user dapat bocor ke pihak yang tidak diinginkan.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
        Fungsi Registrasi
            - Import UserCreationForm dan message pada views.py di direktori main
            - Buat fungsi registrasi yang akan membuat form menggunakan UserCreationForm lalu memvalidasi dan menyimpan form tersebut sebelum memberikan message. Fungsi registrasi akan return redirect('main:login') jika form valid dan render(request, 'register.html', context) jika tidak
            - Buat template register.html pada direktori main\template
            - Import fungsi register dan tambahkan pathnya pada urls.py
        Fungsi Login
            - Import login_required dan restriksi halaman main
            - Import authenticate, login, AuthenticationForm, HttpResponseRedirect, reverse, dan datetime pada views.py
            - Buat fungsi login_user yang membuat dan memvalidasi form. Fungsi login_user kemudian akan get user dan redirect laman ke main jika form valid
            - Buat template login.html
            - Import fungsi login_user dan tampahkan path pada urls.py
        Fungsi Logout
            - Import logout pada views.py
            - Tambahkan last_login pada show_main
            - Buat fungsi logout_user yang akan menghapus cookie last_login dan redirect ke laman login
            - Tambahkan button logout dan kalimat sesi login terakhir pada main.html
            - Import fungsi logout_user dan tambahkan path pada urls.py
    - Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
        - Menghubungkan model Product dengan User
        - Registrasi dua akun
        - Create 3 product pada masing-masing akun
    - Menghubungkan model Product dengan User.
        - Import User pada models.py
        - Tambahkan user pada class product
        - Menambahkan user pada product di create_product pada views.py
        - Ubah value products pada show_main dengan filter object by user
        - Ubah value name pada context menjadi username user
        - Jalankan makemigrations dan migrate
    - Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
        - Mengubah value name menjadi username dari user
        - Menyimpan cookie last_login pada context show_main
        - Menambahkan kalimat Sesi login terakhir pada main.html, set cookie last_login setiap login dan menghapusnya setiap logout


#############################################################################################################################################
TUGAS 5

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    1) Inline style
    2) External dan internal style sheets
    3) Browser default

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Agar aplikasi web tampil optimal pada device mana pun, baik yang layar kecil maupun besar, dan meningkatkan user experience. Contoh aplikasi yang sudah menerapkan responsive design adalah Youtube dan yang belum adalah gbf.wiki  

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin memengaruhi ruang di sekitar elemen, border adalah garis tepi dari elemen, sedangkan padding memengaruhi ruang di dalam elemen. Ketiga hal tersebut dapat diimplementasi pada bagian class dengan margin: m, border: border, padding: p.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox adalah module yang terbagi menjadi container dan itemnya yang bekerja sebagai mode pengaturan atau konsep layout. Flexbox digunakan untuk menyusun item dalam satu dimensi (row atau column). Grid adalah CSS yang dapat membagi kolom pada website baik secara horizontal dan vertikal. Grid digunakan untuk menyusun item dalam dua dimensional.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    - Implementasikan fungsi untuk menghapus dan mengedit product.
        - Membuat fungsi edit_product dan delete_product di views.py. edit_product menerima parameter id dan menampilkan form. delete_product menerima parameter id dan menghapus product.
        - Import kedua fungsi pada urls.py dan tambahkan path.
        - Buat template edit_product.html.
        - Implementasikan fungsi pada main.html
    - Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
        - Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
        - Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
            - Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
            - Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
        - Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
        - Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
            - Tambahkan script tailwind pada base.html
            - Buat global.css pada static/css
            - Tambahkan file global.css pada base.html
            - Buat aturan untuk class yang dibutuhkan pada global.css
            - Buat card_info.html untuk npm, nama, dan kelas serta card_product.html sebagai template untuk product jika sudah ada yang terdaftar.
            - Buat navbar.html di folder template pada root folder sebagai template untuk navigation bar.
            - Buat div dan edit pada class warna, font, text, bentuk, margin, padding, border, transition, dan lainnya.
            - Tambahkan folder image pada static dan tambahkan image sad.png untuk dipakai di main.html saat belum ada product, halaman akan menampilkan bahwa belum ada product yang terdaftar
            - Masukkan navbar.html ke create_product.html, edit_product.html, dan main.html
            - Implementasikan setiap template di main ke dalam main.html

#############################################################################################################################################
TUGAS 6

1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
    Agar manipulasi halaman web dapat dilakukan secara dinamis dan interaksi antara halaman web dengan pengguna dapat meningkat karena JavaScript mendukung konsep pemrograman berbasis obyek, pemrograman imperatif, dan pemrograman fungsional.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
    Fungsi await digunakan untuk menunggu hasil dari fungsi async. Fungsi await akan membuat function menghentikan eksekusinya dan menunggu resolved promise sebelum lanjut.
    Fungsi await hanya bisa digunakan di function async dan jika tidak digunakan pada suatu value, function tidak akan menghentikan eksekusinya dan menunggu value diambil sebelum lanjut.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
    Decorator csrf_exempt membuat Django tidak perlu mengecek keberadaan csrf_token pada POST request yang dikirimkan ke fungsi pada view. Cek csrf token tidak esensial saat sudah login.

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
    Untuk mencegah terjadinya celah keamanan Cross Site Scripting atau XSS.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
     AJAX GET
        - Ubahlah kode cards data mood agar dapat mendukung AJAX GET.
            Hapus bagian block conditional pada main.html
            Tambahkan div kosong dengan id=product_cards
         -Lakukan pengambilan data mood menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
            Pada function show_json, ubah menjadi data yang didapat dari filter Product berdasarkan user logged-in.
            Pada script di main.html, buat async function getProducts yang akan fetch API ke data JSON dan selanjutnya melakukan parse pada data JSON menjadi objek JavaScript.
    AJAX POST
        - Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
            Menambahkan tombol dengan data-modal-target="crudModal", data-modal-toggle="crudModal", dan onclick="showModal() pada main.html.
        - Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data.
            Buat fungsi add_product_ajax pada views.py yang menerima parameter request dan get product data field lalu membuat new_product
        - Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
            Impor fungsi add_product_ajax pada urls.py dan tambahkan path url untuk mengakses fungsi tersebut
        - Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
            Buat function addProduct pada script di main html yang akan fetch create-ajax dan membuat FormData baru yang datanya diambil dari form pada modal.
        - Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan.
            Buat async function refreshProduct
            Buat const products yang await dari fungsi getProduct
            Pada function addProduct panggil refreshProduct setelahnya