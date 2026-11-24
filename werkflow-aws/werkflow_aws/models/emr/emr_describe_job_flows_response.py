from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .emr_job_flow_detail import EMRJobFlowDetail


class EMRDescribeJobFlowsResponse(BaseModel):
    JobFlows: list[EMRJobFlowDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
