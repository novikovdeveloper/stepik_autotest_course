Это репозиторий для хранения домашних работ по курсу автоматизация тестирования на степике, https://stepik.org/course/575  

Запускать тесты для ревью с помощью команды:  

pytest -m need_review -v --browser_name=chrome test_product_page.py 

Старые тесты помечены декоратором @pytest.mark.skip, если их необходимо запустить, то его декоратор нужно убрать  

