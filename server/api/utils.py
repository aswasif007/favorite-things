import random
import uuid

from django.core.validators import RegexValidator


color_code_validator = RegexValidator(r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})')


def generate_uuid():
    return uuid.uuid4().hex


def generate_color():
    return '#%06x' % random.randint(0, 0xFFFFFF)
