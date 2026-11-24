from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .field_association_scheme_field_search_result import FieldAssociationSchemeFieldSearchResult


class PageBean2FieldAssociationSchemeFieldSearchResult(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[FieldAssociationSchemeFieldSearchResult] | None = None
