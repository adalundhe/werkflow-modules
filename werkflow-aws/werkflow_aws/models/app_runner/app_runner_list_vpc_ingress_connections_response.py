from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_runner_vpc_ingress_connection_summary import AppRunnerVpcIngressConnectionSummary


class AppRunnerListVpcIngressConnectionsResponse(BaseModel):
    VpcIngressConnectionSummaryList: list[AppRunnerVpcIngressConnectionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
