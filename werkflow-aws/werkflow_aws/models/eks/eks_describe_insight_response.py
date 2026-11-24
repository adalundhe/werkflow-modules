from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .eks_insight import EKSInsight


class EKSDescribeInsightResponse(BaseModel):
    insight: EKSInsight | None = None
    ResponseMetadata: dict[str, Any] | None = None
