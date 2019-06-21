import random
import uuid

from django.core.validators import RegexValidator


color_code_validator = RegexValidator(
    r'^#([1-9a-fA-F]{3}|[1-9a-fA-F]{6})$',
    message='Must be a valid color hex',
    code='invalid_hex',
)


def generate_uuid():
    return uuid.uuid4().hex


def generate_color():
    return '#%06x' % random.randint(0, 0xFFFFFF)
