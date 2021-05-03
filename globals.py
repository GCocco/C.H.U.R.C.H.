from typing import Union, TYPE_CHECKING


if TYPE_CHECKING:
    from main import Base


class Globals:
    __base: Union['Base', None] = None

    @staticmethod
    def init(base):
        assert Globals.__base is None
        Globals.__base = base
        return
    pass
