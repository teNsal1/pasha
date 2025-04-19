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
