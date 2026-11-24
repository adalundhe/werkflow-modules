from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftEC2SecurityGroup(BaseModel):
    Status: StrictStr | None = None
    EC2SecurityGroupName: StrictStr | None = None
    EC2SecurityGroupOwnerId: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
