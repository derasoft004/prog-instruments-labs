from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time


def driver_scroller(driver_to_scroll, pix) -> None:
    sroll_range = 0
    while sroll_range < pix:
        driver_to_scroll.execute_script(f"window.scrollTo(0, {sroll_range});")  # ширина, высота
        sroll_range += 10  # скорость


def kassir_parser():
    driver = webdriver.Chrome()

    driver.get('https://smr.kassir.ru')

    # xpath_elements_title = driver.find_elements(By.XPATH,
    #                                           f"//h2[@class='recommendation-item_title compilation-tile__title']")
    xpath_elements_a = driver.find_elements(By.XPATH,
                                          f"//a[@class='recommendation-item_img-block compilation-tile__img-block']")
    xpath_elements_img = driver.find_elements(By.XPATH,
                                            f"//img[@class='h-full w-full object-cover']")
    print(len(xpath_elements_a), len(xpath_elements_img))
    driver_scroller(driver, 3000)
    # kassir_posters_titles = [element.text for element in xpath_elements_title]
    kassir_posters_links = [element.get_attribute('href') for element in xpath_elements_a]
    kassir_posters_photos = [element.get_attribute('src') for element in xpath_elements_img]
    ret_list = [(picture, link) for title, picture, link in
                zip(kassir_posters_links, kassir_posters_photos)]
    return ret_list


print(kassir_parser())
