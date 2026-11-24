from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_deliverability_test_report import SESDeliverabilityTestReport
from .ses_isp_placement import SESIspPlacement
from .ses_placement_statistics import SESPlacementStatistics
from .ses_tag import SESTag


class SESGetDeliverabilityTestReportResponse(BaseModel):
    DeliverabilityTestReport: SESDeliverabilityTestReport | None = None
    OverallPlacement: SESPlacementStatistics | None = None
    IspPlacements: list[SESIspPlacement] | None = None
    Message: StrictStr | None = None
    Tags: list[SESTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
