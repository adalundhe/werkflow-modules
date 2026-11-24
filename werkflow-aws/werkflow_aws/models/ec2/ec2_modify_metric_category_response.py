from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_metric_category import EC2MetricCategory


class EC2ModifyMetricCategoryResponse(BaseModel):
    MetricCategory: EC2MetricCategory | None = None
    ResponseMetadata: dict[str, Any] | None = None
