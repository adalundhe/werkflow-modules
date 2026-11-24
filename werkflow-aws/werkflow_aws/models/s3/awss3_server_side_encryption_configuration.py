from __future__ import annotations
from pydantic import BaseModel
from .awss3_server_side_encryption_rule import AWSS3ServerSideEncryptionRule


class AWSS3ServerSideEncryptionConfiguration(BaseModel):
    Rules: list[AWSS3ServerSideEncryptionRule] | None = None
