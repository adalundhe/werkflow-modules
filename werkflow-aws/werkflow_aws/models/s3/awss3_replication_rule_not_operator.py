from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_replication_rule_or_operator import AWSS3ReplicationRuleOrOperator
from .awss3_tag_model import AWSS3TagModel


class AWSS3ReplicationRuleNotOperator(BaseModel):
    Prefix: StrictStr | None = None
    Tag: AWSS3TagModel | None = None
    Or: AWSS3ReplicationRuleOrOperator | None = None
