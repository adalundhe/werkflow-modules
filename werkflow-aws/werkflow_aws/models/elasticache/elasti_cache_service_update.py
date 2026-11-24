from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class ElastiCacheServiceUpdate(BaseModel):
    ServiceUpdateName: StrictStr | None = None
    ServiceUpdateReleaseDate: datetime.datetime | StrictStr | None = None
    ServiceUpdateEndDate: datetime.datetime | StrictStr | None = None
    ServiceUpdateSeverity: StrictStr | None = None
    ServiceUpdateRecommendedApplyByDate: datetime.datetime | StrictStr | None = None
    ServiceUpdateStatus: StrictStr | None = None
    ServiceUpdateDescription: StrictStr | None = None
    ServiceUpdateType: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    AutoUpdateAfterRecommendedApplyByDate: StrictBool | None = None
    EstimatedUpdateTime: StrictStr | None = None
