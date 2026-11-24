from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_action_configuration import QBusinessActionConfiguration
from .q_business_data_accessor_authentication_detail import QBusinessDataAccessorAuthenticationDetail
from .q_business_tag import QBusinessTag


class QBusinessCreateDataAccessorRequest(BaseModel):
    applicationId: StrictStr
    principal: StrictStr
    actionConfigurations: list[QBusinessActionConfiguration]
    displayName: StrictStr
    clientToken: StrictStr | None = None
    authenticationDetail: QBusinessDataAccessorAuthenticationDetail | None = None
    tags: list[QBusinessTag] | None = None
