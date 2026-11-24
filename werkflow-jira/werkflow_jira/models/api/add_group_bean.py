from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class AddGroupBean(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: StrictStr | None = None
