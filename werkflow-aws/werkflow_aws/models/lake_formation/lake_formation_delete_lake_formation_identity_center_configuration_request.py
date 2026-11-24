from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDeleteLakeFormationIdentityCenterConfigurationRequest(BaseModel):
    CatalogId: StrictStr | None = None
