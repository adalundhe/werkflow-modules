from __future__ import annotations
from pydantic import BaseModel
from .awss3_stats import AWSS3Stats


class AWSS3StatsEvent(BaseModel):
    Details: AWSS3Stats | None = None
