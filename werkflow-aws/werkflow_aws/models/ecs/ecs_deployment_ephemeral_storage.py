from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDeploymentEphemeralStorage(BaseModel):
    kmsKeyId: StrictStr | None = None
