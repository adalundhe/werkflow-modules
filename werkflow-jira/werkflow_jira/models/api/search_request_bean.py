from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SearchRequestBean(BaseModel):
    expand: list[StrictStr] | None = None
    fields: list[StrictStr] | None = None
    fieldsByKeys: StrictBool | None = None
    jql: StrictStr | None = None
    maxResults: StrictInt | None = None
    properties: list[StrictStr] | None = None
    startAt: StrictInt | None = None
    validateQuery: StrictStr | None = None
