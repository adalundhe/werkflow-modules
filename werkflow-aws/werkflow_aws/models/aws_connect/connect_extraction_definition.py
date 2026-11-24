from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_extraction_configuration import ConnectExtractionConfiguration
from .connect_extraction_definition_display import ConnectExtractionDefinitionDisplay


class ConnectExtractionDefinition(BaseModel):
    Name: StrictStr | None = None
    ExtractionDefinitionId: StrictStr | None = None
    ExtractionDefinitionArn: StrictStr | None = None
    ExtractionConfiguration: ConnectExtractionConfiguration | None = None
    Display: ConnectExtractionDefinitionDisplay | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedBy: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
