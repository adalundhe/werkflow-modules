from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_authorized_token_issuer import RedshiftAuthorizedTokenIssuer
from .redshift_service_integrations_union import RedshiftServiceIntegrationsUnion
from .redshift_tag import RedshiftTag


class RedshiftIdcApplication(BaseModel):
    IdcInstanceArn: StrictStr | None = None
    RedshiftIdcApplicationName: StrictStr | None = None
    RedshiftIdcApplicationArn: StrictStr | None = None
    IdentityNamespace: StrictStr | None = None
    IdcDisplayName: StrictStr | None = None
    IamRoleArn: StrictStr | None = None
    IdcManagedApplicationArn: StrictStr | None = None
    IdcOnboardStatus: StrictStr | None = None
    AuthorizedTokenIssuerList: list[RedshiftAuthorizedTokenIssuer] | None = None
    ServiceIntegrations: list[RedshiftServiceIntegrationsUnion] | None = None
    ApplicationType: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
    SsoTagKeys: list[StrictStr] | None = None
