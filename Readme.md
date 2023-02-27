Используемые модули:  
allure   
pytest   
requests   
dotenv  
OS    

Скопировать файла .env.example в .env  
Необходимый стенд указать в файле .env  

Запуск тестов  
pytest -sv --alluredir=test_results test/  
Формирование отчета  
allure serve test_results  
