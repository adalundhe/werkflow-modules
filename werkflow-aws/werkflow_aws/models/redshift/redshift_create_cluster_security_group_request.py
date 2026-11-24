from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateClusterSecurityGroupRequest(BaseModel):
    ClusterSecurityGroupName: StrictStr
    Description: StrictStr
    Tags: list[RedshiftTag] | None = None
