from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_metric_category import EC2MetricCategory


class EC2DescribeMetricCategoriesResponse(BaseModel):
    MetricCategories: list[EC2MetricCategory] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
