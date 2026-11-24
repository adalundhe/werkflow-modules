from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class JsonTypeBean(BaseModel):
    configuration: dict[StrictStr, Any] | None = None
    custom: StrictStr | None = None
    customId: StrictInt | None = None
    items: StrictStr | None = None
    system: StrictStr | None = None
    type: StrictStr | None = None
