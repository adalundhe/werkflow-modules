from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMAttachedPermissionsBoundaryModel(BaseModel):
    PermissionsBoundaryType: StrictStr | None = None
    PermissionsBoundaryArn: StrictStr | None = None
