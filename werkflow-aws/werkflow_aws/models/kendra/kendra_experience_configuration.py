from __future__ import annotations
from pydantic import BaseModel
from .kendra_content_source_configuration import KendraContentSourceConfiguration
from .kendra_user_identity_configuration import KendraUserIdentityConfiguration


class KendraExperienceConfiguration(BaseModel):
    ContentSourceConfiguration: KendraContentSourceConfiguration | None = None
    UserIdentityConfiguration: KendraUserIdentityConfiguration | None = None
