from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class DMSRdsConfiguration(BaseModel):
    EngineEdition: StrictStr | None = None
    InstanceType: StrictStr | None = None
    InstanceVcpu: StrictFloat | StrictInt | None = None
    InstanceMemory: StrictFloat | StrictInt | None = None
    StorageType: StrictStr | None = None
    StorageSize: StrictInt | None = None
    StorageIops: StrictInt | None = None
    DeploymentOption: StrictStr | None = None
    EngineVersion: StrictStr | None = None
