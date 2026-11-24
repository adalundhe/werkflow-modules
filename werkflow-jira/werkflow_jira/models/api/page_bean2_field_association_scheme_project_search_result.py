from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .field_association_scheme_project_search_result import FieldAssociationSchemeProjectSearchResult


class PageBean2FieldAssociationSchemeProjectSearchResult(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[FieldAssociationSchemeProjectSearchResult] | None = None
