from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_parameter import RedshiftParameter


class RedshiftDefaultClusterParameters(BaseModel):
    ParameterGroupFamily: StrictStr | None = None
    Marker: StrictStr | None = None
    Parameters: list[RedshiftParameter] | None = None
