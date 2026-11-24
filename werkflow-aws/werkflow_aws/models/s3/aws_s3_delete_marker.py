import datetime
from typing import Dict, Literal
from pydantic import (
    BaseModel,
    StrictBool,
    StrictStr,
)


class AWSs3DeleteMarker(BaseModel):
    Owner: Dict[Literal['DisplayName', 'ID'], StrictStr] | None = None
    Key: StrictStr | None = None
    VersionId: StrictStr | None = None
    IsLatest: StrictBool | None = None
    LastModified: datetime.datetime | None = None
