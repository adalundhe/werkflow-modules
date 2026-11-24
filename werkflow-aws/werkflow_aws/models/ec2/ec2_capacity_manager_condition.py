from __future__ import annotations
from pydantic import BaseModel
from .ec2_dimension_condition import EC2DimensionCondition


class EC2CapacityManagerCondition(BaseModel):
    DimensionCondition: EC2DimensionCondition | None = None
