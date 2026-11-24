from __future__ import annotations
from pydantic import BaseModel
from .q_business_basic_auth_configuration import QBusinessBasicAuthConfiguration
from .q_business_idc_auth_configuration import QBusinessIdcAuthConfiguration
from .q_business_no_auth_configuration import QBusinessNoAuthConfiguration
from .q_business_o_auth2_client_credential_configuration import QBusinessOAuth2ClientCredentialConfiguration


class QBusinessPluginAuthConfiguration(BaseModel):
    basicAuthConfiguration: QBusinessBasicAuthConfiguration | None = None
    oAuth2ClientCredentialConfiguration: QBusinessOAuth2ClientCredentialConfiguration | None = None
    noAuthConfiguration: QBusinessNoAuthConfiguration | None = None
    idcAuthConfiguration: QBusinessIdcAuthConfiguration | None = None
