from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_sampling_statistic_summary import XRaySamplingStatisticSummary


class XRayGetSamplingStatisticSummariesResponse(BaseModel):
    SamplingStatisticSummaries: list[XRaySamplingStatisticSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
