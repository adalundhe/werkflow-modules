from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightS3TablesParameters(BaseModel):
    TableBucketArn: StrictStr | None = None
