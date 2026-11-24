from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .redshift_authorized_token_issuer import RedshiftAuthorizedTokenIssuer
from .redshift_service_integrations_union import RedshiftServiceIntegrationsUnion
from .redshift_tag import RedshiftTag


class RedshiftCreateRedshiftIdcApplicationRequest(BaseModel):
    IdcInstanceArn: StrictStr
    RedshiftIdcApplicationName: StrictStr
    IdcDisplayName: StrictStr
    IamRoleArn: StrictStr
    IdentityNamespace: StrictStr | None = None
    AuthorizedTokenIssuerList: list[RedshiftAuthorizedTokenIssuer] | None = None
    ServiceIntegrations: list[RedshiftServiceIntegrationsUnion] | None = None
    ApplicationType: Literal['None', 'Lakehouse'] | None = None
    Tags: list[RedshiftTag] | None = None
    SsoTagKeys: list[StrictStr] | None = None
