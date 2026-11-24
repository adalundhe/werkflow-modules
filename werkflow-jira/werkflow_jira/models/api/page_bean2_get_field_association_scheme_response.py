from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .get_field_association_scheme_response import GetFieldAssociationSchemeResponse


class PageBean2GetFieldAssociationSchemeResponse(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[GetFieldAssociationSchemeResponse] | None = None
