from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class DMSRdsRequirements(BaseModel):
    EngineEdition: StrictStr | None = None
    InstanceVcpu: StrictFloat | StrictInt | None = None
    InstanceMemory: StrictFloat | StrictInt | None = None
    StorageSize: StrictInt | None = None
    StorageIops: StrictInt | None = None
    DeploymentOption: StrictStr | None = None
    EngineVersion: StrictStr | None = None
