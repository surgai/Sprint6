import pytest
import allure
from pages.home_page import SamokatHomePage
from utils.test_data import SamokatHomePageFAQ
from utils.locators import SamokatHomePageLocator

@allure.epic('Main page / ui usability')
@allure.parent_suite('Parent_suite_Домашняя страница')
@allure.suite('Suite_FAQ')
class TestSamokatFAQPage:
    @allure.feature('Фича_Аккордион с вопрос/ответ на Домашней страницы')
    @allure.story('Стори_При нажатии на вопрос в разделе "Вопросы о важном" раскрывается ответ.')
    @allure.title('При нажатии на вопрос раскрывается ответ ')
    @allure.description('Проверка что при нажатии на поле вопроса в блоке "Вопросы о важном", '
                        'данный вопрос раскрывается и текст в нем соответствует ТЗ')
    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, SamokatHomePageFAQ.answer1),
            (1, 1, SamokatHomePageFAQ.answer2),
            (2, 2, SamokatHomePageFAQ.answer3),
            (3, 3, SamokatHomePageFAQ.answer4),
            (4, 4, SamokatHomePageFAQ.answer5),
            (5, 5, SamokatHomePageFAQ.answer6),
            (6, 6, SamokatHomePageFAQ.answer7),
            (7, 7, SamokatHomePageFAQ.answer8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        samokat_home_page = SamokatHomePage(driver)
        samokat_home_page.go_to_site()
        samokat_home_page.click_cookie_accept()
        samokat_home_page.click_faq_question(question_number=question)
        answer = samokat_home_page.find_element(SamokatHomePageLocator.FAQ_ANSWER(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ на вопрос не совпадает с ожидаемым значением '
