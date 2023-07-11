'''
This code scrapes content from the Takealot.com website to do the following:
1. Gives the price, seller and availability of a product
2. Repeat the steps above, but for an alternatively available offer for the main product.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

DRIVER_EXECUTABLE = "C:/Users/Mpho.Saba/Downloads/chromedriver.exe"  # install Chrome driver and change absolute path to test"

def print_line(values, feature):
    '''
    This function checks whether or not the other offer is available and substitues the value with Not Available
    :param values: list of values to check
    :param feature: Price/Supplier/Availability
    :return: formatted string of the input that will be printed
    '''
    if len(values) < 2:
        return f"{feature}: \nMain Product -> {values[0]} \nOther offer: Not Available\n"
    else:
        return f"{feature}: \nMain Product -> {values[0]} \nOther offer: {values[1]}\n"


def print_values(item_list):
    '''
    This function print all the results of the program
    :param item_list: list of prices, availability list, supplier info (str), product title
    :return: None
    '''
    print(f"Product: {item_list[-1]}\n")
    print(print_line(item_list[0], "Price"))
    print(print_line(item_list[1], "Availability"))
    print(f"Seller/Supplier: {item_list[2]}")

def main():
    driver = webdriver.Chrome(DRIVER_EXECUTABLE)

    driver.get("https://www.takealot.com/russell-hobbs-2200w-crease-control-iron/PLID34147865")

    product_title = driver.find_element(By.CSS_SELECTOR, '.product-title h1').text

    # Pulling price of main and other offer
    main_price = driver.find_element(By.CSS_SELECTOR, "div.buybox-module_price_2YUFa").text
    price = [i.text for i in driver.find_elements(By.CSS_SELECTOR, 'span.currency.plus.currency-module_currency_29IIm')]
    try:
        price = price[20:][4]
    except:
        price = "Not Available"

    #Pulling the product availability
    availability = [i.text for i in driver.find_elements(By.CSS_SELECTOR, 'div.cell.shrink.stock-availability-status')]
    try:
        availability = availability[:2]
    except:
        availability = availability[0]

    #Pulling the seller/supplier info
    next_seller = [i.text for i in driver.find_elements(By.CLASS_NAME, 'seller-information')]
    try:
        next_seller_cleaned = [i.replace("Fulfilled by Takealot", "") for i in next_seller][0]
    except:
        next_seller_cleaned = "Not Available"

    # Pass all the results the print_values function for them to be printed
    print_values([[main_price, price], availability, next_seller_cleaned, product_title])

    driver.quit()  # this shuts down entire browser after executing code

if __name__ == '__main__':
    main()
