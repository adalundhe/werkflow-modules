from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_attachments_configuration import QBusinessAttachmentsConfiguration
from .q_business_encryption_configuration import QBusinessEncryptionConfiguration
from .q_business_personalization_configuration import QBusinessPersonalizationConfiguration
from .q_business_q_apps_configuration import QBusinessQAppsConfiguration
from .q_business_quick_sight_configuration import QBusinessQuickSightConfiguration
from .q_business_tag import QBusinessTag


class QBusinessCreateApplicationRequest(BaseModel):
    displayName: StrictStr
    roleArn: StrictStr | None = None
    identityType: Literal['AWS_IAM_IDP_SAML', 'AWS_IAM_IDP_OIDC', 'AWS_IAM_IDC', 'AWS_QUICKSIGHT_IDP', 'ANONYMOUS'] | None = None
    iamIdentityProviderArn: StrictStr | None = None
    identityCenterInstanceArn: StrictStr | None = None
    clientIdsForOIDC: list[StrictStr] | None = None
    description: StrictStr | None = None
    encryptionConfiguration: QBusinessEncryptionConfiguration | None = None
    tags: list[QBusinessTag] | None = None
    clientToken: StrictStr | None = None
    attachmentsConfiguration: QBusinessAttachmentsConfiguration | None = None
    qAppsConfiguration: QBusinessQAppsConfiguration | None = None
    personalizationConfiguration: QBusinessPersonalizationConfiguration | None = None
    quickSightConfiguration: QBusinessQuickSightConfiguration | None = None
