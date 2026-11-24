from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .firehose_authentication_configuration import FirehoseAuthenticationConfiguration


class FirehoseMSKSourceDescription(BaseModel):
    MSKClusterARN: StrictStr | None = None
    TopicName: StrictStr | None = None
    AuthenticationConfiguration: FirehoseAuthenticationConfiguration | None = None
    DeliveryStartTimestamp: datetime.datetime | StrictStr | None = None
    ReadFromTimestamp: datetime.datetime | StrictStr | None = None
