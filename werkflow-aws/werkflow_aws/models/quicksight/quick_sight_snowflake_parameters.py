from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_o_auth_parameters import QuickSightOAuthParameters


class QuickSightSnowflakeParameters(BaseModel):
    Host: StrictStr | None = None
    Database: StrictStr | None = None
    Warehouse: StrictStr | None = None
    AuthenticationType: StrictStr | None = None
    DatabaseAccessControlRole: StrictStr | None = None
    OAuthParameters: QuickSightOAuthParameters | None = None
