from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LakeFormationGetEffectivePermissionsForPathRequest(BaseModel):
    ResourceArn: StrictStr
    CatalogId: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
