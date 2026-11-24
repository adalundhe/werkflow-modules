from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_vpc_endpoint_summary import OpenSearchVpcEndpointSummary


class OpenSearchListVpcEndpointsForDomainResponse(BaseModel):
    VpcEndpointSummaryList: list[OpenSearchVpcEndpointSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
