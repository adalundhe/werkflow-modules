from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDeleteWorkspaceBundleRequest(BaseModel):
    BundleId: StrictStr | None = None
