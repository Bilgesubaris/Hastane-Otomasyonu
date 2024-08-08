import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Entry, Button, Listbox, Radiobutton, StringVar
import random
import string

patients_details = []
basvurular = [
    {"tip": "Doktor", "isim": "Dr. Ahmet Yılmaz", "dogum_tarihi": "01.01.1980", "uni": "Hacettepe Üniversitesi", "bolum": "Kardiyoloji"},
    {"tip": "Doktor", "isim": "Dr. Elif Kaya", "dogum_tarihi": "15.05.1985", "uni": "İstanbul Üniversitesi", "bolum": "Pediatri"},
    {"tip": "Doktor", "isim": "Dr. Mehmet Öz", "dogum_tarihi": "23.03.1979", "uni": "Ankara Üniversitesi", "bolum": "Genel Cerrahi"},
    {"tip": "Sekreter", "isim": "Zeynep Yıldız", "dogum_tarihi": "12.06.1992", "uni": "Anadolu Üniversitesi", "bolum": "Sağlık Yönetimi"},
    {"tip": "Sekreter", "isim": "Ayşe Çelik", "dogum_tarihi": "30.11.1990", "uni": "Ege Üniversitesi", "bolum": "Halkla İlişkiler"},
]
doctors_details = [
    {"ad": "Dr. Ayşe Yılmaz" ,"bolum": "Kulak,Burun Boğaz Hastalıkları"},
    {"ad": "Dr. Ahmet Demir", "bolum": "Kulak,Burun Boğaz Hastalıkları"},
    {"ad": "Dr. Özlem Kaya","bolum": "Nöroloji"},
    {"ad": "Dr. Emre Avcı", "bolum": "Nöroloji"},
    {"ad": "Dr. Ali Akın","bolum": "Dahiliye"},
    {"ad": "Dr. Sema Öztürk", "bolum": "Dahiliye "},
    {"ad": "Dr. Fatma Demir", "bolum": "Kadın Doğum ve Hastalıkları"},
    {"ad": "Dr. Hasan Yılmaz", "bolum": "Kadın Doğum ve Hastalıkları"},
    {"ad": "Dr. Özlem Kaya", "bolum": "Üroloji"},
    {"ad": "Dr. Emre Avcı", "bolum": "Üroloji"},
    {"ad": "Dr. Elif Arslan","bolum": "Pediatri" },
    {"ad": "Dr. Murat Yıldız", "bolum": "Pediatri"},

]

class AnaEkran:
    def __init__(self, root):
        self.root = root
        self.root.title("Hastane Otomasyonu")
        self.root.geometry("500x500")
        self.root.configure(bg="ivory")

        self.sekreter_button = Button(root, text="Sekreter", command=self.sekreter_giris_ac, font=("Arial", 20, "bold"), bg="ivory")
        self.sekreter_button.pack(pady=30)

        self.doktor_button = Button(root, text="Doktor", command=self.doktor_giris_ac, font=("Arial", 20, "bold"), bg="ivory")
        self.doktor_button.pack(pady=30)

        self.admin_button = Button(root, text="Yönetici", command=self.admin_giris_ac, font=("Arial", 20, "bold"), bg="ivory")
        self.admin_button.pack(pady=30)

    def sekreter_giris_ac(self):
        SekreterGiris(self.root)

    def doktor_giris_ac(self):
        DoktorGiris(self.root)

    def admin_giris_ac(self):
        AdminGiris(self.root)

class SekreterGiris:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Sekreter Giriş Ekranı")
        self.root.geometry("500x500")
        self.root.configure(bg="lightcyan")

        # Kullanıcı adı ve şifre alanları
        self.username_label = Label(self.root, text="Kullanıcı Adı:", bg="lightcyan")
        self.username_label.pack()
        self.username_entry = Entry(self.root)
        self.username_entry.pack()

        self.password_label = Label(self.root, text="Şifre:", bg="lightcyan")
        self.password_label.pack()
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()

        # Giriş butonu
        self.giris_button = Button(self.root, text="Giriş Yap", command=self.giris_kontrol, bg="lightcyan")
        self.giris_button.pack(pady=10)

    def giris_kontrol(self):
        # Burada gerçek bir doğrulama yapılabilir, şimdilik basitçe kontrol ediyoruz
        if self.username_entry.get() == "sekreter" and self.password_entry.get() == "1234":
            messagebox.showinfo("Başarılı", "Sekreter olarak giriş yaptınız!")
            self.root.destroy()  # Giriş ekranını kapat
            SekreterEkran()  # Sekreter ekranını aç
        else:
            messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre")

import tkinter as tk
from tkinter import messagebox, Scrollbar, Listbox, Entry, Label, Button

class SekreterEkran:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sekreter Ekranı")
        self.root.geometry("800x700")
        self.root.configure(bg="lightblue")

        self.isim_label = Label(self.root, text="Hasta İsmi:", bg="lightblue", font=("Arial", 15))
        self.isim_label.pack()
        self.isim_entry = Entry(self.root, width=30)
        self.isim_entry.pack()

        self.dogum_tarihi_label = Label(self.root, text="Doğum Tarihi (GG.AA.YYYY):", bg="lightblue", font=("Arial", 15))
        self.dogum_tarihi_label.pack()
        self.dogum_tarihi_entry = Entry(self.root, width=30)
        self.dogum_tarihi_entry.pack()

        self.tc_label = Label(self.root, text="TC Kimlik Numarası:", bg="lightblue")
        self.tc_label.pack()
        self.tc_entry = Entry(self.root, width=30)
        self.tc_entry.pack()

        self.bolum_label = Label(self.root, text="Hastane Bölümleri", bg="lightblue")
        self.bolum_label.pack()

        self.bolum_listbox = Listbox(self.root, selectmode=tk.SINGLE, width=40)
        self.bolum_listbox.pack()

        bolumler = [
            "Kulak Burun Boğaz Hastalıkları",
            "Nöroloji",
            "Dahiliye",
            "Pediatri",
            "Kadın Doğum ve Hastalıkları",
            "Üroloji"
        ]

        for bolum in bolumler:
            self.bolum_listbox.insert(tk.END, bolum)

        self.bolum_listbox.bind("<<ListboxSelect>>", self.doktor_listele)

        self.doktor_label = Label(self.root, text="Doktorlar ve Randevu Bilgileri", bg="lightblue")
        self.doktor_label.pack()

        self.doktor_listbox = Listbox(self.root, selectmode=tk.SINGLE, width=80)
        self.doktor_listbox.pack()

        self.randevu_label = Label(self.root, text="Randevu Kayıtları", bg="lightblue")
        self.randevu_label.pack()
        self.randevu_listbox = Listbox(self.root, selectmode=tk.SINGLE, width=80)
        self.randevu_listbox.pack()

        self.scrollbar1 = Scrollbar(self.root, orient=tk.VERTICAL)
        self.scrollbar1.config(command=self.doktor_listbox.yview)
        self.scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
        self.doktor_listbox.config(yscrollcommand=self.scrollbar1.set)

        self.scrollbar2 = Scrollbar(self.root, orient=tk.VERTICAL)
        self.scrollbar2.config(command=self.randevu_listbox.yview)
        self.scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
        self.randevu_listbox.config(yscrollcommand=self.scrollbar2.set)

        # Butonları frame içine yerleştirme
        button_frame = tk.Frame(self.root, bg="lightblue")
        button_frame.pack(pady=10)

        self.randevu_olustur_button = Button(button_frame, text="Randevu Oluştur", command=self.randevu_olustur)
        self.randevu_olustur_button.pack(side=tk.LEFT, padx=10)

        self.randevu_sil_button = Button(button_frame, text="Tüm Randevuları Sil", command=self.tum_randevulari_sil)
        self.randevu_sil_button.pack(side=tk.LEFT, padx=10)

        self.geri_button = Button(self.root, text="Geri", command=self.geri_don)
        self.geri_button.pack(pady=10)

        self.root.mainloop()

    def doktor_listele(self, event):
        bolum_indeksi = self.bolum_listbox.curselection()
        if bolum_indeksi:
            bolum = self.bolum_listbox.get(bolum_indeksi)
            self.doktor_listbox.delete(0, tk.END)

            if bolum == "Kulak Burun Boğaz Hastalıkları":
                doktorlar = [
                    {"ad": "Dr. Ayşe Yılmaz", "saat": "15:00"},
                    {"ad": "Dr. Ahmet Demir", "saat": "10:00"}
                ]
            elif bolum == "Nöroloji":
                doktorlar = [
                    {"ad": "Dr. Mehmet Yılmaz", "saat": "11:30"},
                    {"ad": "Dr. Zeynep Kaya", "saat": "15:30"}
                ]
            elif bolum == "Dahiliye":
                doktorlar = [
                    {"ad": "Dr. Ali Akın", "saat": "12:00"},
                    {"ad": "Dr. Sema Öztürk", "saat": "13:00"}
                ]
            elif bolum == "Pediatri":
                doktorlar = [
                    {"ad": "Dr. Elif Arslan", "saat": "08:30"},
                    {"ad": "Dr. Murat Yıldız", "saat": "09:30"}
                ]
            elif bolum == "Kadın Doğum ve Hastalıkları":
                doktorlar = [
                    {"ad": "Dr. Fatma Demir", "saat": "15:00"},
                    {"ad": "Dr. Hasan Yılmaz", "saat": "13:00"}
                ]
            elif bolum == "Üroloji":
                doktorlar = [
                    {"ad": "Dr. Özlem Kaya", "saat": "08:30"},
                    {"ad": "Dr. Emre Avcı", "saat": "12:30"}
                ]
            else:
                doktorlar = []

            for doktor in doktorlar:
                entry = f"{doktor['ad']} - Randevu Saatleri: {doktor['saat']}"
                self.doktor_listbox.insert(tk.END, entry)

    def randevu_olustur(self):
        selected_doktor = self.doktor_listbox.get(self.doktor_listbox.curselection())
        isim = self.isim_entry.get()
        dogum_tarihi = self.dogum_tarihi_entry.get()
        tc = self.tc_entry.get()

        if not selected_doktor or not isim or not dogum_tarihi or not tc:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurunuz ve bir doktor seçiniz.")
            return

        randevu = f"Randevu - {isim}, {dogum_tarihi}, {tc}, {selected_doktor}"
        self.randevu_listbox.insert(tk.END, randevu)

    def tum_randevulari_sil(self):
        self.randevu_listbox.delete(0, tk.END)

    def geri_don(self):
        self.root.destroy()

class DoktorGiris:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Doktor Giriş Ekranı")
        self.root.geometry("500x500")
        self.root.configure(bg="lightcyan")

        # Kullanıcı adı ve şifre alanları
        self.username_label = Label(self.root, text="Kullanıcı Adı:", bg="lightcyan")
        self.username_label.pack()
        self.username_entry = Entry(self.root)
        self.username_entry.pack()

        self.password_label = Label(self.root, text="Şifre:", bg="lightcyan")
        self.password_label.pack()
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()

        # Giriş butonu
        self.giris_button = Button(self.root, text="Giriş Yap", command=self.giris_kontrol, bg="lightcyan")
        self.giris_button.pack(pady=10)

    def giris_kontrol(self):
        # Burada gerçek bir doğrulama yapılabilir, şimdilik basitçe kontrol ediyoruz
        if self.username_entry.get() == "doktor" and self.password_entry.get() == "1234":
            messagebox.showinfo("Başarılı", "Doktor olarak giriş yaptınız!")
            self.root.destroy()  # Giriş ekranını kapat
            DoktorEkran()  # Doktor ekranını aç
        else:
            messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre")

class DoktorEkran:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Doktor Ekranı")
        self.root.geometry("500x600")
        self.root.configure(bg="lightcyan")

        self.label = Label(self.root, text="Doktor İşlemleri", font=("Arial", 12, "bold"), bg="lightcyan")
        self.label.grid(row=0, column=0, columnspan=2, pady=20)

        self.isim_label = Label(self.root, text="Hasta İsmi:", bg="lightcyan", anchor="e", justify="right")
        self.isim_label.grid(row=1, column=0, sticky="e")
        self.isim_entry = Entry(self.root, width=60)
        self.isim_entry.grid(row=1, column=1, padx=10, pady=5)

        self.tc_label = Label(self.root, text="TC Kimlik Numarası:", bg="lightcyan", anchor="e", justify="right")
        self.tc_label.grid(row=2, column=0, sticky="e")
        self.tc_entry = Entry(self.root, width=60)
        self.tc_entry.grid(row=2, column=1, padx=10, pady=5)

        self.hastalik_label = Label(self.root, text="Hastalık Belirtileri:", bg="lightcyan", anchor="e", justify="right")
        self.hastalik_label.grid(row=3, column=0, sticky="e")
        self.hastalik_entry = Entry(self.root, width=60)
        self.hastalik_entry.grid(row=3, column=1, padx=10, pady=5)

        self.yatis_label = Label(self.root, text="Yatış Verilecek Mi:", bg="lightcyan", anchor="e", justify="right")
        self.yatis_label.grid(row=4, column=0, sticky="e")
        self.yatis_var = StringVar(value="Hayır")
        self.yatis_evet_radio = Radiobutton(self.root, text="Evet", variable=self.yatis_var, value="Evet", bg="lightcyan")
        self.yatis_hayir_radio = Radiobutton(self.root, text="Hayır", variable=self.yatis_var, value="Hayır", bg="lightcyan")
        self.yatis_evet_radio.grid(row=4, column=1, sticky="w")
        self.yatis_hayir_radio.grid(row=4, column=1, padx=60, sticky="w")

        self.ilac_label = Label(self.root, text="İlaç:", bg="lightcyan", anchor="e", justify="right")
        self.ilac_label.grid(row=5, column=0, sticky="e")
        self.ilac_entry = Entry(self.root, width=40)
        self.ilac_entry.grid(row=5, column=1, padx=10, pady=5)

        self.olustur_button = Button(self.root, text="Kod Oluştur", command=self.kod_olustur, bg="lightcyan")
        self.olustur_button.grid(row=6, column=0, columnspan=2, pady=10)

    def kod_olustur(self):
        isim = self.isim_entry.get()
        tc = self.tc_entry.get()
        hastalik = self.hastalik_entry.get()
        yatis = self.yatis_var.get()
        ilac = self.ilac_entry.get()

        if not isim or not tc or not hastalik or not ilac:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurunuz.")
            return

        kod = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        messagebox.showinfo("Oluşturulan Kod", f"{isim} adlı hasta için oluşturulan kod: {kod}")

class AdminGiris:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Yönetici Giriş Ekranı")
        self.root.geometry("500x500")
        self.root.configure(bg="lightcyan")

        # Kullanıcı adı ve şifre alanları
        self.username_label = Label(self.root, text="Kullanıcı Adı:", bg="lightcyan")
        self.username_label.pack()
        self.username_entry = Entry(self.root)
        self.username_entry.pack()

        self.password_label = Label(self.root, text="Şifre:", bg="lightcyan")
        self.password_label.pack()
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()

        # Giriş butonu
        self.giris_button = Button(self.root, text="Giriş Yap", command=self.giris_kontrol, bg="lightcyan")
        self.giris_button.pack(pady=10)

    def giris_kontrol(self):
        
        if self.username_entry.get() == "admin" and self.password_entry.get() == "admin23":
            messagebox.showinfo("Başarılı", "Yönetici olarak giriş yaptınız!")
            self.root.destroy()  # Giriş ekranını kapat
            AdminEkran()  # Yönetici ekranını aç
        else:
            messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre")

class AdminEkran:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Yönetici Ekranı")
        self.root.geometry("600x500")
        self.root.configure(bg="lightcyan")
        
        self.label = Label(self.root, text="Doktor Listesi", font=("Arial", 12, "bold"), bg="lightcyan")
        self.label.pack(pady=10)
        self.doktor_listbox = Listbox(self.root, width=60)
        self.doktor_listbox.pack(pady=10)

        self.listele_button = Button(self.root, text="Doktorları Listele", command=self.doktorlari_listele, bg="lightcyan")
        self.listele_button.pack(pady=10)

        self.basvurulari_gor_button = Button(self.root, text="Başvuruları Görüntüle", command=self.basvurulari_goruntule, bg="lightcyan")
        self.basvurulari_gor_button.pack(pady=10)

    def doktorlari_listele(self):
        self.doktor_listbox.delete(0, tk.END)
        for doktor in doctors_details:
            self.doktor_listbox.insert(tk.END, f"{doktor['ad']} - Bölüm: {doktor['bolum']}")
    

    def basvurulari_goruntule(self):
        yeni_pencere = Toplevel(self.root)
        yeni_pencere.title("Başvurular Listesi")
        yeni_pencere.geometry("600x500")
        yeni_pencere.configure(bg="lightblue")

        basvurular_label = Label(yeni_pencere, text="Başvurular Listesi", font=("Arial", 12, "bold"), bg="lightblue")
        basvurular_label.pack(pady=10)

        basvurular_listbox = Listbox(yeni_pencere, width=80)
        basvurular_listbox.pack(pady=10)

        for basvuru in basvurular:
            basvurular_listbox.insert(tk.END, f"{basvuru['tip']} - {basvuru['isim']} - {basvuru['dogum_tarihi']} - {basvuru['uni']} - {basvuru['bolum']}")
        al_button = Button(self.root, text="İşe Al", command=lambda idx=index: self.ise_al(idx-1))
        al_button.pack()

    def ise_al(self, index):
        basvuru = basvurular[index]
        mesaj = f"{basvuru['tip']} - {basvuru['isim']} başvurusu işe alındı!"
        tk.messagebox.showinfo("Başvuru Durumu", mesaj)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnaEkran(root)
    root.mainloop()
