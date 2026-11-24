from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueDDBELTCatalogAdditionalOptions(BaseModel):
    DynamodbExport: StrictStr | None = None
    DynamodbUnnestDDBJson: StrictBool | None = None
