from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_replication_rule_and_operator import AWSS3ReplicationRuleAndOperator
from .awss3_replication_rule_not_operator import AWSS3ReplicationRuleNotOperator
from .awss3_tag_model import AWSS3TagModel


class AWSS3ReplicationRuleFilter(BaseModel):
    Prefix: StrictStr | None = None
    Tag: AWSS3TagModel | None = None
    And: AWSS3ReplicationRuleAndOperator | None = None
    Not: AWSS3ReplicationRuleNotOperator | None = None
