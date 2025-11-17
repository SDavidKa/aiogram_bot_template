from .async_data_cache import AsyncDataCache
from src.api.endpoints.groups import get_groups_info

groups_cache = AsyncDataCache(loader_func=get_groups_info)
