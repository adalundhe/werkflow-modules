from __future__ import annotations
from pydantic import BaseModel
from .ec2_target_group import EC2TargetGroup


class EC2TargetGroupsConfig(BaseModel):
    TargetGroups: list[EC2TargetGroup] | None = None
