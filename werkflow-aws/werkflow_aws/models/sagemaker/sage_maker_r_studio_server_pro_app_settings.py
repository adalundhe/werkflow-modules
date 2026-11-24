from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerRStudioServerProAppSettings(BaseModel):
    AccessStatus: StrictStr | None = None
    UserGroup: StrictStr | None = None
