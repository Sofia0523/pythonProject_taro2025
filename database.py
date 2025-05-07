import sqlite3

# connect = sqlite3.connect('database.db')
# connect.execute("""CREATE TABLE cards(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 image TEXT NOT NULL,
#                 title TEXT NOT NULL,
#                 desc_love TEXT,
#                 desc_future TEXT,
#                 desc_finances TEXT )""")
#
# # connect.execute("""DROP TABLE cards""")
# connect.commit()
# connect.close()

def add_cards(image, title, desc_love, desc_future, desc_finances):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(''' INSERT INTO cards(image, title, desc_love,desc_future,desc_finances)
                     VALUES(?, ?, ?, ?, ?)''', (image, title, desc_love, desc_future, desc_finances))
        conn.commit()
        conn.close()


# add_cards('https://mytaro.com.ua/assets/files/2022-02-07/1644262034-300226-rider-waite-smith-1909-03.jpg','Імператриця','Спокій, порозуміння, також вам варто виразити себе найближчим часом', 'Найближчим часом вас чекає спокійна обстановка, але варто проявити себе якось, аби вас побачили','Спокій, можливо порозуміння з колегами в питаннях, що раніше були конфліктними')
# add_cards('https://tarot.pp.ua/wp-content/uploads/2019/12/rider-waite-smith-1909-16.jpg','Вежа','Руйнування нинішньої ситуації, схильність до поганих дій','Схоже на когось чекають ДУУУЖЕ різкі зміни','Різка зміна нинішньої ситуації, на краще чи на гірше')
# add_cards('https://tarot.pp.ua/wp-content/uploads/2019/12/rider-waite-smith-1909-19.jpg','Сонце','Предвісник гарних подій, розквіт стосунків, налагодження ситуації','Найближчим часом вас чекає позитив та тепло',' у сфері фінансів у вас все добре')
# add_cards('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/RWS_Tarot_13_Death.jpg/220px-RWS_Tarot_13_Death.jpg','Смерть','Закінчення старих стосунків, або ж старої схеми стосунків, початок чогось нового','Скоро буде шанс почати те, що вас тривожить з нової сторінки','Скоро з’явиться можливість змінити потік грошенят, не втрать можливість!')
# add_cards('https://upload.wikimedia.org/wikipedia/commons/9/90/RWS_Tarot_00_Fool.jpg','Дурень','Для вас відкрито багато нових доріг та можливостей прямо зараз на любовному фронті, і вибір куди йти тільки за вами','Відпусти, те, що тривожить, і скоро доля подарує шанс на щось краще','Скоро вам можуть запропонувати кар’єрний зріст, не варто відмовлятися від такого подарунку долі')
# add_cards('https://upload.wikimedia.org/wikipedia/commons/c/c3/RWS_Tarot_04_Emperor.jpg','Імператор','У вас все стабільно, не потрібно перейматися, ви в безпеці','У вас в житті найближчим часом все буде стабільно','Особливих змін не передбачується, але стабільність, це не завжди погано чи добре')
# add_cards('https://tarot.pp.ua/wp-content/uploads/2019/12/rider-waite-smith-1909-02.jpg','Верховна жриця','Довірся своєму серцю, відключи мозок','Дійте за покликом серця!','саме час спертися на інтуіцію')
# add_cards('https://taro24.com.ua/wp-content/uploads/2022/12/%D1%82%D1%80%D1%96%D0%B9%D0%BA%D0%B0-%D0%BA%D1%83%D0%B1%D0%BA%D1%96%D0%B2.gif','Кубки',' Символ сердечності, закоханості, доброти та підтримки','Якщо у вас є проблеми, не закривайтесь в собі, люди вас підтримають, важливо лише правильно подати інформацію, та знайти правильну людину','схоже у вас є щось, що бентежить вас. Не варто перейматися, скоро ви отримаєте підтримку чи то від колег, чи грошову винагороду за труди')
# add_cards('https://cdn.pixabay.com/photo/2021/10/10/20/36/ace-of-pentacles-6698695_960_720.jpg','Туз пентаклів','Схоже твоя друга половинка зараз проявляє жадібність на любов до тебе','Не будьте жадібними, життя бумеранг',' Жадібність не призведе ні до чого гарного, пам’ятай')
# add_cards('https://mytaro.com.ua/assets/files/2022-02-07/1644268766-6705-rider-waite-smith-1909-74.jpg','Король пентаклів','Непорозуміння в знак недоговорення, труднощі','туднощі в житті найближчим часом, особливо з фінансами',' труднощі в сфері фінансів')
# add_cards('https://tarot.pp.ua/wp-content/uploads/2019/12/rider-waite-smith-1909-32.jpg','Король жезлів','Серйозний поступок зі сторони твоєї другої половинки','Щоб щось отримати, треба не боятися рухатись вперед та йти на ризик і жертви',' Серйозний поступок. Вам доведеться піти на якийсь важкий поступок для вас, зробити серйозний крок, аби збільшити свої грошенята')
# add_cards('https://upload.wikimedia.org/wikipedia/commons/3/3c/RWS_Tarot_10_Wheel_of_Fortune.jpg','Колесо фортуни','Все залежить від ситуації та твоїх дій, але доля гарно показує ситуацію, скоріше щось гарне, ніж погане','перед вами щодня сотні можливостей, і лише вам обирати якою дорогою йти і який вибір робити','у вас багато доріг, але вибір за вами!')
# add_cards('https://i.pinimg.com/550x/3e/99/54/3e9954ce71a103c6b87d4e95d201cc93.jpg','Перевернута карта','-','-','-')


# connect = sqlite3.connect('database.db')
# connect.execute("""CREATE TABLE users(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 phone TEXT NOT NULL,
#                 problem TEXT NOT NULL
#                 )""")
#
# connect.commit()
# connect.close()

# connect.execute("""DROP TABLE users""")
# connect.commit()
# connect.close()

def users():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        a=cursor.execute(''' SELECT * FROM users''').fetchall()
        conn.commit()
        conn.close()
        print(a)
# users()


# connect = sqlite3.connect('database.db')
# connect.execute("""CREATE TABLE predict(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 predict TEXT NOT NULL)""")
# connect.commit()
# connect.close()

def add_predict(predict):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(''' INSERT INTO predict(predict)
                     VALUES(?)''', (predict,))
        conn.commit()
        conn.close()

# add_predict('Не думаєш, що пора вибрати якусь одну дорогу? Ще трохи і тебе може розірвати…')
# add_predict('То що? Гарна інтуіція не завжди добре?')
# add_predict('Дозволь собі фантазувати! Вивільни свого Вінсента Вангога!')
# add_predict('Мені здається пора проявити милосердя до однієї людини, там де одна, там вже дві, три…')
# add_predict('Постав ціль, напиши план і дій!')
# add_predict('Харе токсичності!')
# add_predict('Всі думають, що ти ……, але я знаю що це не так)')
# add_predict('Зверни увагу на людей навколо, опусти свій ніс і зніми корону!')
# add_predict('Скоро твоя доля про себе нагадає')
# add_predict('Якщо ти думаєш, що в тебе трабл, просто подумай, що є єнот, що помив солодку вату…')
# add_predict('Ти бусічка!')
# add_predict('Блін! Та стань ти вже простим! Не всі навколо розуміють що 2 і 2 це 22!')
# add_predict('Присядь, віддихайся, подивись навколо, насолодись красою !')
# add_predict('Виправдання для лінивих слабаків!')
# add_predict('Інші люди думають, що ви як вулкан, непередбачувані і гарячі…')
# add_predict('Ти позитивчик)))')
# add_predict('Щоб побачити людину, не достатньо подивитися на неї 1 раз. Поговори з нею декілька разів!')


# connect = sqlite3.connect('database.db')
# connect.execute("""CREATE TABLE shop(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 image TEXT NOT NULL,
#                 title TEXT NOT NULL,
#                 desc TEXT,
#                 price INTEGER NOT NULL)""")
#
# connect.commit()
# connect.close()

def add_product(image, title, desc, price):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO shop (image, title, desc, price) VALUES (?, ?, ?, ?)",
                   (image, title, desc, price))
    conn.commit()
    conn.close()

# add_product("https://content.rozetka.com.ua/goods/images/big_tile/387381689.jpg","Таро Orner Starlight","Карти Таро Orner x Wyspell Starlight Tarot — ідеальне поєднання основних значень та символів оригінальної колоди з естетикою нічного неба.Starlight Tarot — нова колода від Orner x Wyspell, яка потрапить вам прямо в серденько.",350)
# add_product("https://content.rozetka.com.ua/goods/images/big/420664167.jpg"," таро Райдера Уейтаt","У поєднанні з книгою «Таро Уейта як система: теорія і практика» колода Вейта стає могутнім інструментом у віщуванні доль і відповідей на хвилюючі життєві питання. Книга стане джерелом корисної інформації, розкладів та базових складових ворожіння. Дві позиції ідеально поєднуються одна з одною.", 400)
# add_product("https://content1.rozetka.com.ua/goods/images/big/358087071.jpg","Таро світловидця – The Light seer`s tarot","Традиція: Уейт Молодші аркани: иллюстрації Масти: жезли, чаші, мечі, пентаклі Карти двору: Паж, Лицар, Дама, Король 0 Сила 8 Правосуддя 11 78 карт + інструкція англійською Розмір карт: 6 11 см Виробник: Китай",450)
# add_product("https://content.rozetka.com.ua/goods/images/big/394263185.jpg","Карти Таро Небо та Земля","Найкраща колода за останній час! Наповнена символізмом, але не перевантажена фарбами. На картах вказані відповідності літерам івриту, стихіям, положенням на дереві Сефірот, астрологічні значення. У колоді використовується символіка значень Уейта та Кроулі. Гарне якісне промальовування карток художником, це не комп'ютерна графіка. Колода дивовижної краси. Джек Сефірот кидає виклик позачасовій символіці Таро своїм неймовірним мистецтвом, де символи та приховані нюанси сплетені разом із найбільшою майстерністю. У цьому Таро кордон між духовним і матеріальним розмито, і все стає зрозумілим для чуйного читача.", 300)
# add_product("https://content2.rozetka.com.ua/goods/images/big/330942936.jpg","Таро Святої Смерті","Традиція: Уейт Молодші аркани: іллюстрації Масти: жезли, чаші, мечі, пентаклі Карти двору: Паж, Лицар, Дама, Король 0 Сила 8 Правосуддя 11 Склад: 78 карт + інструкція англійською Розмір карт: 6 5 х 12 см Виробник: Китай", 500)
# add_product("https://content.rozetka.com.ua/goods/images/big/407011334.jpg","Таро Божевільного місяця Deviant Moon","Чесна, прямолінійна та відкрита колода від екстравагантного художника Patrick Valenza примітна не лише надприродним дизайном, а й цікавою історією створення колоди. Кожен персонаж опрацьовувався місяцями, а створення всієї колоди зайняло понад три десятиліття копіткої праці, подорожей, досвіду та художньої роботи у північно-східному регіоні США, де збереглося багато старовинних будинків, предметів мистецтва та величних надгробків.Придбати Таро Божевільного Місяця можна порекомендувати тим, хто не прагне загнати себе та оточення в рамки якоїсь певної норми й готовий зануритися в темне море несвідомого.Комплектація колоди: 78 карт та інструкція англійською мовою.Розмір карт: 65х130 мм.", 350)
#

