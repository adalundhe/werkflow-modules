from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateClusterSubnetGroupRequest(BaseModel):
    ClusterSubnetGroupName: StrictStr
    Description: StrictStr
    SubnetIds: list[StrictStr]
    Tags: list[RedshiftTag] | None = None
