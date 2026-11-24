from __future__ import annotations
from pydantic import BaseModel
from .q_business_open_id_connect_provider_configuration import QBusinessOpenIDConnectProviderConfiguration
from .q_business_saml_provider_configuration import QBusinessSamlProviderConfiguration


class QBusinessIdentityProviderConfiguration(BaseModel):
    samlConfiguration: QBusinessSamlProviderConfiguration | None = None
    openIDConnectConfiguration: QBusinessOpenIDConnectProviderConfiguration | None = None
