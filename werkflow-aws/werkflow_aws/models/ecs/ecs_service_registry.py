from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSServiceRegistry(BaseModel):
    registryArn: StrictStr | None = None
    port: StrictInt | None = None
    containerName: StrictStr | None = None
    containerPort: StrictInt | None = None
