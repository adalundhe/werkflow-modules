from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_vpc_endpoint_detail import OpenSearchServerlessVpcEndpointDetail
from .open_search_serverless_vpc_endpoint_error_detail import OpenSearchServerlessVpcEndpointErrorDetail


class OpenSearchServerlessBatchGetVpcEndpointResponse(BaseModel):
    vpcEndpointDetails: list[OpenSearchServerlessVpcEndpointDetail] | None = None
    vpcEndpointErrorDetails: list[OpenSearchServerlessVpcEndpointErrorDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
