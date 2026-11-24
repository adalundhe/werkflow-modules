from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_applied_attachments_configuration import QBusinessAppliedAttachmentsConfiguration
from .q_business_auto_subscription_configuration import QBusinessAutoSubscriptionConfiguration
from .q_business_encryption_configuration import QBusinessEncryptionConfiguration
from .q_business_error_detail import QBusinessErrorDetail
from .q_business_personalization_configuration import QBusinessPersonalizationConfiguration
from .q_business_q_apps_configuration import QBusinessQAppsConfiguration
from .q_business_quick_sight_configuration import QBusinessQuickSightConfiguration


class QBusinessGetApplicationResponse(BaseModel):
    displayName: StrictStr | None = None
    applicationId: StrictStr | None = None
    applicationArn: StrictStr | None = None
    identityType: StrictStr | None = None
    iamIdentityProviderArn: StrictStr | None = None
    identityCenterApplicationArn: StrictStr | None = None
    roleArn: StrictStr | None = None
    status: StrictStr | None = None
    description: StrictStr | None = None
    encryptionConfiguration: QBusinessEncryptionConfiguration | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    error: QBusinessErrorDetail | None = None
    attachmentsConfiguration: QBusinessAppliedAttachmentsConfiguration | None = None
    qAppsConfiguration: QBusinessQAppsConfiguration | None = None
    personalizationConfiguration: QBusinessPersonalizationConfiguration | None = None
    autoSubscriptionConfiguration: QBusinessAutoSubscriptionConfiguration | None = None
    clientIdsForOIDC: list[StrictStr] | None = None
    quickSightConfiguration: QBusinessQuickSightConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
