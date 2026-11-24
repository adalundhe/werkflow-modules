from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftIPRange(BaseModel):
    Status: StrictStr | None = None
    CIDRIP: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
