from __future__ import annotations
from pydantic import BaseModel
from .connect_recommender_config import ConnectRecommenderConfig


class ConnectContentAttributes(BaseModel):
    RecommenderConfig: ConnectRecommenderConfig | None = None
