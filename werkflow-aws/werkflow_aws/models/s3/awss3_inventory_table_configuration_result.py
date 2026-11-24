from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_error_details import AWSS3ErrorDetails


class AWSS3InventoryTableConfigurationResult(BaseModel):
    ConfigurationState: StrictStr | None = None
    TableStatus: StrictStr | None = None
    Error: AWSS3ErrorDetails | None = None
    TableName: StrictStr | None = None
    TableArn: StrictStr | None = None
