from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CloudWatchLogsDeliverySourceConfigurationSchema(BaseModel):
    keyName: StrictStr | None = None
    valueType: StrictStr | None = None
    defaultValue: StrictStr | None = None
    supportedValues: list[StrictStr] | None = None
    minValue: StrictFloat | StrictInt | None = None
    maxValue: StrictFloat | StrictInt | None = None
