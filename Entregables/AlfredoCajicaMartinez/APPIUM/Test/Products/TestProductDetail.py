import pytest
from Screens.Login.Login_Screen import Login_Screen
from Screens.Products.Products_Screen import Products_Screen
from Screens.Products.Products_Detail_Screen import Product_Detail_Screen
from Utils.Dictionaries.Products.Products_Info import FIRST_PRODUCT_INFO


@pytest.mark.regression
def test_check_product_detail_info(driver):
    log = Login_Screen(driver)
    p = Products_Screen(driver)
    pd = Product_Detail_Screen(driver)
    log.login()
    p.tap_element(*p.first_product)
    # assert para validar nombre, descripción y precio del primer producto
    assert pd.get_element_attribute('text', *pd.text_product_name) == FIRST_PRODUCT_INFO.get("name")\
           and pd.get_element_attribute('text', *pd.text_product_description) == FIRST_PRODUCT_INFO.get("description")\
           and pd.get_element_attribute('text', *pd.text_product_price) == FIRST_PRODUCT_INFO.get("price")
