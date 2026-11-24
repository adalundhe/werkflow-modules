from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .search_result_field_parameters import SearchResultFieldParameters
from .search_result_work_type_parameters import SearchResultWorkTypeParameters


class FieldAssociationSchemeFieldSearchResult(BaseModel):
    allowedOperations: list[StrictStr] | None = None
    fieldId: StrictStr | None = None
    parameters: SearchResultFieldParameters | None = None
    restrictedToWorkTypes: list[StrictStr] | None = None
    workTypeParameters: list[SearchResultWorkTypeParameters] | None = None
