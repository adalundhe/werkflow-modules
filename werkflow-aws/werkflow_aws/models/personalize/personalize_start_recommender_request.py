from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeStartRecommenderRequest(BaseModel):
    recommenderArn: StrictStr
