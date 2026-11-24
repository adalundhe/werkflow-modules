from __future__ import annotations
from pydantic import BaseModel
from .ssm_instance_info import SSMInstanceInfo


class SSMNodeType(BaseModel):
    Instance: SSMInstanceInfo | None = None
