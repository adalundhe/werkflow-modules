from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SESPutConfigurationSetTrackingOptionsRequest(BaseModel):
    ConfigurationSetName: StrictStr
    CustomRedirectDomain: StrictStr | None = None
    HttpsPolicy: Literal['REQUIRE', 'REQUIRE_OPEN_ONLY', 'OPTIONAL'] | None = None
