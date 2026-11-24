from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ses_domain_isp_placement import SESDomainIspPlacement
from .ses_volume_statistics import SESVolumeStatistics


class SESDailyVolume(BaseModel):
    StartDate: datetime.datetime | StrictStr | None = None
    VolumeStatistics: SESVolumeStatistics | None = None
    DomainIspPlacements: list[SESDomainIspPlacement] | None = None
