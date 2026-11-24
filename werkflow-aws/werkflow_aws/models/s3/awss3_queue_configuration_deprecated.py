from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3QueueConfigurationDeprecated(BaseModel):
    Id: StrictStr | None = None
    Event: StrictStr | None = None
    Events: list[StrictStr] | None = None
    Queue: StrictStr | None = None
