from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSAddonNamespaceConfigResponse(BaseModel):
    namespace: StrictStr | None = None
