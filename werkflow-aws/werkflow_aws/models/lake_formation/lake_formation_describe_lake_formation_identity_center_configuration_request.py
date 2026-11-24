from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDescribeLakeFormationIdentityCenterConfigurationRequest(BaseModel):
    CatalogId: StrictStr | None = None
