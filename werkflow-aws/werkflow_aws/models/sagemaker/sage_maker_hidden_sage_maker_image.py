from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerHiddenSageMakerImage(BaseModel):
    SageMakerImageName: StrictStr | None = None
    VersionAliases: list[StrictStr] | None = None
