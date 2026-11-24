from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_non_compliant_resource import IoTNonCompliantResource
from .io_t_related_resource import IoTRelatedResource


class IoTAuditFinding(BaseModel):
    findingId: StrictStr | None = None
    taskId: StrictStr | None = None
    checkName: StrictStr | None = None
    taskStartTime: datetime.datetime | StrictStr | None = None
    findingTime: datetime.datetime | StrictStr | None = None
    severity: StrictStr | None = None
    nonCompliantResource: IoTNonCompliantResource | None = None
    relatedResources: list[IoTRelatedResource] | None = None
    reasonForNonCompliance: StrictStr | None = None
    reasonForNonComplianceCode: StrictStr | None = None
    isSuppressed: StrictBool | None = None
