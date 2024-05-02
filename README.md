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
#### Fonksiyon-Giriş  
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

# F-string kullanarak değişkenleri yerleştirme
message = f"Merhaba, benim adım {name} ve yaşım {age}."

print(message)
```
Bu örnekte, name ve age değişkenleri, F-string içinde süslü parantez içine yerleştirilmiştir. Program çalıştırıldığında, bu değişkenlerin değerleri doğrudan string içine yerleştirilerek ekrana yazdırılır.


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
    📋Statik, dinamik ve generic kavramları, temiz kod yazmanın önemli bir parçasıdır. Bu kavramları anlamak ve doğru durumda kullanmak, kodunuzun kalitesini ve bakımını büyük ölçüde artırabilir.  
    📋Generic programlama da, doğru durumda kullanıldığında kodu daha güvenli ve yeniden kullanılabilir hale getirebilir  
    📋Statik ve dinamik tipli dillerin her birinin kendine özgü avantajları ve dezavantajları vardır. Kod yazdıkça kullanım alanlarını daha iyi kavrayacaksınız.

     

   





 
