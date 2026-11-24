from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_o_auth2_client_application import GlueOAuth2ClientApplication


class GlueOAuth2Properties(BaseModel):
    OAuth2GrantType: StrictStr | None = None
    OAuth2ClientApplication: GlueOAuth2ClientApplication | None = None
    TokenUrl: StrictStr | None = None
    TokenUrlParametersMap: dict[StrictStr, StrictStr] | None = None
