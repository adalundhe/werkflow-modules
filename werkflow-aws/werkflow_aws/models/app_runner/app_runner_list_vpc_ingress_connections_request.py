from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .app_runner_list_vpc_ingress_connections_filter import AppRunnerListVpcIngressConnectionsFilter


class AppRunnerListVpcIngressConnectionsRequest(BaseModel):
    Filter: AppRunnerListVpcIngressConnectionsFilter | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
