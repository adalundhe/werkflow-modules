from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_attachments_configuration import QBusinessAttachmentsConfiguration
from .q_business_auto_subscription_configuration import QBusinessAutoSubscriptionConfiguration
from .q_business_personalization_configuration import QBusinessPersonalizationConfiguration
from .q_business_q_apps_configuration import QBusinessQAppsConfiguration


class QBusinessUpdateApplicationRequest(BaseModel):
    applicationId: StrictStr
    identityCenterInstanceArn: StrictStr | None = None
    displayName: StrictStr | None = None
    description: StrictStr | None = None
    roleArn: StrictStr | None = None
    attachmentsConfiguration: QBusinessAttachmentsConfiguration | None = None
    qAppsConfiguration: QBusinessQAppsConfiguration | None = None
    personalizationConfiguration: QBusinessPersonalizationConfiguration | None = None
    autoSubscriptionConfiguration: QBusinessAutoSubscriptionConfiguration | None = None
