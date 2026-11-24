from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class PersonalizeUpdateRecommenderResponse(BaseModel):
    recommenderArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
