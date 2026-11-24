from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class PersonalizeCreateDatasetGroupResponse(BaseModel):
    datasetGroupArn: StrictStr | None = None
    domain: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
