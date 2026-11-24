from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_read_authentication_metadata import QuickSightReadAuthenticationMetadata


class QuickSightReadAuthConfig(BaseModel):
    AuthenticationType: StrictStr | None = None
    AuthenticationMetadata: QuickSightReadAuthenticationMetadata | None = None
