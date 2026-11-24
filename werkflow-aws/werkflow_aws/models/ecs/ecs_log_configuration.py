from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_secret import ECSSecret


class ECSLogConfiguration(BaseModel):
    logDriver: StrictStr | None = None
    options: dict[StrictStr, StrictStr] | None = None
    secretOptions: list[ECSSecret] | None = None
