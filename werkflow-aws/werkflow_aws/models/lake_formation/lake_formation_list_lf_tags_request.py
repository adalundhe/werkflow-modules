from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class LakeFormationListLFTagsRequest(BaseModel):
    CatalogId: StrictStr | None = None
    ResourceShareType: Literal['FOREIGN', 'ALL'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
