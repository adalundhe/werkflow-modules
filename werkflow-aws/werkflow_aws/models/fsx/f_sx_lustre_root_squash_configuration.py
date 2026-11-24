from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxLustreRootSquashConfiguration(BaseModel):
    RootSquash: StrictStr | None = None
    NoSquashNids: list[StrictStr] | None = None
