from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GlueSpigot(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Path: StrictStr | None = None
    Topk: StrictInt | None = None
    Prob: StrictFloat | StrictInt | None = None
