from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_action_configuration import QBusinessActionConfiguration
from .q_business_data_accessor_authentication_detail import QBusinessDataAccessorAuthenticationDetail


class QBusinessUpdateDataAccessorRequest(BaseModel):
    applicationId: StrictStr
    dataAccessorId: StrictStr
    actionConfigurations: list[QBusinessActionConfiguration]
    authenticationDetail: QBusinessDataAccessorAuthenticationDetail | None = None
    displayName: StrictStr | None = None
