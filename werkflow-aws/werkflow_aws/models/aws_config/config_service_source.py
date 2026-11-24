from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_custom_policy_details import ConfigServiceCustomPolicyDetails
from .config_service_source_detail import ConfigServiceSourceDetail


class ConfigServiceSource(BaseModel):
    Owner: StrictStr | None = None
    SourceIdentifier: StrictStr | None = None
    SourceDetails: list[ConfigServiceSourceDetail] | None = None
    CustomPolicyDetails: ConfigServiceCustomPolicyDetails | None = None
