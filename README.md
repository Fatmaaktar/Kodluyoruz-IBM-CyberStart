# 💻 Kodluyoruz-IBM-CyberStartProgram   
![kodluyoruz-kodlama-gelecek-gelecegi-kodluyoruz-gelecek-burada](https://github.com/Fatmaaktar/Kodluyoruz-IBM-CyberStart/assets/106100226/b203294e-3eb4-417f-ae7e-76cdf70b2167)  


### 🐍 Python
🌟 90'lı yıllarda Amsterdam'da Guide Van Rossum tarafından geliştirildi.  
🌟Yorumlanabilen yüksek seviyeli bir programlama dilidir.  

#### Veri Tipleri  
<li>Programa istedğimizi yaptırmamız için girdilerimizi ve programın içinde kullanılacak verileri ifade etmemizi sağlar</li>  

1) Scalar veri tipleri (Tek bir değeri temsil eden veri tipleridir. Int,Float,Complex,Bool veri tipleri örnek olarak gösterilir) 
2) Non-Scalar veri tipleri (Birden fazla değeri içeren veri tipleridir. List,Tuple,Dict,Set veri tipleri örnek olarak gösterilir)  
   
<li>Her objenin bir tipi vardır ve pogram bu tiplere göre onlara nasıl işlem yapacağımızı belirler</li>   


🌟Metin tipleri: string 

🌟Sayısal tipler: int , float , complex

🌟Dizi tipleri:  list , tuple , range  

🌟Mantıksal tipler: bool   

📋 Python programlama dilinde bir değişken oluştururken o değişkenin tipini belirtmemize gerek yoktur. Python, oluşturduğunuz değişkene atayacağınız değer üzerinden otomatik olarak o değişkenin tipini algılayacaktır.  
📌**Örnek**  
a=5  (int olarak algılar)  
a="5" (string olarak algılar)  


 #### Değişken Atama  
  **Integer (Tam Sayılar)**

```python
x = 10
y = -5
z = 0
```

**Float (Ondalıklı Sayılar)**  
```python
a = 3.14
b = -0.001
c = 2.71828
```
**String (Metin):**  
```python
name = "John"
surname = 'Doe'
full_name = "John Doe"
```
**Boolean (Mantıksal Değerler):**
```python
is_sunny = True
is_raining = False

```
**List (Listeler):**
```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed_list = [10, "apple", True]
```
**Dictionary (Sözlükler):**
 ```python
person = {"name": "John", "age": 30, "city": "New York"}
car = {"brand": "Toyota", "model": "Camry", "year": 2022}
```  
**Set (Kümeler):**
```python
unique_numbers = {1, 2, 3, 4, 5}
vowels = {'a', 'e', 'i', 'o', 'u'}
```

 #### Operatörler   

##### Aritmetik Operatörler

- **Toplama (+):** İki değeri toplar.
  
- **Çıkarma (-):** İki değeri çıkarır.

- **Çarpma (*):** İki değeri çarpar.

- **Bölme (/):** İlk değeri ikinci değere böler.

- **Üs Alma (**):** İlk değerin ikinci değere üssünü alır.

- **Modülüs (Kalan) (%):** İlk değerin ikinci değere bölümünün kalanını verir.


##### Karşılaştırma Operatörleri

- **Eşitlik (==):** İki değerin eşit olup olmadığını kontrol eder.

- **Eşit Değil (!=):** İki değerin eşit olup olmadığını kontrol eder.

- **Büyük (>):** Bir değerin diğerinden büyük olup olmadığını kontrol eder.

- **Küçük (<):** Bir değerin diğerinden küçük olup olmadığını kontrol eder.

- **Büyük Eşit (>=):** Bir değerin diğerinden büyük veya eşit olup olmadığını kontrol eder.

- **Küçük Eşit (<=):** Bir değerin diğerinden küçük veya eşit olup olmadığını kontrol eder.


##### Mantıksal Operatörler

- **Ve (and):** Her iki koşul da doğruysa True döndürür.

- **Veya (or):** Koşullardan en az biri doğruysa True döndürür.

- **Değil (not):** Bir koşulun tersini döndürür.


##### Atama Operatörleri

- **Eşit (=):** Değişkenlere değer atamak için kullanılır.

- **Topla ve Ata (+=):** Bir değişkenin değerine bir sayı ekler ve sonucu değişkene atar.

- **Çıkar ve Ata (-=):** Bir değişkenden bir sayı çıkarır ve sonucu değişkene atar.

- **Çarp ve Ata (*=):** Bir değişkenin değerini bir sayıyla çarpar ve sonucu değişkene atar.

- **Böl ve Ata (/=):** Bir değişkenin değerini bir sayıyla böler ve sonucu değişkene atar.

- **Modülüs ve Ata (%=):** Bir değişkenin değerini bir sayıya böler ve kalanı değişkene atar.


##### Kimlik Operatörleri

- **Eşitlik (is):** İki nesnenin aynı nesne olup olmadığını kontrol eder.

- **Eşit Değil (is not):** İki nesnenin aynı olmadığını kontrol eder.


##### Üyelik Operatörleri

- **İçerir (in):** Bir elemanın bir veri yapısında bulunup bulunmadığını kontrol eder.

- **İçermez (not in):** Bir elemanın bir veri yapısında bulunmadığını kontrol eder.   

 #### String Veri Tipleri / Indexing & Casting  
 **Indexing (Dizinleme)**  
Stringlerin her bir karakteri bir dizin numarasına sahiptir. Bu dizin numaraları sıfırdan başlar. İlk karakterin dizin numarası 0'dır.  
```python
name = "John"
print(name[0])  # J
print(name[1])  # o
print(name[2])  # h
print(name[3])  # n
```

**Casting (Dönüştürme)**  
Python'da stringleri diğer veri tiplerine dönüştürmek için fonksiyonlar kullanılır.   

int(): Bir stringi tamsayıya dönüştürür.
float(): Bir stringi ondalıklı sayıya dönüştürür.
str(): Başka bir veri tipini stringe dönüştürür.   
```python
# Stringi tamsayıya dönüştürme
num_str = "10"
num_int = int(num_str)  # 10

# Stringi ondalıklı sayıya dönüştürme
float_str = "3.14"
float_num = float(float_str)  # 3.14

# Tamsayıyı stringe dönüştürme
num = 10
num_str = str(num)  # "10"
```

 #### Input   
 **input() Fonksiyonu**  
Python'da "input()" fonksiyonu, kullanıcıdan veri almak için kullanılır.  
```python
name = input("Adınızı girin: ")
print("Merhaba, " + name + "!")
```

 #### Comment    
 Python'da yorumlar, kodun anlaşılması ve belgelendirilmesi için kullanılır. Yorumlar, "#" karakteri ile başlar ve satır sonuna kadar devam eder. Python yorumları yalnızca insanlar için açıklama amacıyla kullanılır ve programın işlevselliğini etkilemez.  
 
 #### String ve Sayısal  ifadelerde karşılaştırma 
 ```python
# Eşitlik (==)
x = 5
y = 5
result = x == y  # True

# Eşit Değil (!=)
a = 10
b = 20
result = a != b  # True

# Büyük (>)
m = 15
n = 10
result = m > n  # True

# Küçük (<)
p = 5
q = 8
result = p < q  # True

# Büyük Eşit (>=)
c = 15
d = 10
result = c >= d  # True

# Küçük Eşit (<=)
i = 5
j = 5
result = i <= j  # True

```
 ```python
# Eşitlik (==)
str1 = "hello"
str2 = "hello"
result = str1 == str2  # True

# Eşit Değil (!=)
str3 = "hello"
str4 = "world"
result = str3 != str4  # True

# Büyük (>)
str5 = "apple"
str6 = "banana"
result = str5 > str6  # False

# Küçük (<)
str7 = "apple"
str8 = "banana"
result = str7 < str8  # True

# Büyük Eşit (>=)
str9 = "apple"
str10 = "banana"
result = str9 >= str10  # False

# Küçük Eşit (<=)
str11 = "apple"
str12 = "banana"
result = str11 <= str12  # True

```
 
 #### İf-Else-Elif   
 Python'da "if", "else" ve "elif" ifadeleri, programın farklı koşullara göre farklı işlemler yapmasını sağlar. Bu yapılar, programların karar verme süreçlerini yönlendirir.

**if:** Belirli bir koşulun doğru olup olmadığını kontrol eder. Koşul doğruysa, if bloğu içindeki kod çalıştırılır.  

**else:** Bir "if" bloğundan önce gelir. "if" koşulu yanlışsa, else bloğu içindeki kod çalıştırılır.  

**elif:** "else if" kısaltmasıdır. Birden fazla koşulu kontrol etmek için kullanılır. İlk ifade yanlışsa ve elif ifadesi doğruysa, elif bloğu içindeki kod çalıştırılır.  

 ```python
# Kullanıcıdan bir sayı alın
num = int(input("Bir sayı girin: "))

# Sayının pozitif, negatif veya sıfır olduğunu kontrol edin
if num > 0:
    print("Girilen sayı pozitif")
elif num < 0:
    print("Girilen sayı negatif")
else:
    print("Girilen sayı sıfır")
 ```  
 
 #### Ternary Conditionals  
 
 📋Python'da ternary conditional ifadeleri, kısa ve tek satırda bir koşul kontrolü yapmak için kullanılan bir yapıdır. Bu yapı, "if" ve "else" ifadelerini tek satırda ifade etmek için kullanılır.  
 ```python
 [option1] if [condition] else [option2]
 ```
```python
user_score = 90

print("Next level") if user_score > 50 else print("Repeat level")
 ```

 #### Döngüler(Loops)  

**For döngüsü**  
bir dizi (örneğin liste, demet veya dize) üzerinde dolaşır ve her bir eleman için belirli bir işlemi tekrarlar.  
📌**Örnek:**

```python
# Bir liste üzerinde dolaşarak elemanları yazdırma
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

**While Döngüsü**  
While döngüsü, belirli bir koşul doğru olduğu sürece belirli bir bloğu tekrarlar.  

📌**Örnek:**

```python
# 1'den 5'e kadar olan sayıları yazdırma
num = 1
while num <= 5:
    print(num)
    num += 1
```

👉**continue:** Bu ifade, döngü içerisinde çalıştırıldığında, o anda bulunulan döngü adımını atlayarak döngünün bir sonraki adımına geçer. Yani, döngünün geri kalan kısmını çalıştırmadan döngüye başa döner.  
<br>
👉**break:** Bu ifade, döngü içerisinde çalıştırıldığında, döngüyü tamamen sonlandırır ve döngüden çıkar. Yani, döngü koşulu hala sağlanıyor olsa bile, break ifadesi çalıştığında döngü sona erer.    


#### List  
Birden çok veriyi guruplayıp bir arada tutmak istediğimizde bu yapıyı kullanırız. Farklı veri tiplerini bir List'te barındırabiliriz. String konusunda gördüğümüz Indexing ve Slicing mantığı burda da geçerli. 
  
📌**Örnek:**

```python
notes=[12,25,45,78,96,63]
notes[0]   #12
notes[0:5]   #[12, 25, 45, 78, 96]
notes[0:]   #[12, 25, 45, 78, 96, 63]

notes[0] +=10  #0 inexli elemana yani 12'ye 10 ekler
```
**len()** List'te kaç eleman olduğunu verir  
**append()** İçinde yazdığımız elemanı List'e ekler  
**extend()** İçinde yazılan birden çok elemanı List'in sonuna ekler  
**insert()** List'in sonuna değilde kendi belirlediğimiz indexe eleman eklemek istediğimizde kullanabiliriz  
**remove()** belli bir elemanı listeden silmek için kullanılır  
**pop()** belirli bir indexteki elemanı silmek için kullanılır, aynı zamanda o değeri bize döndürür  
**count()** içinde yazdığımız değerin listede kaç kez göründüğünü döndürür  
**Concatenation** '+' operatörü ile birden fazla listelerin elemanlarını tek bir listede gösterme işlemine denir  
**index()** belirli bir elemanın indexini verir  
**reverse** List'i tersine çevirir  
**sorted() & sort()** ikisi de List'teki değerleri default olarak küçükten büyüğe sıralar.  

#### Tuple  
Listeler gibi birden çok veriyi bir arada tutmamızı sağlar, tek farkları Tuple'lar immutable'dır(Değişmez).  
Tuple'larda elemanlar () içinde belirtilir.  

📌**Örnek:**

```python
# Bir tuple oluşturuyoruz
my_tuple = (1, 2, 3, 4, 5)

# Tuple'ın elemanlarına erişiyoruz
print("Tuple'ın ikinci elemanı:", my_tuple[1])

# Tuple'ın uzunluğunu alıyoruz
print("Tuple'ın uzunluğu:", len(my_tuple))
```
**in** List ve Tuple'larda belirli bir elemanın varlığını sorgulamak için kullanılır.  

#### Dictionary  
Anahtar-değer çiftlerinden oluşan, değiştirilebilir (mutable) ve sırasız bir veri yapısıdır. Her bir anahtar, bir değerle eşleştirilir. Anahtarlar genellikle metin veya sayısal veri türlerinden oluşabilirken, değerler herhangi bir veri tipi olabilir.

Süslü parantezler {} kullanılarak oluşturulur. Anahtar ve değer arasında : ile ayrılır.  
📌**Örnek:**  
```python
# Bir sözlük oluşturuyoruz
my_dict = {"anahtar1": "değer1", "anahtar2": 2, "anahtar3": [1, 2, 3]}

# Sözlükten bir değeri çağırıyoruz
print(my_dict["anahtar1"])  # Çıktı: değer1

# Sözlüğe yeni bir anahtar-değer çifti ekliyoruz
my_dict["anahtar4"] = True
```

#### Set  
👉 Bir set, benzersiz öğelerin koleksiyonunu tutar. Yani bir set içinde aynı öğeden birden fazla olamaz. Eğer aynı öğeyi birden fazla kez eklerseniz, set sadece bir kez ekler.  
👉 Setler, öğelerin sırasını korumazlar. Yani bir setin elemanlarına eklediğiniz sıra, setin içindeki sırayı belirlemez.  
👉 Setler, değiştirilebilir (mutable) veri tipleridir. Yani set içindeki öğeleri ekleyebilir, çıkarabilir veya güncelleyebilirsiniz.  
👉 Setlerde matematiksel küme işlemleri gerçekleştirebilirsiniz. Örneğin, iki setin birleşimini, kesişimini veya farkını alabilirsiniz.  
📌**Örnek:**  
```python
# Bir set oluşturuyoruz
my_set = {1, 2, 3, 4, 5}

# Set'e eleman ekliyoruz
my_set.add(6)

# Setten eleman çıkarıyoruz
my_set.remove(3)

# Seti yazdırıyoruz
print(my_set)  # Çıktı: {1, 2, 4, 5, 6}
```
📋 Birleşim (Union): İki veya daha fazla setin birleşimini almak, bu setlerde bulunan tüm benzersiz öğelerin toplamını içeren yeni bir set oluşturur. Bu işlem union() metodu veya | operatörü ile gerçekleştirilebilir.    
📌**Örnek:**  
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
# veya
# union_set = set1 | set2
print(union_set)  # Çıktı: {1, 2, 3, 4, 5}
```
📋 Kesişim (Intersection): İki veya daha fazla setin kesişimini almak, bu setlerde ortak olan tüm öğeleri içeren yeni bir set oluşturur. Bu işlem intersection() metodu veya & operatörü ile gerçekleştirilebilir.     
📌**Örnek:**  
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
# veya
# intersection_set = set1 & set2
print(intersection_set)  # Çıktı: {3}
```
📋 Fark (Difference): Bir setin diğer setten farkını almak, ilk sette bulunan ancak diğer sette bulunmayan öğeleri içeren yeni bir set oluşturur. Bu işlem difference() metodu veya - operatörü ile gerçekleştirilebilir.     
📌**Örnek:**  
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
# veya
# difference_set = set1 - set2
print(difference_set)  # Çıktı: {1, 2}
```

#### Non-Scallar For  
📋 Python'da döngülerle (genellikle for döngüsüyle) işlem yapılırken, her bir adımda bir skaler değer (örneğin, bir sayı veya bir karakter) yerine, bir dizi, liste veya başka bir veri yapısı gibi tek bir değer yerine birden fazla değeri işlediğiniz durumları ifade eder.    
📌**Örnek:**   
```python
# Var olan sayıların listesi
numbers = [1, 2, 3, 4, 5]

# Eklenecek sayı
addition = 10

# Sayıları güncelle
for i in range(len(numbers)):
    numbers[i] += addition

# Güncellenmiş sayıları yazdır
print("Güncellenmiş Sayılar:")
print(numbers)
```
#### Split & Join  
**split()** belirli bir bölme kriterine göre string'in alt parçalarını listenin elemanları olarak dönüştürebilir  
**join** listenin elemanları arasına belirlediğimiz yapıyı koyup stringe döndürür  

#### List Comprehension
📋 Python'da liste oluşturmanın kısa ve okunaklı bir yoludur. Bir listenin içinde döngü kullanarak yeni bir liste oluşturmayı sağlar. Genellikle bir dizi veya başka bir liste üzerinde döngü yaparak her bir eleman üzerinde belirli bir işlem yapmak için kullanılır.    
📌**Örnek:** 
```python
# Orjinal liste
numbers = [1, 2, 3, 4, 5]

# Her bir elemanın karesini alarak yeni bir liste oluştur
squared_numbers = [num * num for num in numbers]

# Oluşturulan liste
print(squared_numbers)
```
#### Variable Unpacking 
Bir demet veya liste içindeki elemanları tek bir adımda ayrıştırarak birden çok değişkene atama işlemidir.    
📌**Örnek:** 
```python
numbers = [1, 2, 3, 4, 5]

# İlk iki değeri a ve b değişkenlerine atayalım, kalan değerleri ise bir c'ye atayalım
a, b, *c = numbers

print("a:", a)  #1
print("b:", b)  #2
print("c:", c)  #3,4,5
```
#### Enumerate & Zip   
**enumerate()** bir dizi, liste veya başka bir iterable nesne alır ve her bir öğeyi ve onun dizindeki konumunu içeren bir tuple döndürür. Bu, bir döngü içinde hem öğe değerine hem de indeksine erişmek için kullanışlıdır.  
📌**Örnek:** 
```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

#çıktı:
0 apple
1 banana
2 cherry
```
**zip()** bir veya daha fazla iterable nesneyi alır ve bunları birleştirerek her birinin karşılıklı öğelerinden oluşan bir tuple oluşturur. Bu, birden fazla liste veya demet üzerinde aynı anda döngü yaparken kullanışlıdır  
📌**Örnek:** 
```python
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]
for name, age in zip(names, ages):
    print(name, age)

#çıktı
Alice 30
Bob 25
Charlie 35

```


### Fonksiyon-Giriş  
📋 Belirli bir işlemi gerçekleştirmek için bir araya getirilmiş kod bloklarıdır. Bir fonksiyon, belirli bir isim altında tanımlanır ve bu isimle çağrılır. Fonksiyonlar, kodunuzu modüler hale getirmenin ve tekrar kullanılabilir parçalar oluşturmanın temel bir yoludur    
" def fonksiyon_adı(input): " şeklinde tanımlanır.  
**Abstraksiyon** karmaşık bir sistem veya nesnenin önemli detaylarından arındırılması ve sadece temel işlevlerinin veya özelliklerinin odaklanılması anlamına gelir. Programlama bağlamında, abstraksiyon genellikle bir arayüz veya sınıf kullanarak bir nesnenin iç işleyişini gizlemek veya soyutlamak için kullanılır.  
#### Return  
Bir fonksiyon, işlemleri tamamladıktan sonra bir değer döndürebilir     
📌**Örnek:** 
```python
def toplama(a, b):
    return a + b

print(toplama(3, 5))  # Çıktı: 8
```
**Void Fonksiyonlar** herhangi bir değer döndürmeyen fonksiyonlardır  
**Fonksiyonlar-Yorum** """ Yorumlar üç tırkan içinde yazılır """.  "?" ise fonksiyonun bize ne yaptığını döndürür.
#### Multiple  
**Multiple** (çoklu), birden fazla öğeyi içeren veya birden fazla işlemi gerçekleştiren anlamına gelir. Programlama bağlamında, "multiple" genellikle birçok öğeyi veya işlemi ifade eder  
```python
x, y, z = 1, 2, 3
```
#### Predefiend/Parameters 
📋 "Predefined Parameters" veya "Default Parameters", bir fonksiyon tanımlanırken parametrelerin varsayılan değerlerle belirlenmesi anlamına gelir. Bu varsayılan değerler, fonksiyon çağrısı sırasında belirtilmezse otomatik olarak kullanılır.  
#### First Class Functions
📋 Fonksiyonların diğer veri türleriyle aynı şekilde kullanılabilmesini sağlar. Bu özellik, fonksiyonların değişkenlere atanabilmesini, fonksiyonların başka fonksiyonlara argüman olarak geçirilebilmesini, fonksiyonlardan dönüş değeri olarak kullanılabilmesini ve veri yapılarında saklanabilmesini sağlar.
#### Underscore-Placeholder  
Python'da, alt çizgi (_) genellikle bir "placeholder" (yer tutucu) olarak kullanılır. Yani, alt çizgi, belirli bir değeri veya döndürülen değeri göz ardı etmek veya kullanmamak için kullanılır.
```python
for _ in range(5):
    print("Merhaba")
```
Burada,range(5) fonksiyonu bir döngüyü beş kez tekrarlayacak ancak döngü içinde değişken kullanmamız gerekmediği için bu değişkenin adını _ olarak atadık  
#### Fstring
(format string), Python 3.6 ve sonraki sürümlerde kullanılabilen bir string formatlama yöntemidir. F-stringler, string içinde değişkenleri ve ifadeleri daha kolay bir şekilde yerleştirmenizi sağlar  
📌**Örnek:**
```python
name = "Ahmet"
age = 30
F-string kullanarak değişkenleri yerleştirme
message = f"Merhaba, benim adım {name} ve yaşım {age}."

print(message)
```
Bu örnekte, name ve age değişkenleri, F-string içinde süslü parantez içine yerleştirilmiştir. Program çalıştırıldığında, bu değişkenlerin değerleri doğrudan string içine yerleştirilerek ekrana yazdırılır.




### Veri Yapıları ve Algoritmalar  

📋 Algoritma, belirli bir problemi çözmek veya bir görevi yerine getirmek için tasarlanmış, sonlu sayıda adımlardan oluşan talimatlar dizisidir. Her adım, kesin ve açık bir şekilde tanımlanmış işlemler içerir ve bu adımların sırası takip edildiğinde, başlangıç verilerinden istenilen sonuca ulaşılır. Algoritmalar, bilgisayar bilimlerinde ve günlük yaşamda geniş bir uygulama alanına sahiptir.   

#### Sayı Sistemleri

Bu proje, çeşitli sayı sistemleri hakkında temel bilgileri ve bunlar arasındaki dönüşüm işlemlerini içermektedir.  

###### 1. Onlu Sayı Sistemi (Decimal)
- **Taban:** 10
- **Rakamlar:** 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
- **Kullanım:** Günlük yaşamda en yaygın kullanılan sistemdir.
- **Örnek:** 345 (Bu, 3*10^2 + 4*10^1 + 5*10^0 olarak ifade edilir)

###### 2. İkili Sayı Sistemi (Binary)
- **Taban:** 2
- **Rakamlar:** 0, 1
- **Kullanım:** Bilgisayarlar ve dijital elektroniklerde temel sistemdir.
- **Örnek:** 1011 (Bu, 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 olarak ifade edilir)

###### 3. Sekizli Sayı Sistemi (Octal)
- **Taban:** 8
- **Rakamlar:** 0, 1, 2, 3, 4, 5, 6, 7
- **Kullanım:** Bilgisayar bilimlerinde, özellikle daha eski sistemlerde yaygın olarak kullanılır.
- **Örnek:** 345 (Bu, 3*8^2 + 4*8^1 + 5*8^0 olarak ifade edilir)

###### 4. Onaltılı Sayı Sistemi (Hexadecimal)
- **Taban:** 16
- **Rakamlar:** 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F (A = 10, B = 11, ... , F = 15)
- **Kullanım:** Bilgisayar bilimlerinde, özellikle bellek adresleme ve renk kodlamada kullanılır.
- **Örnek:** 1A3 (Bu, 1*16^2 + 10*16^1 + 3*16^0 olarak ifade edilir)

###### 5. Üçlü Sayı Sistemi (Ternary)
- **Taban:** 3
- **Rakamlar:** 0, 1, 2
- **Kullanım:** Daha az yaygın olmakla birlikte, bazı teorik ve pratik uygulamalarda kullanılır.
- **Örnek:** 102 (Bu, 1*3^2 + 0*3^1 + 2*3^0 olarak ifade edilir)

**Dönüşüm İşlemleri**

Sayılar bir sistemden diğerine dönüştürülebilir. İşte birkaç dönüşüm örneği:

**Onlu'dan İkili'ye Dönüşüm:** Sayıyı 2 tabanına bölerek ve kalanları yazarak yapılır.
  - Örnek: 13 (decimal) → 1101 (binary)
    - 13 ÷ 2 = 6 kalan 1
    - 6 ÷ 2 = 3 kalan 0
    - 3 ÷ 2 = 1 kalan 1
    - 1 ÷ 2 = 0 kalan 1 (sondan başa doğru yazılır: 1101)

**Onlu'dan Onaltılı'ya Dönüşüm:** Sayıyı 16 tabanına bölerek ve kalanları yazarak yapılır.
  - Örnek: 255 (decimal) → FF (hexadecimal)
    - 255 ÷ 16 = 15 kalan 15 (15 = F)
    - 15 ÷ 16 = 0 kalan 15 (15 = F) (sondan başa doğru yazılır: FF)

##### Kullanım Alanları
- **Bilgisayar Bilimleri:** İkili, sekizli ve onaltılı sistemler, bellek adresleme, veri temsil etme ve çeşitli algoritmalarda kullanılır.
- **Elektronik:** İkili sistem, dijital devrelerde ve mikroişlemcilerde kullanılır.
- **Matematik ve Teorik Bilgisayar Bilimleri:** Çeşitli sayı sistemleri, sayı teorisi ve algoritmaların analizinde kullanılır.
<br>

**Array:** Sabit boyutlu ve aynı türden elemanlar içeren bir veri yapısıdır.
  
  - Elemanlara indeksleri aracılığıyla doğrudan erişim sağlar.
  - Bellekte ardışık konumlarda saklanır.
  - **Hızlı Erişim:** İndeksleme sayesinde herhangi bir elemana O(1) zaman karmaşıklığı ile erişilebilir.
  - **Basitlik:** Yapısı basittir ve kullanımı kolaydır.
 
<br>    

**Linked List**  

Düğümlerin (nodes) birbirine bağlandığı dinamik bir veri yapısıdır. Her düğüm, bir veri öğesi ve bir sonraki düğümün adresini içerir.

- Singly Linked List: Her düğüm sadece sonraki düğüme işaret eder.
- Doubly Linked List: Her düğüm hem önceki hem de sonraki düğüme işaret eder.
- Circular Linked List: Son düğüm, ilk düğüme işaret eder.

- Dinamik Boyut: Bağlı listenin boyutu dinamik olarak değiştirilebilir.
- Kolay Eleman Ekleme ve Çıkarma: Listeye eleman eklemek veya çıkarmak, sadece ilgili düğümlerin bağlantılarını değiştirmeyi gerektirir (O(1) zaman karmaşıklığı).
<br>

**Stack**   

Veri yapılarından biridir ve verilerin yalnızca üstünden (top) erişilip eklenebildiği veya çıkarılabildiği bir koleksiyondur.  
**Çalışma Prensibi:** LIFO (Last In, First Out) - Son giren, ilk çıkar.

- **Push:** Yeni bir öğe yığının tepesine eklenir.
- **Pop:** Yığının tepesindeki öğe çıkarılır.
- **Peek/Top:** Yığının tepesindeki öğeyi çıkarılmadan görüntüler.
- **IsEmpty:** Yığının boş olup olmadığını kontrol eder.
<br>

**Queue**  

Elemanların eklendiği bir veri yapısıdır ve ilk eklenen elemanın ilk çıkarıldığı (FIFO - First In, First Out) prensibi ile çalışır.
- **Çalışma Prensibi:** FIFO (First In, First Out) - İlk giren, ilk çıkar.

- **Enqueue:** Yeni bir öğe kuyruğun sonuna eklenir.
- **Dequeue:** Kuyruğun başındaki öğe çıkarılır.
- **Front/Peek:** Kuyruğun başındaki öğeyi çıkarılmadan görüntüler.
- **IsEmpty:** Kuyruğun boş olup olmadığını kontrol eder
<br>

**Hash Table**  

Anahtar-değer çiftlerini depolayan bir veri yapısıdır. Verileri hızlı bir şekilde eklemek, erişmek ve silmek için hash fonksiyonları kullanır.
**Çalışma Prensibi:** Hash fonksiyonu, verilen anahtarı bir dizin değeriyle eşleştirir ve bu dizin, tablodaki veri konumunu belirler.

- **Anahtar-Değer Çiftleri:** Her veri, bir anahtar ve bu anahtara karşılık gelen bir değerden oluşur.
- **Hash Fonksiyonu:** Anahtarı alır ve bunu tablo içinde bir indekse dönüştürür.
- **Çakışma Yönetimi:** İki anahtar aynı indekse hash edilirse (çakışma), bunu çözmek için çeşitli teknikler kullanılır (zincirleme, açık adresleme vb.).

#### Algoritma Türleri

##### 1. Arama Algoritmaları
- **Linear Search (Doğrusal Arama):** Verilen bir dizide, belirli bir elemanı bulmak için sırayla her elemanı kontrol eder.
- **Binary Search (İkili Arama):** Sıralanmış bir dizide, ortadaki elemanı kontrol ederek aramayı yarıya indirir. O(log n) zaman karmaşıklığına sahiptir.

##### 2. Sıralama Algoritmaları
- **Bubble Sort (Kabarcık Sıralaması):** Elemanları ardışık çiftler halinde karşılaştırır ve gerektiğinde yer değiştirir.
- **Merge Sort (Birleştirme Sıralaması):** Diziyi ikiye böler, her iki yarıyı da ayrı ayrı sıralar ve ardından birleştirir. O(n log n) zaman karmaşıklığına sahiptir.
- **Quick Sort (Hızlı Sıralama):** Bir pivot seçer ve diziyi bu pivot etrafında yeniden düzenler. Ortalama O(n log n) zaman karmaşıklığına sahiptir.

##### 3. Grafik Algoritmaları
- **Dijkstra'nın Algoritması:** Ağırlıklı bir grafikte, bir başlangıç düğümünden diğer tüm düğümlere olan en kısa yolları bulur.
- **Kruskal'ın Algoritması:** Minimum maliyetli bir ağacın (minimum spanning tree) bulunması için kullanılır.

##### 4. Dinamik Programlama
- **Fibonacci Serisi:** Önceki iki elemanın toplamına dayalı olarak Fibonacci sayısını hesaplar.
- **Knapsack Problemi:** Belirli bir ağırlık kapasitesiyle, maksimum değeri elde etmek için nesnelerin seçilmesi problemi.

#### Algoritma Analizi

Bir algoritmanın verimliliğini ve performansını değerlendirmek için kullanılan yöntem ve tekniklerin bütünüdür. Bu analiz, algoritmanın çalışma süresi ve bellek kullanımı gibi kaynak tüketimini inceler.
**Amaç;**  
- Algoritmanın ne kadar hızlı çalıştığını ve ne kadar bellek kullandığını anlamak.
- Farklı algoritmaların aynı problemi çözmedeki performanslarını karşılaştırmak.
- Algoritmanın büyük veri kümelerinde nasıl davranacağını tahmin etmek.

##### Zaman Karmaşıklığı (Time Complexity)
Algoritmanın çalışma süresinin, girdi boyutuna bağlı olarak nasıl değiştiğini gösterir.
- **Big O Notasyonu:** En kötü durum senaryosunda algoritmanın performansını ifade eder.
  - **O(1):** Sabit zaman
  - **O(n):** Doğrusal zaman
  - **O(log n):** Logaritmik zaman
  - **O(n^2):** Karesel zaman

##### Uzay Karmaşıklığı (Space Complexity)
Algoritmanın bellek kullanımı, girdi boyutuna bağlı olarak nasıl değiştiğini gösterir.
- **Big O Notasyonu:** En kötü durum senaryosunda algoritmanın bellek kullanımı.

#### Algoritma Analizinde En Kötü, Ortalama ve En İyi Durum

- **En Kötü Durum (Worst Case):** Algoritmanın en yavaş çalıştığı senaryo. Bu, genellikle algoritmanın performansının garanti edilmesi gereken durumlar için önemlidir.
- **Ortalama Durum (Average Case):** Algoritmanın tipik bir girdi kümesi üzerindeki performansı. Bu, genellikle günlük kullanımda algoritmanın beklenen davranışını temsil eder.
- **En İyi Durum (Best Case):** Algoritmanın en hızlı çalıştığı senaryo. Bu, algoritmanın ideal şartlar altında nasıl performans gösterdiğini gösterir.  

##### Doğrusal Arama (Linear Search)
- **Açıklama:** Bir dizide belirli bir elemanı bulmak için sırayla her elemanı kontrol eder.
- **En Kötü Durum:** O(n) - Aranan eleman dizinin sonunda veya dizide yoksa.
- **Ortalama Durum:** O(n/2) veya O(n) - Aranan eleman dizinin ortalarında bir yerdeyse (ortalama olarak).
- **En İyi Durum:** O(1) - Aranan eleman dizinin başındaysa.


### Temel Bilgisayar Ağları

Bu belge, temel bilgisayar ağları hakkında bilgi içermektedir. Bilgisayar ağları, cihazların birbiriyle iletişim kurmasını ve veri paylaşmasını sağlayan sistemlerdir. Bu belgede ağ türleri, topolojileri, bileşenleri, protokoller ve güvenlik hakkında temel bilgiler bulabilirsiniz.

#### Ağ Türleri
- **LAN (Local Area Network - Yerel Alan Ağı):** Küçük bir coğrafi alanı kapsayan ağlardır, genellikle bir bina veya kampüs içindeki cihazları birbirine bağlar. Ethernet ve Wi-Fi, yaygın kullanılan teknolojilerdir.
- **WAN (Wide Area Network - Geniş Alan Ağı):** Geniş coğrafi alanları kapsayan ağlardır. İnternet, en büyük WAN örneğidir.
- **MAN (Metropolitan Area Network - Metropol Alan Ağı):** Bir şehir veya büyük bir kampüs gibi daha geniş bir alanı kapsayan ağlardır.
- **PAN (Personal Area Network - Kişisel Alan Ağı):** Çok küçük bir alanı, genellikle bir kişinin cihazları arasında veri alışverişini kapsayan ağlardır. Bluetooth ve USB, yaygın teknolojilerdir.

#### Ağ Topolojileri
- **Yıldız (Star) Topolojisi:** Tüm cihazlar merkezi bir cihaza (örneğin, bir switch veya hub) bağlıdır. Kolay yönetilebilir ve sorun tespiti kolaydır.
- **Halka (Ring) Topolojisi:** Cihazlar halka şeklinde birbirine bağlanır. Veriler belirli bir yönde dolaşır. Ancak, bir bağlantı kesilirse tüm ağ etkilenir.
- **Veri Yolu (Bus) Topolojisi:** Tüm cihazlar tek bir veri yolu üzerinden bağlanır. Kurulumu kolaydır ancak veri yolu arızalanırsa tüm ağ çalışmaz.
- **Ağaç (Tree) Topolojisi:** Yıldız topolojisinin bir uzantısıdır, merkezi düğümlerden dallanarak alt ağlar oluşturur.
- **Ağ (Mesh) Topolojisi:** Her cihaz diğer cihazlara doğrudan bağlanır. Yüksek güvenilirlik sağlar, ancak karmaşıktır ve maliyetlidir.

#### Ağ Bileşenleri
- **Yönlendirici (Router):** Ağlar arasında veri paketlerini yönlendirir. İnternet bağlantısı sağlayıcılarının kullandığı ana cihazlardır.
- **Anahtar (Switch):** Yerel ağlarda cihazları birbirine bağlar. Verimli ve güvenilir veri iletimi sağlar.
- **Hub:** Çoklu cihazları birbirine bağlar, ancak veri paketlerini herkese iletir, bu da daha az verimli olur.
- **Erişim Noktası (Access Point):** Kablosuz cihazların bir kablolu ağa bağlanmasını sağlar.

#### Ağ Protokolleri
- **TCP/IP (Transmission Control Protocol/Internet Protocol):** İnternetin temel protokolüdür, veri paketlerinin nasıl iletileceğini ve adresleneceğini belirler.
- **HTTP/HTTPS (HyperText Transfer Protocol/Secure):** Web sayfalarını görüntülemek için kullanılır. HTTPS, güvenli veri iletimi sağlar.
- **FTP (File Transfer Protocol):** Dosya transferi için kullanılır.
- **SMTP (Simple Mail Transfer Protocol):** E-posta gönderimi için kullanılır.
- **DNS (Domain Name System):** Alan adlarını IP adreslerine dönüştürür.

#### Ağ Güvenliği
- **Firewall (Güvenlik Duvarı):** İzin verilen ve yasaklanan trafik kurallarını belirler, yetkisiz erişimi engeller.
- **VPN (Virtual Private Network):** İnternet üzerinden güvenli ve şifreli bağlantı sağlar.
- **Antivirüs ve Antimalware Yazılımları:** Zararlı yazılımlara karşı koruma sağlar.
- **Şifreleme (Encryption):** Verilerin okunabilir olmaktan çıkarılarak gizliliğinin korunmasını sağlar.

Bilgisayar ağları, modern bilgi teknolojisinin bel kemiğidir ve her türlü veri iletişimi ve paylaşımında kritik bir rol oynar. Ağ türleri ve bileşenleri hakkında temel bilgi sahibi olmak, ağların nasıl çalıştığını ve nasıl güvenli hale getirileceğini anlamak için önemlidir.



 ### 🤩 Clean Code  
 Temiz kodun önemi, yazılım geliştirmenin sadece kodu yazmak olmadığı gerçeğinden kaynaklanır. Kodun yazılmasından sonra, onu okuma, anlama, değiştirme ve bakımını yapma işlemi başlar  
 <br>
 Clean Code yazarken dikat etmemiz gereken kavramlar;  
 
 1) **Değişken İsimlendirme**
    
    📋 İyi bir değişken ismi, kodun okunabilirliğini artırır ve hataların oluşmasını azaltır.  
    Değişkenleri isimlendirirken olabildiğince kısa anlamlı ve ingilizce kelimeler seçmeye özen gösterin.  
    
       📌**Örnek**  
     Kötü örnek: kmn (anlaşılması zor)  
     İyi örnek: kilometerNumber (anlamlı ve okunabilir)

    📋Boolean Değerler İçin Anlamlı İsimler Kullanın: Boolean değerleri temsil eden değişkenler genellikle bir durumu ifade eder. Bu tür değişkenler için is, has, can gibi ön ekler 
    kullanmak kodun anlaşılırlığını artırır.
    
    📌**Örnek2**
     
    Kötü örnek: durum (ne tür bir durum olduğu belirsiz)  
    İyi örnek: isActive (bu isim, durumun ne olduğunu belirtir)

2) **Statik, Dinamik ve Generic Kavramları**    
    📋 Statik, dinamik ve generic kavramları, temiz kod yazmanın önemli bir parçasıdır. Bu kavramları anlamak ve doğru durumda kullanmak, kodunuzun kalitesini ve bakımını büyük ölçüde artırabilir.  
    📋 Generic programlama da, doğru durumda kullanıldığında kodu daha güvenli ve yeniden kullanılabilir hale getirebilir  
    📋 Statik ve dinamik tipli dillerin her birinin kendine özgü avantajları ve dezavantajları vardır. Kod yazdıkça kullanım alanlarını daha iyi kavrayacaksınız.

     

3) **DRY Prensibi/ Don't Repeat Yourself (Kendini Tekrarlama)**   
   📋 Yazılım geliştirme sürecinde tekrarlanan kodları en aza indirmeyi ve kod tekrarını önlemeyi amaçlar. Her bilginin tek ve kesin bir temsili olmalıdır sözüne ithafen yapılan bir prensiptir.

4) **Tek Sorumluluk İlkesi/ Single-Responsibility Principle**   
   📋 SOLID prensiplerinin ilkini oluşturan bir yazılım geliştirme prensibidir
       
   📋 Temel amacı, yazılım bileşenlerini daha anlaşılır, daha bakımı kolay ve daha esnek hale getirmektir. Bir bileşenin tek bir sorumluluğa sahip olması, o bileşenin diğer bileşenlerle daha az bağımlı olmasını sağlar ve bu da kodun daha modüler ve yeniden kullanılabilir olmasını sağlar

   
## Bulut Bilişim
Bilgileri bir bilgisayarın sabit disk sürücüsü yerine İnternet üzerinde depolar ve işler  
- Çok daha yüksek miktarda bilgiyi çok daha hızlı bir biçimde depolayabilir ve işleyebilir  
- Sonuçları yalnızca tek bir telefona, tablete, bilgisayara ya da bir dizi yerel terminale değil, İnternet'e bağlanabilen herhangi bir aygıta aktarabilir
**3 Farklı bulut hizmeti vardır**
  - Genel Bulut
     Küçük işletmelerin ve bireysel kullanıcıların İnternet üzerinden çok yüksek bilgi işlem gücüne erişebilecekleri klasik bulut bilişim modelidir
  - Hibrit Bulut
    Genel ve özel kaynakları birleştirir. Verilerin bir kısmı özel bulutta ve bir kısmı da genel bulutta bulunur ve bunlar farklı bulut kullanım düzeyleri sunan birden çok satıcı firma tarafından sağlanır.
  - Özel Bulut
     Tek bir kuruluşun bilgilerini korur  
   
**Bulut bilişimin en popüler üç hizmet modelini**  
Hizmet olarak sunulan yazılım **(SaaS)**, hizmet olarak sunulan platform **(PaaS)** hizmet olarak sunulan altyapı **(IaaS)**  

![bulutB](https://github.com/Fatmaaktar/Kodluyoruz-IBM-CyberStart/assets/106100226/f62a0cee-5cbc-4e9b-afae-33e0f2c4cde9)   

📌 **SaaS** ifadesini duyduğunuzda, e-posta veya çevrimiçi alışveriş gibi kullanım biçimlerini düşünün.  
📌 **PaaS**'yi duyduğunuzda, konteynerleri, veritabanlarını, çalıştırma zamanını ve entegrasyonu düşünün.  
📌 **IaaS**'yi duyduğunuzda, bilişim, depolama ve ağ kaynaklarını düşünün.  

**Kubernetes** konteynerli iş yüklerinin ve hizmetlerin yönetilmesi için açık kaynaklı bir platformdur  

![23](https://github.com/Fatmaaktar/Kodluyoruz-IBM-CyberStart/assets/106100226/002acc9c-01c4-476c-abac-aaf6e2eed869)  

 📋 Teknik inovasyonlar, buluta bağımlıdır ve bu da bulutu yapay zekaya, blockchain'e, Nesnelerin İnterneti'ne ve hatta kuantum bilişime açılan kapı haline getirir  
 

## Yapay Zeka
Yapay zeka veya AI, makineleri akıllı hale getirme bilimidir. 
**Zayıf Yapay Zeka**  
Çoğu şirket, işleri daha hızlı ve daha düşük maliyetle otomatik hale getirmek ve sonuç almak için zayıf yapay zekayı kullanır.  
 Müşteri hizmetleri sorularını yanıtlayan bir sohbet robotunu, Facebook'taki yüz tanıma özelliğini, Amazon'daki satın alma önerilerini veya sesi metne dönüştürebilen uygulamaları düşünün. Alexa, Google Assistant ve Siri, zayıf yapay zekaya örnektir.  
 **Artırılmış zeka**   
 İnsan zekasına yönelik tamamlayıcı bir rol üstlenerek, insanların daha iyi karar almalarına yardımcı olur.   
 Örneğin IBM Watson for Oncology, sağlık uzmanlarının bir kanser hastasının tıbbi kayıtlarındaki önemli bilgileri belirlemelerine yardımcı olur ve çeşitli olası tedavileri, her birinin ne kadar işe yarayacağına dair tahminlerle birlikte önerir.    
 **Genel Yapay Zeka**   
 Henüz icat edilmedi. Bugün, genel yapay zeka pratik bir teknolojiden ziyade bir hedef. Buna ulaşmak için, on yıllar sürecek ek araştırma ve daha güçlü bilgisayarlar gerekecek.   
 
![24](https://github.com/Fatmaaktar/Kodluyoruz-IBM-CyberStart/assets/106100226/b84b0d3a-56b0-4267-9435-720f73229693)   

**Sinir ağları**  
Makine öğrenimi modellerinden oluşan gruplardır. İnsan beyninin yoğun bir şekilde birbirine bağlı olan hücrelerini simüle ederler. Nesneleri öğrenebilir, örüntüleri tanıyabilir ve açık bir şekilde programlanmalarına gerek olmadan karar verebilirler.  
**Gözetim altında öğrenim**  
Makineye bir insan tarafından etiketlenmiş oldukça doğru bir veri seti sunan bir makine öğrenimi modelidir.  
**Gözetimsiz öğrenim**  
Yapay zekaya herhangi bir etiketlenmiş veri sunmayan bir makine öğrenimi modelidir. Bu, verilerin insanların bu veri örüntülerini kendi başlarına tanımlayamayacağı kadar büyük veya karmaşık olduğu durumlarda değerlidir.  
**Görsel tanıma**   
 Bilgisayarları fotoğraf ve videoları anlayıp yorumlamaları için eğitmeye odaklanan bir yapay zeka alt alanıdır.  
 
## Siber Güvenlik
Siber güvenlik, sanal dünyada suçun ve zararın azaltılmasına yardımcı oluyor. Bunu bilgisayar sistemlerinin ve verilerin gizliliğinin, bütünlüğünün ve kullanılabilirliğinin tehditlere karşı korunmasına yönelik bir dizi yöntem olarak düşünün.  

**Siber Güvenlik ile ilgili terimler**   

**APT**   Çok sayıda aşamadan oluşan ve uzun süreli bir ağ saldırısıdır ve bu saldırı türünde, yetkisiz kullanıcılar değerli kurumsal verilere erişir ve bunları toplar.  
**Botnet** Potansiyel olarak dünyanın herhangi bir yerinde bulunan, bir kötü amaçlı yazılım parçasının bulaşmış olduğu bir grup bilgisayar sistemidir.   
**Kaba Kuvvet Saldırısı** Bir bilgisayar korsanının, örneğin parolasını "tahmin etmeye" çalışarak bir bilgisayar sistemine yetkisiz olarak erişmek için kullanabileceği bir yöntemdir.  
**Komuta ve Kontrol Merkezi** Bir botnetteki tüm botları kontrol eden bir uygulamadır. Bir bilgisayar korsanı, bir uygulama aracılığıyla bir komut gönderir ve bu uygulama daha sonra komutu bir ağ üzerindeki tüm ele geçirilmiş bilgisayarlara aktarır.  
**Dijital İmza** Bir özel anahtar ile şifrelenmiş ve mesajın ya da nesnenin orijinalliğinin ve bütünlüğünün alıcıya garanti edilmesi için bir mesaja ya da nesneye eklenmiş olan bilgilerdir.  
**İstismar** Bir bilgisayarın güvenlik açığından yararlanmak amacıyla kullanılabilecek kötü amaçlı bir uygulama veya komut dosyasıdır.  
**Güvenlik Duvarı**  Yetkisiz erişimin engellenmesine odaklanan donanım veya yazılım tabanlı bir savunma teknolojisidir. 
**Bal Çanağı (honeypot)** Savunma amaçlı bir siber güvenlik yöntemidir. Bu yöntem, bir ağ üzerinde yasal ve yüksek değerli bir hedef gibi görünecek şekilde tasarlanmış bir bilgisayarın (sunucu) kullanılmasını kapsar.  
**Jailbreak** Bir aygıt üzerindeki yazılım kısıtlamaları atlanarak bir kullanıcının bir işletim sistemine ya da çekirdeğe kök erişimi elde etmesidir. Bu yöntem, genellikle cep telefonu güvenliği bağlamında kullanılır.  
**Ortadaki Adam (MitM)**  Bir saldırganın, işlemleri gözlemek ve kaydetmek amacıyla bir kullanıcı ile web sitesi arasındaki mesajları yakaladığı izinsiz giriş yöntemidir. MitM saldırıları, kimlik avı 
dolandırıcılığı ile site trafiğini yönlendirme saldırılarının gelişmiş türevleridir.   
**Yama** Bir "düzeltme" olarak yayınlanan yeni bir yazılım parçasıdır. Çoğu yazılımın oluşturulması binlerce satırlık programlama dili gerektirir, bu nedenle bir geliştiricinin tüm güvenlik açıklarının kapatıldığından emin olması zordur.   
**Fidye Yazılımı**  Bir bilgisayardaki dosyalara erişimi kasıtlı olarak engelleyen bir tür kötü amaçlı yazılımdır. Bir bilgisayara bu amaçla tasarlanmış bir kötü amaçlı yazılım bulaşırsa, yazılım tipik olarak dosyaları şifreler ve şifrelerinin çözülmesi için bir "fidye" ödenmesini talep eder.  
**Truva Atı** Genellikle bir bilgisayar korsanının bir bilgisayara uzaktan erişim elde etmesine olanak sağlayan bir kötü amaçlı yazılım parçasıdır. Truva Atı bulaşmış olan bir sistem, bir suçlunun dosyaları karşıdan yüklemesi ya da kullanıcının tuş vuruşlarını izlemesi için bir giriş noktası yaratır.  
**Sanal Özel Ağ (VPN)** Bir kullanıcının İnternet'i kullanırken anonim olarak kalmasına imkan tanıyan bir araçtır. Bir VPN, lokasyonu gizleyerek ve kullanıcının bilgisayarı ile ziyaret ettiği web sitesi arasında aktarıldığı sırada trafiği şifreleyerek anonimlik sağlar.  
**Su Kaynağı (Saldırısı)** Belirli bir hedef kitlenin sıklıkla ziyaret ettiği bir web sitesine kötü amaçlı kod yerleştirerek belirli bir ilgi alanına sahip olan bir grubu hedefleyen bir saldırıdır.   
**Beyaz Şapkalı Bilgisayar Korsanı** Bilgisayar korsanlığı yeteneklerini etik bir amaçla kullanan bir kişidir. Buna karşı, "siyah şapkalı" bilgisayar korsanı ise tipik olarak kötü amaçlıdır.  
**Solucan** Diğer bağlı bilgisayarlara bulaşmak için kendini çoğaltabilen bir kötü amaçlı yazılım parçasıdır. Kötü amaçlı yazılımlar, istismar etmek ve yayılmak için bir ağdaki zayıf sistemleri aktif olarak avlar.  
**Sıfır Gün (Saldırısı)** Belirli bir tür yazılım istismarıdır, genellikle kötü amaçlı yazılımdır. Sıfır gün istismarını özgün kılan özellik, halk ya da yazılım satıcı firması tarafından bilinmemesidir. Bir başka deyişle, güvenlik açığından haberdar olan az sayıda insan olduğundan, kendilerini bunun kullanımından korumak için "sıfır günleri" bulunur.  


## Veri Bilimi   
Veri bilimcisi, verilerden içgörüler çıkarır. Tahmine dayalı analitik, veri madenciliği, metin madenciliği, örüntü tanıma, veri modelleme, makine öğrenimi ve istatistik yöntemlerini kullanarak, geniş veri setlerinde saklı anlamı ortaya çıkarır
Verileri iki farklı şekilde organize edebilirsiniz, yapılandırılmış veri veya yapılandırılmamış veri.   
**Yapılandırılmış veriler**  sütunlar ve satırlar şeklinde ortaya konulabilen bilgilerdir. Microsoft Excel gibi bir hesap tablosu kullanarak yapılandırılmış verilerle çalışmış olabilirsiniz. Karmaşık bilgiler için, veri bilimcileri SQL, Apache veya R gibi, bağlı birçok tabloda bulunan devasa miktarda veriyi sıralayabilen daha güçlü araçlar kullanırlar.  
**yapılandırılmamış veriler** bir diğer deyişle "geri kalan her şey" var. Verilere ilişkin yerleşik bir organizasyon (veya yapı) olmadığında bu terimi kullanırız. Yapılandırılmamış veriler; ses dosyaları, sosyal medya paylaşımları, makale metinleri, hatta şarkı sözlerinden oluşan bir koleksiyon olabilir.    
## Blockchain nedir?  
Blockchain, eşler arası bir ağda gerçekleşen zincir işlemler ve alışverişlerdeki veri bloklarını kaydeden bir dağıtık defter teknolojisi uygulamasıdır.  

1) Blockchain, bilgileri kişisel bilgisayarlardan oluşan bir ağda depolayarak, bilgi depolamasını merkezilikten uzaklaştırır ve dağınık hale getirir.   
2) Bu da herhangi birinin ağı ele geçirmesini veya ağa müdahale edip bozmasını zorlaştırır.  
3) Blockchain, kayıtların kurcalanmasını engellemek için kriptografiyi kullanır.
4) Blockchain dağıtık defteri, işlem bilgilerini tipik bir defterden farklı biçimde saklar ve bu defter müdahaleye açık değildir!

Kriptografik hash fonksiyonları  
Zincire bir blok eklendiğinde, rastgele harfler ve rakamların bir araya gelerek oluşturduğu, hash adında bir kriptografik mühürle mühürlenir.

Peki Blockchain nasıl çalışır?

1) Gerçekleşen her işlem bir blok içine yerleştirilir
2) Her blok önündeki ve arkasındaki bloğa bağlıdır
3) İşlemler bir araya gelerek blokları oluşturur ve blockchain (blok zinciri) adı verilen değiştirilemeyen bir zincir yaratılmış olur
   
**Not** Blockchain, dağıtık defter teknolojisini kullanarak değerin veya dijital varlıkların A noktasından B noktasına hareketini izler. Bu da blockchain defterlerinin, yazılımını çalıştıran tüm bilgisayarlara dağıtılmış olduğu anlamına gelir.  

**Not** Blockchain ve veritabanı arasındaki temel fark yetki dağıtımıdır (decentralization). Blockchain'de kayıtlar tek bir merkezi noktada tutulmaz; eşzamanlı olarak bilgisayarlarda paylaşılır. Blockchain'deki her katılımcı tüm kayıtların ve değişikliklerin güvenli bir kopyasına sahip olduğundan verilerin denetim geçmişini herkes görüntüleyebilir. İşlemlerin denetlenmesi ve her şeyin doğruluğunun onaylanması için güvenilir ve merkezi bir üçüncü kişiye gerek yoktur.  
Güveni ve gücü ağdaki tüm katılımcılara dağıtır, yani herkes bunun bir parçası olabilir. Bitcoin bugün üretilen en büyük genel blockchain ağlarından biridir.  

**Hyperledger** işlemlerin dünya çapında gerçekleştirilme biçimini dönüştürebilen dağıtık defterler için sektörler genelinde bir açık standardın önemli özelliklerini belirleyerek ve bunları ele alarak blockchain teknolojisini geliştirmeyi amaçlayan bir Linux Foundation açık kaynak projesidir.  

  




