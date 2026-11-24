from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesUpdateWorkspaceBundleRequest(BaseModel):
    BundleId: StrictStr | None = None
    ImageId: StrictStr | None = None
