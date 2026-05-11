# Automatyzacja testów aplikacji webowej Demoblaze.com w Pythonie

## Opis projektu

Projekt przedstawia automatyzację testów aplikacji webowej Demoblaze.com z wykorzystaniem języka Python oraz Selenium WebDriver.

Testy zostały przygotowane zgodnie ze wzorcem projektowym Page Object Model (POM), co umożliwia lepszą organizację kodu, łatwiejsze utrzymanie projektu oraz ponowne wykorzystanie komponentów testowych.

Projekt automatyzuje najważniejsze funkcjonalności sklepu internetowego:
- rejestrację użytkownika,
- logowanie,
- dodawanie produktów do koszyka,
- składanie zamówienia,
- obsługę koszyka zakupowego.

---

## Technologie

- Python
- Selenium WebDriver
- Unittest
- ChromeDriver
- Page Object Model (POM)
- DDT

---

## Struktura projektu

```text
Selenium-Projekt/
│
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── create_account_page.py
│   ├── customer_account_page.py
│   ├── home_page.py
│   ├── log_in_page.py
│   ├── nokia_lumia_1520.py
│   ├── phone_page.py
│   ├── place_order_page.py
│   └── samsung_galaxy_s6_page.py
│
├── test_data/
│   ├── orderData.csv
│   ├── place_order_data.py
│   ├── products_in_cart.py
│   └── registration_data.py
│
├── tests/
│   ├── base_test.py
│   ├── login_test.py
│   ├── purchase_test.py
│   └── registration_test.py
│
└── README.md
