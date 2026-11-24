from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_instance import ConnectInstance
from .connect_replication_configuration import ConnectReplicationConfiguration


class ConnectDescribeInstanceResponse(BaseModel):
    Instance: ConnectInstance | None = None
    ReplicationConfiguration: ConnectReplicationConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
