from __future__ import annotations
from pydantic import BaseModel
from .ecr_replication_rule import ECRReplicationRule


class ECRReplicationConfiguration(BaseModel):
    rules: list[ECRReplicationRule] | None = None
