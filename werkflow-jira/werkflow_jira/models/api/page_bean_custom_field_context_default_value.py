from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr

if TYPE_CHECKING:
    from .custom_field_context_default_value import CustomFieldContextDefaultValue


class PageBeanCustomFieldContextDefaultValue(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[CustomFieldContextDefaultValue] | None = None
