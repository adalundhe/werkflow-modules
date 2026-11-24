from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_action_configuration import QBusinessActionConfiguration
from .q_business_data_accessor_authentication_detail import QBusinessDataAccessorAuthenticationDetail


class QBusinessGetDataAccessorResponse(BaseModel):
    displayName: StrictStr | None = None
    dataAccessorId: StrictStr | None = None
    dataAccessorArn: StrictStr | None = None
    applicationId: StrictStr | None = None
    idcApplicationArn: StrictStr | None = None
    principal: StrictStr | None = None
    actionConfigurations: list[QBusinessActionConfiguration] | None = None
    authenticationDetail: QBusinessDataAccessorAuthenticationDetail | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
