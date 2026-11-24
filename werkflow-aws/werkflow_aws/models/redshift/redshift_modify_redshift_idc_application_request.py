from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_authorized_token_issuer import RedshiftAuthorizedTokenIssuer
from .redshift_service_integrations_union import RedshiftServiceIntegrationsUnion


class RedshiftModifyRedshiftIdcApplicationRequest(BaseModel):
    RedshiftIdcApplicationArn: StrictStr
    IdentityNamespace: StrictStr | None = None
    IamRoleArn: StrictStr | None = None
    IdcDisplayName: StrictStr | None = None
    AuthorizedTokenIssuerList: list[RedshiftAuthorizedTokenIssuer] | None = None
    ServiceIntegrations: list[RedshiftServiceIntegrationsUnion] | None = None
