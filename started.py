import cianparser 
from time import sleep 
 
a = 0 
moscow_parser = cianparser.CianParser(location="Долгопрудный") 
while a < 30: 
    data = moscow_parser.get_flats(deal_type = "sale", rooms = (1), with_saving_csv = True, with_extra_data = True, additional_settings = {"start_page":1+a,"end_page": 2+a}) 
    sleep(40) 
    a+=2



























