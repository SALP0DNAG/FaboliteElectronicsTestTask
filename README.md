# Тестовое задание для компании Fabolite Electronics.
Разработать простое серверное приложение на выбранном вами языке программирования (Python или JavaScript).
Реализовать базу данных (можно использовать PostgreSQL или любую другую удобную вам систему).
Реализовать функции регистрации и аутентификации пользователей.
Реализовать обработку следующих типов запросов:
  Получение списка пользователей.
  Добавление нового пользователя.
  Обновление информации о пользователе.
  Удаление пользователя.
## Требования
- Python 3.11.9
- PostgreSQL
## 1. Клонируйте репозиторий 
```
git clone https://github.com/SALP0DNAG/FaboliteElectronicsTestTask.git
cd FaboliteElectronicsTestTask
```
## 2. Установите зависимости
```
pip install -r requirements.txt
```
## 3. Настройте базу данных
Внутри вашего django проекта, в файле settings.py, укажите настройки базы данных.
```
'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': 'fabolite_electronics_test_task',
      'USER': 'test_user',
      'PASSWORD': 'password',
      'HOST': 'localhost',
      'PORT': '5432',
}
```
## 4. Создайте миграции
```
python manage.py makemigrations
python manage.py migrate
```
## 5. Загрузите fixtures
```
python manage.py loaddata app/fixtures/users.json
```
## 6. Запустите сервер
```
python manage.py runserver
```
