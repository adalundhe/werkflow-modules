from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_notification_configuration_filter import AWSS3NotificationConfigurationFilter


class AWSS3LambdaFunctionConfiguration(BaseModel):
    Id: StrictStr | None = None
    LambdaFunctionArn: StrictStr | None = None
    Events: list[StrictStr] | None = None
    Filter: AWSS3NotificationConfigurationFilter | None = None
