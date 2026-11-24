from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateTagsRequest(BaseModel):
    ResourceName: StrictStr
    Tags: list[RedshiftTag]
