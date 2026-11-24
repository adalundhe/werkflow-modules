from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_sampling_target_document import XRaySamplingTargetDocument
from .x_ray_unprocessed_statistics import XRayUnprocessedStatistics


class XRayGetSamplingTargetsResponse(BaseModel):
    SamplingTargetDocuments: list[XRaySamplingTargetDocument] | None = None
    LastRuleModification: datetime.datetime | StrictStr | None = None
    UnprocessedStatistics: list[XRayUnprocessedStatistics] | None = None
    UnprocessedBoostStatistics: list[XRayUnprocessedStatistics] | None = None
    ResponseMetadata: dict[str, Any] | None = None
