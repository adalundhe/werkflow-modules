from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAppSpecification(BaseModel):
    ImageUri: StrictStr | None = None
    ContainerEntrypoint: list[StrictStr] | None = None
    ContainerArguments: list[StrictStr] | None = None
