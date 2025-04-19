from typing import Callable, Union, Optional
import csv

# Часть 1
def password_checker(func: Callable) -> Callable:

    def wrapper(password: str) -> Union[str, ValueError]:
        special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>/?"

        if len(password) < 8:
            return "Ошибка: Пароль должен быть не менее 8 символов"
        if not any(c.isdigit() for c in password):
            return "Ошибка: Пароль должен содержать цифру"
        if not any(c.isupper() for c in password):
            return "Ошибка: Пароль должен содержать заглавную букву"
        if not any(c.islower() for c in password):
            return "Ошибка: Пароль должен содержать строчную букву"
        if not any(c in special_chars for c in password):
            return "Ошибка: Пароль должен содержать спецсимвол"

        return func(password)
    return wrapper

@password_checker
def register_user_v1(password: str) -> str:
    return "Успешная регистрация! Пароль надежный."

# Часть two


def password_validator(
    min_length: int = 8,
    min_uppercase: int = 1,
    min_lowercase: int = 1,
    min_special_chars: int = 1
) -> Callable:
   
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> None:
            errors = []
            special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>/?"

            # Проверка длины
            if len(password) < min_length:
                errors.append(f"Длина пароля < {min_length}")

            # Проверка заглавных
            uppercase = sum(1 for c in password if c.isupper())
            if uppercase < min_uppercase:
                errors.append(f"Заглавных букв < {min_uppercase}")

            # Проверка строчных
            lowercase = sum(1 for c in password if c.islower())
            if lowercase < min_lowercase:
                errors.append(f"Строчных букв < {min_lowercase}")

            # Проверка спецсимволов
            special = sum(1 for c in password if c in special_chars)
            if special < min_special_chars:
                errors.append(f"Спецсимволов < {min_special_chars}")

            if errors:
                raise ValueError(" | ".join(errors))
            
            return func(username, password)
        return wrapper
    return decorator

def username_validator(func: Callable) -> Callable:
    
    def wrapper(username: str, password: str) -> None:
        if ' ' in username:
            raise ValueError("Имя пользователя содержит пробелы")
        return func(username, password)
    return wrapper

@username_validator
@password_validator(min_length=10, min_uppercase=2, min_lowercase=2, min_special_chars=2)
def register_user_v2(username: str, password: str) -> None:
    
    with open('users.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])