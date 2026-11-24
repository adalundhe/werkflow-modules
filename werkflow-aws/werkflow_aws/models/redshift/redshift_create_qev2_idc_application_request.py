from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateQev2IdcApplicationRequest(BaseModel):
    IdcInstanceArn: StrictStr
    Qev2IdcApplicationName: StrictStr
    IdcDisplayName: StrictStr
    Tags: list[RedshiftTag] | None = None
