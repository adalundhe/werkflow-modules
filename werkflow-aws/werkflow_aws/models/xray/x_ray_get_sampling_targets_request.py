from __future__ import annotations
from pydantic import BaseModel
from .x_ray_sampling_boost_statistics_document import XRaySamplingBoostStatisticsDocument
from .x_ray_sampling_statistics_document import XRaySamplingStatisticsDocument


class XRayGetSamplingTargetsRequest(BaseModel):
    SamplingStatisticsDocuments: list[XRaySamplingStatisticsDocument]
    SamplingBoostStatisticsDocuments: list[XRaySamplingBoostStatisticsDocument] | None = None
