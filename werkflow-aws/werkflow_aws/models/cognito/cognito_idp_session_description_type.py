from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .cognito_idp_session_location_type import CognitoIDPSessionLocationType


class CognitoIDPSessionDescriptionType(BaseModel):
    SessionId: StrictStr | None = None
    SessionType: StrictStr | None = None
    ClientId: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    LastActiveDate: datetime.datetime | StrictStr | None = None
    DeviceType: StrictStr | None = None
    LastIPAddress: StrictStr | None = None
    LastLocation: CognitoIDPSessionLocationType | None = None
    OriginSessionId: StrictStr | None = None
    IsCurrentSession: StrictBool | None = None
