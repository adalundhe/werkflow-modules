from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class RekognitionProjectPolicy(BaseModel):
    ProjectArn: StrictStr | None = None
    PolicyName: StrictStr | None = None
    PolicyRevisionId: StrictStr | None = None
    PolicyDocument: StrictStr | None = None
    CreationTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
