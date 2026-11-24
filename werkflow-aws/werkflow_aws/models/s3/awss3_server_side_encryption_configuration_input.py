from __future__ import annotations
from pydantic import BaseModel
from .awss3_server_side_encryption_rule_input import AWSS3ServerSideEncryptionRuleInput


class AWSS3ServerSideEncryptionConfigurationInput(BaseModel):
    Rules: list[AWSS3ServerSideEncryptionRuleInput]
