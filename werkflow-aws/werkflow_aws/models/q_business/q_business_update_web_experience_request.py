from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_browser_extension_configuration import QBusinessBrowserExtensionConfiguration
from .q_business_customization_configuration import QBusinessCustomizationConfiguration
from .q_business_identity_provider_configuration import QBusinessIdentityProviderConfiguration
from .q_business_web_experience_auth_configuration import QBusinessWebExperienceAuthConfiguration


class QBusinessUpdateWebExperienceRequest(BaseModel):
    applicationId: StrictStr
    webExperienceId: StrictStr
    roleArn: StrictStr | None = None
    authenticationConfiguration: QBusinessWebExperienceAuthConfiguration | None = None
    title: StrictStr | None = None
    subtitle: StrictStr | None = None
    welcomeMessage: StrictStr | None = None
    samplePromptsControlMode: Literal['ENABLED', 'DISABLED'] | None = None
    identityProviderConfiguration: QBusinessIdentityProviderConfiguration | None = None
    origins: list[StrictStr] | None = None
    browserExtensionConfiguration: QBusinessBrowserExtensionConfiguration | None = None
    customizationConfiguration: QBusinessCustomizationConfiguration | None = None
