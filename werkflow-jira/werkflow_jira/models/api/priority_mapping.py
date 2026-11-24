from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictInt, StrictStr


class PriorityMapping(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    in_: dict[StrictStr, StrictInt] | None = PydanticField(default=None, alias='in')
    out: dict[StrictStr, StrictInt] | None = None
