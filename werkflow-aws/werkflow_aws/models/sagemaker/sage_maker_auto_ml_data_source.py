from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_auto_mls3_data_source import SageMakerAutoMLS3DataSource


class SageMakerAutoMLDataSource(BaseModel):
    S3DataSource: SageMakerAutoMLS3DataSource | None = None
