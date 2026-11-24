from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .wa_fv2_sampled_http_request import WAFv2SampledHTTPRequest
from .wa_fv2_time_window import WAFv2TimeWindow


class WAFv2GetSampledRequestsResponse(BaseModel):
    SampledRequests: list[WAFv2SampledHTTPRequest] | None = None
    PopulationSize: StrictInt | None = None
    TimeWindow: WAFv2TimeWindow | None = None
    ResponseMetadata: dict[str, Any] | None = None
