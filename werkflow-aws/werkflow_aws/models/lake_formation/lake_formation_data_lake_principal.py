from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDataLakePrincipal(BaseModel):
    DataLakePrincipalIdentifier: StrictStr | None = None
