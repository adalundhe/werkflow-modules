from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictInt
from .application_role import ApplicationRole
from .list_wrapper_callback_application_role import ListWrapperCallbackApplicationRole


class SimpleListWrapperApplicationRole(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    callback: ListWrapperCallbackApplicationRole | None = None
    items: list[ApplicationRole] | None = None
    max_results: StrictInt | None = PydanticField(default=None, alias='max-results')
    pagingCallback: ListWrapperCallbackApplicationRole | None = None
    size: StrictInt | None = None
