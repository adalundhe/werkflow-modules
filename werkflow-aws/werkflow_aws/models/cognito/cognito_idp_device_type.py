from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cognito_idp_attribute_type import CognitoIDPAttributeType


class CognitoIDPDeviceType(BaseModel):
    DeviceKey: StrictStr | None = None
    DeviceAttributes: list[CognitoIDPAttributeType] | None = None
    DeviceCreateDate: datetime.datetime | StrictStr | None = None
    DeviceLastModifiedDate: datetime.datetime | StrictStr | None = None
    DeviceLastAuthenticatedDate: datetime.datetime | StrictStr | None = None
