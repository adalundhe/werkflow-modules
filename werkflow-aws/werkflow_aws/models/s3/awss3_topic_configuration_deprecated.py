from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3TopicConfigurationDeprecated(BaseModel):
    Id: StrictStr | None = None
    Events: list[StrictStr] | None = None
    Event: StrictStr | None = None
    Topic: StrictStr | None = None
