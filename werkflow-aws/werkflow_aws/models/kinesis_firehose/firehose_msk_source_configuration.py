from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .firehose_authentication_configuration import FirehoseAuthenticationConfiguration


class FirehoseMSKSourceConfiguration(BaseModel):
    MSKClusterARN: StrictStr
    TopicName: StrictStr
    AuthenticationConfiguration: FirehoseAuthenticationConfiguration
    ReadFromTimestamp: datetime.datetime | StrictStr | None = None
