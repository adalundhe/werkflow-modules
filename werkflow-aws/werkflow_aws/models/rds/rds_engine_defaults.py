from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_parameter import RDSParameter


class RDSEngineDefaults(BaseModel):
    DBParameterGroupFamily: StrictStr | None = None
    Marker: StrictStr | None = None
    Parameters: list[RDSParameter] | None = None
