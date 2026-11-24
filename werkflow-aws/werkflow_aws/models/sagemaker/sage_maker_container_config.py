from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerContainerConfig(BaseModel):
    ContainerArguments: list[StrictStr] | None = None
    ContainerEntrypoint: list[StrictStr] | None = None
    ContainerEnvironmentVariables: dict[StrictStr, StrictStr] | None = None
