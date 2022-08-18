import pytest
from settings import valid_email, valid_password

def testing_all_pet_cards():
   '''Проверка всех карточек питомцев'''

   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)

   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys(valid_email)

   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys(valid_password)

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

   #Мы объявили три переменные, в которых записали все найденные элементы на странице:
   # в images — все картинки питомцев, в names — все их имена, в descriptions — все виды и возрасты
   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

   assert names[0].text != ''

   for i in range(len(names)):
      assert images[i].get_attribute('src') != '' # на странице нет питомцев без фото
      assert names[i].text != '' # на странице нет питомцев без Имени
      assert descriptions[i].text != '' # на странице нет питомцев с пустым полем для указания Породы и возраста
      assert ',' in descriptions[i].text # проверяем, что между породой и лет есть запятая (значит есть оба значения)
      parts = descriptions[i].text.split(", ") # Создаём список, где разделитель значений - запятая
      assert len(parts[0]) > 0 # Проверяем, что длина текста в первой части списка и
      assert len(parts[1]) > 0 # ...и во второй > 0, значит там что-то да указано! Если нет -> FAILED!

#python -m pytest -v --driver Chrome --driver-path C:/TESTER/chromedriver.exe  C:/Users/Иван/PycharmProjects/pythonProject1/testing_all_pets_cards.py