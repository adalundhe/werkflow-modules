from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_notification_configuration_filter_input import AWSS3NotificationConfigurationFilterInput


class AWSS3LambdaFunctionConfigurationInput(BaseModel):
    LambdaFunctionArn: StrictStr
    Events: list[StrictStr]
    Id: StrictStr | None = None
    Filter: AWSS3NotificationConfigurationFilterInput | None = None
