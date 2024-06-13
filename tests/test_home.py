import allure
from utils.urls import Urls
from pages.home_page import SamokatHomePage


#@allure.epic('Эпик_Upgrade Main page / ui usability')
#@allure.parent_suite('Parent_suite_Домашняя страница')
@allure.suite('Suite_Header')
class TestSamokatHomePage:

    @allure.feature('Оформление заказа" Домашняя страница')
    @allure.story('"Оформление заказа" по кнопке "Заказать" из header')
    @allure.title('Нажатия на кнопку "Заказать" в header.')
    @allure.description('в header по кнопке "Заказать", '
                        'переход на страницу "Оформления заказа".')
    def test_click_top_order_button_show_order_page(self, driver):
        samokat_home_page = SamokatHomePage(driver)
        samokat_home_page.go_to_site()
        samokat_home_page.click_cookie_accept()
        samokat_home_page.click_top_order_button()
        assert samokat_home_page.current_url() == Urls.ORDER_PAGE

    @allure.feature('"Оформление заказа" из Домашней страницы')
    @allure.story('"Оформление заказа" по кнопке "Заказать" из блока "Как это работает"')
    @allure.title('Нажатие на кнопку "Заказать", в блоке "Как это работает".')
    @allure.description('Проверка "Как это работает" по кнопке "Заказать", '
                        'переход на страницу "Оформления заказа".')
    def test_click_bottom_order_button_show_order_page(self, driver):
        samokat_home_page = SamokatHomePage(driver)
        samokat_home_page.go_to_site()
        samokat_home_page.click_cookie_accept()
        samokat_home_page.click_bottom_order_button()

        assert samokat_home_page.current_url() == Urls.ORDER_PAGE

    @allure.feature('"ЯндексДзен" из Домашней страницы')
    @allure.story("редирект на Дзен по кнопке logo в header")
    @allure.title('При нажатии на лого "ЯндексСамокат" редирект на страницу "Дзен"')
    @allure.description('На домашней странице в header по кнопке "ЯндексСамокат" '
                        'происходит редирект на "Дзен".')
    def test_click_yandex_button_go_to_yandex(self, driver):
        samokat_home_page = SamokatHomePage(driver)
        samokat_home_page.go_to_site()
        samokat_home_page.click_cookie_accept()
        samokat_home_page.click_yandex_button()
        samokat_home_page.switch_window(1)
        samokat_home_page.wait_url_until_not_about_blank()
        current_url = samokat_home_page.current_url()

        assert (Urls.YANDEX_HOME_PAGE in current_url) or (Urls.DZEN_HOME_PAGE in current_url) or (Urls.YANDEX_CAPTCHA_PAGE in current_url)
