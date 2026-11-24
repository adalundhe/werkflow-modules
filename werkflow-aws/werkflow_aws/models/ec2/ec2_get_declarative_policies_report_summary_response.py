from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_attribute_summary import EC2AttributeSummary


class EC2GetDeclarativePoliciesReportSummaryResponse(BaseModel):
    ReportId: StrictStr | None = None
    S3Bucket: StrictStr | None = None
    S3Prefix: StrictStr | None = None
    TargetId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    NumberOfAccounts: StrictInt | None = None
    NumberOfFailedAccounts: StrictInt | None = None
    AttributeSummaries: list[EC2AttributeSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
