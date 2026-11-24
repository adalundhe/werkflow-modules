from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_error_details import AWSS3ErrorDetails
from .awss3_record_expiration import AWSS3RecordExpiration


class AWSS3JournalTableConfigurationResult(BaseModel):
    TableStatus: StrictStr | None = None
    Error: AWSS3ErrorDetails | None = None
    TableName: StrictStr | None = None
    TableArn: StrictStr | None = None
    RecordExpiration: AWSS3RecordExpiration | None = None
