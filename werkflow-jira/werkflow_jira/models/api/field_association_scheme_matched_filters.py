from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FieldAssociationSchemeMatchedFilters(BaseModel):
    projectIds: list[StrictInt] | None = None
    query: StrictStr | None = None
