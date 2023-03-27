# TC Doğrulama
# Kurallar:
# * 11 hanelidir.
# * Her hanesi rakamsal değer içerir.(Araştırma)
# * İlk hane 0 olamaz.
# * 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından,
# 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında, elde edilen
# sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
# * 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde
# edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.


tc: str = input("TC: ")

if len(tc) != 11:
    print("TC geçersiz 11 haneli olmalıdır")
    if tc.isdigit():
        print()
        if tc[0] == 0:
            print("TC geçersiz")
        else:
            print()
            rakamlar = [int(r) for r in tc]
            if sum(rakamlar[:10]) % 10 == rakamlar[10]:
                print()
                a: int = int(7 * sum(rakamlar[0:9:2]) - sum(rakamlar[1:10:2]))
                if a % 10 == rakamlar[10]:
                    print("TC geçerli")
                else:
                    print("TC geçersiz")
            else:
                print("TC geçersiz")
    else:
        print("TC geçersiz sadece rakamlardan olusmalıdır.")
else:
    print("Tc Geçerli")