from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .q_business_data_accessor_authentication_detail import QBusinessDataAccessorAuthenticationDetail


class QBusinessDataAccessor(BaseModel):
    displayName: StrictStr | None = None
    dataAccessorId: StrictStr | None = None
    dataAccessorArn: StrictStr | None = None
    idcApplicationArn: StrictStr | None = None
    principal: StrictStr | None = None
    authenticationDetail: QBusinessDataAccessorAuthenticationDetail | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
