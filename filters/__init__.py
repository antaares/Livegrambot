from aiogram import Dispatcher

from filters.admins import IsAdmin
from .banned import Isbanned
from .group import IsGroup
from loader import dp
# from .is_admin import AdminFilter



if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(Isbanned)
    dp.filters_factory.bind(IsAdmin)
    pass
