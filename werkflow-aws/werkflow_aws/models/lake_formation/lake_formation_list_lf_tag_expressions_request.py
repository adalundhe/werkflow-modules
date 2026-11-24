from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LakeFormationListLFTagExpressionsRequest(BaseModel):
    CatalogId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
