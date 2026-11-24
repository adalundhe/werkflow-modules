from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_filter import EC2Filter


class EC2DescribeKeyPairsRequest(BaseModel):
    KeyNames: list[StrictStr] | None = None
    KeyPairIds: list[StrictStr] | None = None
    IncludePublicKey: StrictBool | None = None
    Filters: list[EC2Filter] | None = None
    DryRun: StrictBool | None = None
