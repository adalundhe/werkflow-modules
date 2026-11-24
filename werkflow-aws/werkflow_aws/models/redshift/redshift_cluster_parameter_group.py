from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftClusterParameterGroup(BaseModel):
    ParameterGroupName: StrictStr | None = None
    ParameterGroupFamily: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
