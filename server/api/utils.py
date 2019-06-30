import random
import uuid

from django.core.validators import RegexValidator


color_code_validator = RegexValidator(
    r'^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$',
    message='Must be a valid color hex',
    code='invalid_hex',
)


def generate_uuid():
    return uuid.uuid4().hex


def generate_color():
    return '#%06x' % random.randint(0, 0xFFFFFF)


class RankHandler(object):

    def _make_or_fill_vacancy(self, position, dx):
        # dx = +1 to make a vacant place at `position`
        # dx = -1 to fill a vacant place at `position`
        for item_guid, item_rank in self.data.items():
            if position <= item_rank:
                self.data[item_guid] += dx

    def insert_item(self, guid, rank=None):
        # Insert `guid` at `rank`
        # Shift all the subsequent ranks to right

        max_rank = len(self.data) + 1

        if not rank or not 1 <= rank <= max_rank:
            rank = max_rank

        self._make_or_fill_vacancy(rank, dx=+1)

        self.data[guid] = rank

    def delete_item(self, guid):
        # Delete `guid` from ranking
        # Shift all the subsequent ranks to left

        rank = self.data.pop(guid, None)

        if not rank: return

        self._make_or_fill_vacancy(rank, dx=-1)

    def update_item(self, guid, new_rank):
        # Move `guid` to position `rank`
        # Shift all the ranks in between

        self.delete_item(guid)
        self.insert_item(guid, new_rank)
