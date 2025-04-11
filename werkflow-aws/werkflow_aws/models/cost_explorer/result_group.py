from pydantic import BaseModel, StrictStr
from .metric import Metric


class ResultGroup(BaseModel):
    Keys: list[StrictStr]
    Metrics: dict[StrictStr, Metric]