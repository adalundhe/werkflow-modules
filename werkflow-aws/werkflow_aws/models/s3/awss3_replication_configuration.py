from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_replication_rule import AWSS3ReplicationRule


class AWSS3ReplicationConfiguration(BaseModel):
    Role: StrictStr | None = None
    Rules: list[AWSS3ReplicationRule] | None = None
