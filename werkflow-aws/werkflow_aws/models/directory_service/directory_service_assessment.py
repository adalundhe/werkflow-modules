from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceAssessment(BaseModel):
    AssessmentId: StrictStr | None = None
    DirectoryId: StrictStr | None = None
    DnsName: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    LastUpdateDateTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    StatusCode: StrictStr | None = None
    StatusReason: StrictStr | None = None
    CustomerDnsIps: list[StrictStr] | None = None
    VpcId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    SelfManagedInstanceIds: list[StrictStr] | None = None
    ReportType: StrictStr | None = None
    Version: StrictStr | None = None
