from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_data_accessor_authentication_configuration import QBusinessDataAccessorAuthenticationConfiguration


class QBusinessDataAccessorAuthenticationDetail(BaseModel):
    authenticationType: StrictStr | None = None
    authenticationConfiguration: QBusinessDataAccessorAuthenticationConfiguration | None = None
    externalIds: list[StrictStr] | None = None
