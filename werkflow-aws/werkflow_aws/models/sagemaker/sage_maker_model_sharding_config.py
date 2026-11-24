from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelShardingConfig(BaseModel):
    Image: StrictStr | None = None
    OverrideEnvironment: dict[StrictStr, StrictStr] | None = None
