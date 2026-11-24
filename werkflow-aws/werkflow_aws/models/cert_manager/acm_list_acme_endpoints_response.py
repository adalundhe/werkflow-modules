from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .acme_endpoint_summary import AcmeEndpointSummary


class ACMListAcmeEndpointsResponse(BaseModel):
    AcmeEndpoints: list[AcmeEndpointSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
