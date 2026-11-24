from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_extraction_configuration import ConnectExtractionConfiguration
from .connect_extraction_definition_display import ConnectExtractionDefinitionDisplay


class ConnectCreateExtractionDefinitionRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    ExtractionConfiguration: ConnectExtractionConfiguration
    ClientToken: StrictStr | None = None
    Display: ConnectExtractionDefinitionDisplay | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
