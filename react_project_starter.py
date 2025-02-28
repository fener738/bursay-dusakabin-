import os

def main():
    print("React projesi için gerekli ortam hazırlanıyor...")

    # Node.js yüklü mü kontrol et
    node_check = os.system("node -v")
    if node_check != 0:
        print("Hata: Node.js yüklü değil! https://nodejs.org adresinden yükleyin.")
        return
    
    # Proje klasörüne gir
    project_folder = input("React projenizin olduğu klasörü girin: ")
    if not os.path.exists(project_folder):
        print("Hata: Belirtilen klasör bulunamadı!")
        return
    
    os.chdir(project_folder)
    
    # Gerekli bağımlılıkları yükle
    print("Bağımlılıklar yükleniyor...")
    os.system("npm install")

    # React uygulamasını başlat
    print("Uygulama başlatılıyor...")
    os.system("npm run dev")

if __name__ == "__main__":
    main()
