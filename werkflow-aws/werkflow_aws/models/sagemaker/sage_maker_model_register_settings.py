from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelRegisterSettings(BaseModel):
    Status: StrictStr | None = None
    CrossAccountModelRegisterRoleArn: StrictStr | None = None
