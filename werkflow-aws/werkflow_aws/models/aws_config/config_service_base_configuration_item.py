from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceBaseConfigurationItem(BaseModel):
    version: StrictStr | None = None
    accountId: StrictStr | None = None
    configurationItemCaptureTime: datetime.datetime | StrictStr | None = None
    configurationItemStatus: StrictStr | None = None
    configurationStateId: StrictStr | None = None
    arn: StrictStr | None = None
    resourceType: StrictStr | None = None
    resourceId: StrictStr | None = None
    resourceName: StrictStr | None = None
    awsRegion: StrictStr | None = None
    availabilityZone: StrictStr | None = None
    resourceCreationTime: datetime.datetime | StrictStr | None = None
    configuration: StrictStr | None = None
    supplementaryConfiguration: dict[StrictStr, StrictStr] | None = None
    recordingFrequency: StrictStr | None = None
    configurationItemDeliveryTime: datetime.datetime | StrictStr | None = None
