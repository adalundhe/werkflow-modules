from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .io_t_behavior import IoTBehavior
from .io_t_metric_value import IoTMetricValue
from .io_t_violation_event_additional_info import IoTViolationEventAdditionalInfo


class IoTActiveViolation(BaseModel):
    violationId: StrictStr | None = None
    thingName: StrictStr | None = None
    securityProfileName: StrictStr | None = None
    behavior: IoTBehavior | None = None
    lastViolationValue: IoTMetricValue | None = None
    violationEventAdditionalInfo: IoTViolationEventAdditionalInfo | None = None
    verificationState: StrictStr | None = None
    verificationStateDescription: StrictStr | None = None
    lastViolationTime: datetime.datetime | StrictStr | None = None
    violationStartTime: datetime.datetime | StrictStr | None = None
