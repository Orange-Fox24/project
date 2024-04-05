Welcome file
Welcome file
# Умный Холодильник

Добро пожаловать в приложение «Умный холодильник»! Здесь вы можете легко добавлять продукты, отслеживать сроки их годности, получать уведомления об истечении срока годности и находить рецепты вкусных блюд. Готовьте с удовольствием и без лишних забот!

Кнопка «Следующая страница» уничтожит текущее окно и создаст новое с заголовком «Умный Холодильник!». и размеры 1300x600 пикселей. Окно будет иметь значок и фоновое изображение.

Второе окно будет создано через две секунды, а затем уничтожено еще через две секунды, перемещая пользователя на следующую страницу.

В первом окне будет отображаться изображение с помощью функции show_image.

## Функции

- next_page: уничтожить текущее окно и создать новое с указанными свойствами.
- show_image: отобразить изображение на экране, а затем перейти на следующую страницу.

## Глобальные переменные

- root1, root2: объекты Windows Tkinter.
- bg_image: фоновое изображение, используемое в обоих окнах.
- image_label: объект метки, который отображает изображение в первом окне.

## Первое окно

Сначала создайте окно без размера, затем установите его размер на весь экран. Установите значок и фоновое изображение окна. Добавьте метку с текстом приветствия и кнопку, ведущую на следующую страницу.

## Второе окно

Создайте окно с определенными размерами и свойствами. Установите значок и фоновое изображение окна. Добавьте метку с инструкциями и виджет древовидного представления для отображения информации о продукте.

## Конфигурация представления

Настройте виджет в виде таблицы с тремя столбцами: «Название продукта», «Срок года» и «Категория». Заполните древовидное представление примерами данных.

## Проверка срока годности

Проверьте дату истечения срока годности каждого продукта в древовидном представлении и отобразите предупреждающее сообщение, если срок годности продукта истек или близок к истечению.

## Выбор категории

Разрешите пользователю выбрать категорию из списка и открыть третье окно, где он сможет добавлять продукты в древовидное представление на основе выбранной категории.
# Импортируем необходимые библиотеки
импортировать tkinter как tk из tkinter, импортировать окно сообщения из tkinter, импортировать прокручиваемый текст из PIL, импортировать изображение, запросы на импорт ImageTk из deep_translator, импортировать GoogleTranslator из io, импортировать BytesIO







# Определяем класс Recipe
Рецепт класса:     def init(self, name, категория, ингредиенты, инструкции, image_url):         self.name = имя         self.category = категория         self.ingredients = ингредиенты         self.instructions = инструкции         self.image_url = image_url







# Создаем пустой список для хранения рецептов
каталог = []

# Функция для получения рецепта
def get_recipe(texter):     # Здесь нужно указать URL API     url = API     ответ = Requests.get(url)     if response.status_code == 200:         data = response.json()         рецепт_данные = data['meals'][0]         name = рецепт_данные['strMeal']         категория = рецепт_данные['strCategory']         ингредиенты = [рецепт_данные[f'strIngredient{i}'] для i в диапазоне (1, 21), если рецепт_данные[f'strIngredient{i}']]         инструкции = данные_рецепта['strInstructions']         image_url = данные_рецепта['strMealThumb']         return Recipe(имя, категория, ингредиенты, инструкции, image_url)     else:         return None



    



        





        




# Функция для перевода рецепта
def translate_recipe(text):     # Перевод текста рецепта     переведенный_текст = GoogleTranslator(source="auto", target="ru").translate(text)     return переведенный_текст




# Функция для добавления рецепта в каталог
def add_recipe(category_recipe_id):     for i in range(len(category_recipe_id)):         texter = "lookup.php?i=" + (str(category_recipe_id[i]))         рецепт = get_recipe(texter)         if рецепт:             каталог.append( рецепт)             переведенное_имя = переводчик_рецепт(рецепт.название)             lb_recipes.insert(tk.END, переведенное_имя)             lbl_status.config(text=f"Рецепт '{translated_name}' добавлен в каталог.")         else:             messagebox.showerror("Ошибка", "Не удалось получить рецепт с сайта")











# Функция для добавления случайного рецепта в каталог
def add_random_recipe_to_catalog():
    texter = "random.php"
    recipe = get_recipe(texter)
    if recipe:
        catalog.append(recipe)
        translated_name = translate_recipe(recipe.name)
        lb_recipes.insert(tk.END, translated_name)
        lbl_status.config(text=f"Рецепт '{translated_name}' добавлен в каталог.")
    else:
        messagebox.showerror("Ошибка", "Не удалось получить рецепт с сайта")

# Функция для выбора категории рецепта
def select_recipe_category():
    def on_select():
        category = v.get()
        index_categories_recipe = categories_recipe_translated.index(category)
        
        messagebox.showinfo("Ваш выбор", f"Вы выбрали: {category}")
        category_window.destroy()
        categories_recipe = ["Beef", "Breakfast", "Chicken", "Dessert", "Goat", "Lamb", "Miscellaneous",
                             "Pasta", "Pork", "Seafood", "Side", "Starter", "Vegan", "Vegetarian"]
        index_recipe = categories_recipe[int(index_categories_recipe)]
        url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + index_recipe
        response = requests.get(url)
        category_recipe_id = []
        data
Умный Холодильник
Добро пожаловать в приложение «Умный холодильник»! Здесь вы можете легко добавлять продукты, отслеживать сроки их годности, получать уведомления об истечении срока годности и находить рецепты вкусных блюд. Готовьте с удовольствием и без лишних забот!

Кнопка «Следующая страница» уничтожит текущее окно и создаст новое с заголовком «Умный Холодильник!». и размеры 1300x600 пикселей. Окно будет иметь значок и фоновое изображение.

Второе окно будет создано через две секунды, а затем уничтожено еще через две секунды, перемещая пользователя на следующую страницу.

В первом окне будет отображаться изображение с помощью функции show_image.

Функции
next_page: уничтожить текущее окно и создать новое с указанными свойствами.
show_image: отобразить изображение на экране, а затем перейти на следующую страницу.
Глобальные переменные
root1, root2: объекты Windows Tkinter.
bg_image: фоновое изображение, используемое в обоих окнах.
image_label: объект метки, который отображает изображение в первом окне.
Первое окно
Сначала создайте окно без размера, затем установите его размер на весь экран. Установите значок и фоновое изображение окна. Добавьте метку с текстом приветствия и кнопку, ведущую на следующую страницу.

Второе окно
Создайте окно с определенными размерами и свойствами. Установите значок и фоновое изображение окна. Добавьте метку с инструкциями и виджет древовидного представления для отображения информации о продукте.

Конфигурация представления
Настройте виджет в виде таблицы с тремя столбцами: «Название продукта», «Срок года» и «Категория». Заполните древовидное представление примерами данных.

Проверка срока годности
Проверьте дату истечения срока годности каждого продукта в древовидном представлении и отобразите предупреждающее сообщение, если срок годности продукта истек или близок к истечению.

Выбор категории
Разрешите пользователю выбрать категорию из списка и открыть третье окно, где он сможет добавлять продукты в древовидное представление на основе выбранной категории.

Импортируем необходимые библиотеки
импортировать tkinter как tk из tkinter, импортировать окно сообщения из tkinter, импортировать прокручиваемый текст из PIL, импортировать изображение, запросы на импорт ImageTk из deep_translator, импортировать GoogleTranslator из io, импортировать BytesIO

Определяем класс Recipe
Рецепт класса: def init(self, name, категория, ингредиенты, инструкции, image_url): self.name = имя self.category = категория self.ingredients = ингредиенты self.instructions = инструкции self.image_url = image_url

Создаем пустой список для хранения рецептов
каталог = []

Функция для получения рецепта
def get_recipe(texter): # Здесь нужно указать URL API url = API ответ = Requests.get(url) if response.status_code == 200: data = response.json() рецепт_данные = data[‘meals’][0] name = рецепт_данные[‘strMeal’] категория = рецепт_данные[‘strCategory’] ингредиенты = [рецепт_данные[f’strIngredient{i}’] для i в диапазоне (1, 21), если рецепт_данные[f’strIngredient{i}’]] инструкции = данные_рецепта[‘strInstructions’] image_url = данные_рецепта[‘strMealThumb’] return Recipe(имя, категория, ингредиенты, инструкции, image_url) else: return None

Функция для перевода рецепта
def translate_recipe(text): # Перевод текста рецепта переведенный_текст = GoogleTranslator(source=“auto”, target=“ru”).translate(text) return переведенный_текст

Функция для добавления рецепта в каталог
def add_recipe(category_recipe_id): for i in range(len(category_recipe_id)): texter = “lookup.php?i=” + (str(category_recipe_id[i])) рецепт = get_recipe(texter) if рецепт: каталог.append( рецепт) переведенное_имя = переводчик_рецепт(рецепт.название) lb_recipes.insert(tk.END, переведенное_имя) lbl_status.config(text=f"Рецепт ‘{translated_name}’ добавлен в каталог.") else: messagebox.showerror(“Ошибка”, “Не удалось получить рецепт с сайта”)

Функция для добавления случайного рецепта в каталог
def add_random_recipe_to_catalog():
texter = “random.php”
recipe = get_recipe(texter)
if recipe:
catalog.append(recipe)
translated_name = translate_recipe(recipe.name)
lb_recipes.insert(tk.END, translated_name)
lbl_status.config(text=f"Рецепт ‘{translated_name}’ добавлен в каталог.")
else:
messagebox.showerror(“Ошибка”, “Не удалось получить рецепт с сайта”)

Функция для выбора категории рецепта
def select_recipe_category():
def on_select():
category = v.get()
index_categories_recipe = categories_recipe_translated.index(category)

    messagebox.showinfo("Ваш выбор", f"Вы выбрали: {category}")
    category_window.destroy()
    categories_recipe = ["Beef", "Breakfast", "Chicken", "Dessert", "Goat", "Lamb", "Miscellaneous",
                         "Pasta", "Pork", "Seafood", "Side", "Starter", "Vegan", "Vegetarian"]
    index_recipe = categories_recipe[int(index_categories_recipe)]
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + index_recipe
    response = requests.get(url)
    category_recipe_id = []
    data
