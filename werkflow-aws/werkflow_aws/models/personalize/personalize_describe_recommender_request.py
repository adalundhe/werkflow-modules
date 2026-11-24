from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeRecommenderRequest(BaseModel):
    recommenderArn: StrictStr
