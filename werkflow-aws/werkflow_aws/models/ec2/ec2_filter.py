from pydantic import BaseModel, StrictStr
from typing import Literal

EC2Filters = Literal[
    "attachment.attach-time",
    "attachment.delete-on-termination",
    "attachment.device",
    "attachment.instance-id",
    "attachment.status",
    "availability-zone",
    "create-time",
    "encrypted",
    "fast-restored",
    "multi-attach-enabled",
    "operator.managed",
    "operator.principal",
    "size",
    "snapshot-id",
    "status",
    "tag",
    "tag-key",
    "volume-id",
    "volume-type"
]


class EC2Filter(BaseModel):
    Name: EC2Filters
    Value: list[StrictStr]