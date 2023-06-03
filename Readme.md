Используемые модули:  
allure   
pytest   
requests   
python-dotenv
OS    
pip install psycopg2-binary

Скопировать файла .env.example в .env  
Необходимый стенд указать в файле .env  

Запуск тестов  
pytest -sv --alluredir=test_results test/  
Формирование отчета  
allure serve test_results  
