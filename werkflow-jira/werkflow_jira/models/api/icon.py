from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class Icon(BaseModel):
    model_config = ConfigDict(extra="allow")

    link: StrictStr | None = None
    title: StrictStr | None = None
    url16x16: StrictStr | None = None
