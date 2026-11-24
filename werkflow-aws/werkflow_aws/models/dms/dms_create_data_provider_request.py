from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .dms_data_provider_settings import DMSDataProviderSettings
from .dms_tag import DMSTag


class DMSCreateDataProviderRequest(BaseModel):
    Engine: StrictStr
    Settings: DMSDataProviderSettings
    DataProviderName: StrictStr | None = None
    Description: StrictStr | None = None
    Virtual: StrictBool | None = None
    Tags: list[DMSTag] | None = None
