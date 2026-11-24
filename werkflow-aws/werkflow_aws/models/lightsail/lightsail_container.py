from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailContainer(BaseModel):
    image: StrictStr | None = None
    command: list[StrictStr] | None = None
    environment: dict[StrictStr, StrictStr] | None = None
    ports: dict[StrictStr, StrictStr] | None = None
