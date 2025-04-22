#модуль strings.py (пространство имен для строк)

__all__ = ['to_upper', 'remove_spaces']

def to_upper(s):
    return s.upper()

def remove_spaces(s):
    return s.replace(" ", "")

def _secret_reverse(s):
    return s[::-1]