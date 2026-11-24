from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_unprocessed_data_sources_result import GuardDutyUnprocessedDataSourcesResult


class GuardDutyCreateDetectorResponse(BaseModel):
    DetectorId: StrictStr | None = None
    UnprocessedDataSources: GuardDutyUnprocessedDataSourcesResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
