from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_parameter import NeptuneParameter


class NeptuneEngineDefaults(BaseModel):
    DBParameterGroupFamily: StrictStr | None = None
    Marker: StrictStr | None = None
    Parameters: list[NeptuneParameter] | None = None
