from __future__ import annotations
from pydantic import BaseModel
from .ec2_key_pair_info import EC2KeyPairInfo


class EC2DescribeKeyPairsResponse(BaseModel):
    KeyPairs: list[EC2KeyPairInfo] | None = None
