from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_registered_instance import EC2RegisteredInstance


class EC2EnableInstanceSqlHaStandbyDetectionsResponse(BaseModel):
    Instances: list[EC2RegisteredInstance] | None = None
    ResponseMetadata: dict[str, Any] | None = None
