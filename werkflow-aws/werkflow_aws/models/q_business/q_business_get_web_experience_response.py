from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_browser_extension_configuration import QBusinessBrowserExtensionConfiguration
from .q_business_customization_configuration import QBusinessCustomizationConfiguration
from .q_business_error_detail import QBusinessErrorDetail
from .q_business_identity_provider_configuration import QBusinessIdentityProviderConfiguration
from .q_business_web_experience_auth_configuration import QBusinessWebExperienceAuthConfiguration


class QBusinessGetWebExperienceResponse(BaseModel):
    applicationId: StrictStr | None = None
    webExperienceId: StrictStr | None = None
    webExperienceArn: StrictStr | None = None
    defaultEndpoint: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    title: StrictStr | None = None
    subtitle: StrictStr | None = None
    welcomeMessage: StrictStr | None = None
    samplePromptsControlMode: StrictStr | None = None
    origins: list[StrictStr] | None = None
    roleArn: StrictStr | None = None
    identityProviderConfiguration: QBusinessIdentityProviderConfiguration | None = None
    authenticationConfiguration: QBusinessWebExperienceAuthConfiguration | None = None
    error: QBusinessErrorDetail | None = None
    browserExtensionConfiguration: QBusinessBrowserExtensionConfiguration | None = None
    customizationConfiguration: QBusinessCustomizationConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
