from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class EC2AthenaIntegration(BaseModel):
    IntegrationResultS3DestinationArn: StrictStr
    PartitionLoadFrequency: Literal['none', 'daily', 'weekly', 'monthly']
    PartitionStartDate: datetime.datetime | StrictStr | None = None
    PartitionEndDate: datetime.datetime | StrictStr | None = None
