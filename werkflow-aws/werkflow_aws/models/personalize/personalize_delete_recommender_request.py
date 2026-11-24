from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDeleteRecommenderRequest(BaseModel):
    recommenderArn: StrictStr
