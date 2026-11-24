from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .dms_data_provider_settings import DMSDataProviderSettings


class DMSDataProvider(BaseModel):
    DataProviderName: StrictStr | None = None
    DataProviderArn: StrictStr | None = None
    DataProviderCreationTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    Engine: StrictStr | None = None
    Virtual: StrictBool | None = None
    Settings: DMSDataProviderSettings | None = None
