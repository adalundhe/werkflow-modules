from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_o_auth_parameters import QuickSightOAuthParameters


class QuickSightStarburstParameters(BaseModel):
    Host: StrictStr | None = None
    Port: StrictInt | None = None
    Catalog: StrictStr | None = None
    ProductType: StrictStr | None = None
    DatabaseAccessControlRole: StrictStr | None = None
    AuthenticationType: StrictStr | None = None
    OAuthParameters: QuickSightOAuthParameters | None = None
