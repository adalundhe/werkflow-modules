from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .ses_domain_isp_placement import SESDomainIspPlacement
from .ses_volume_statistics import SESVolumeStatistics


class SESOverallVolume(BaseModel):
    VolumeStatistics: SESVolumeStatistics | None = None
    ReadRatePercent: StrictFloat | StrictInt | None = None
    DomainIspPlacements: list[SESDomainIspPlacement] | None = None
