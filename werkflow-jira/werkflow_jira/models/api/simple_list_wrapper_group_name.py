from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictInt
from .group_name import GroupName
from .list_wrapper_callback_group_name import ListWrapperCallbackGroupName


class SimpleListWrapperGroupName(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    callback: ListWrapperCallbackGroupName | None = None
    items: list[GroupName] | None = None
    max_results: StrictInt | None = PydanticField(default=None, alias='max-results')
    pagingCallback: ListWrapperCallbackGroupName | None = None
    size: StrictInt | None = None
