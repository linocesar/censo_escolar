from selenium.common.exceptions import TimeoutException
from selenium import webdriver

url1 = "https://sistemas.anm.gov.br/SCM/site/admin/pesquisarProcessos.aspx"
url2 = "https://cdp.anp.gov.br/ords/r/cdp_apex/consulta-dados-publicos-cdp/home"
url3 = "https://sistemas.anac.gov.br/CNPA/PesquisarCnpa"

try:
    with webdriver.Chrome() as driver:
        driver.set_page_load_timeout(30)
        driver.get(url=url1)

        logs = driver.get_log('browser')
        for entry in logs:
            if entry['level'] == 'SEVERE' and entry['source'] == 'network':
                print("Erro no site: " + entry['message'])
except TimeoutException as e:
    print("Site não responde: timeout")


