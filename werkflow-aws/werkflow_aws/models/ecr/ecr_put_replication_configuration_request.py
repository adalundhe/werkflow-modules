from __future__ import annotations
from pydantic import BaseModel
from .ecr_replication_configuration import ECRReplicationConfiguration


class ECRPutReplicationConfigurationRequest(BaseModel):
    replicationConfiguration: ECRReplicationConfiguration
