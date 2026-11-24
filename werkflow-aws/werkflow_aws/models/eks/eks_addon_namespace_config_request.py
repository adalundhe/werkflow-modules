from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSAddonNamespaceConfigRequest(BaseModel):
    namespace: StrictStr | None = None
