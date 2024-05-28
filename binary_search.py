def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # x midde bulunduysa
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

# Kullanım
arr = [2, 3, 4, 10, 40]
x = 10

# Fonksiyonu çağır ve sonucu kontrol et
result = binary_search(arr, x)

if result != -1:
    print("Eleman dizideki indeksi:", str(result))
else:
    print("Eleman dizide bulunamadı")
