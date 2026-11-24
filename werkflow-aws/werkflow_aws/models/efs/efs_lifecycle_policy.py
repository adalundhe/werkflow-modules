from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EFSLifecyclePolicy(BaseModel):
    TransitionToIA: StrictStr | None = None
    TransitionToPrimaryStorageClass: StrictStr | None = None
    TransitionToArchive: StrictStr | None = None
