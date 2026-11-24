from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .dms_data_provider_settings import DMSDataProviderSettings


class DMSModifyDataProviderRequest(BaseModel):
    DataProviderIdentifier: StrictStr
    DataProviderName: StrictStr | None = None
    Description: StrictStr | None = None
    Engine: StrictStr | None = None
    Virtual: StrictBool | None = None
    ExactSettings: StrictBool | None = None
    Settings: DMSDataProviderSettings | None = None
