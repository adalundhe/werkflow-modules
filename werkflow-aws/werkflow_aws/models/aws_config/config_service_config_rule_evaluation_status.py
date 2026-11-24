from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class ConfigServiceConfigRuleEvaluationStatus(BaseModel):
    ConfigRuleName: StrictStr | None = None
    ConfigRuleArn: StrictStr | None = None
    ConfigRuleId: StrictStr | None = None
    LastSuccessfulInvocationTime: datetime.datetime | StrictStr | None = None
    LastFailedInvocationTime: datetime.datetime | StrictStr | None = None
    LastSuccessfulEvaluationTime: datetime.datetime | StrictStr | None = None
    LastFailedEvaluationTime: datetime.datetime | StrictStr | None = None
    FirstActivatedTime: datetime.datetime | StrictStr | None = None
    LastDeactivatedTime: datetime.datetime | StrictStr | None = None
    LastErrorCode: StrictStr | None = None
    LastErrorMessage: StrictStr | None = None
    FirstEvaluationStarted: StrictBool | None = None
    LastDebugLogDeliveryStatus: StrictStr | None = None
    LastDebugLogDeliveryStatusReason: StrictStr | None = None
    LastDebugLogDeliveryTime: datetime.datetime | StrictStr | None = None
