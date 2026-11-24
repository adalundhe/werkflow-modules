from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_data_source import SageMakerAutoMLDataSource


class SageMakerAutoMLJobChannel(BaseModel):
    ChannelType: StrictStr | None = None
    ContentType: StrictStr | None = None
    CompressionType: StrictStr | None = None
    DataSource: SageMakerAutoMLDataSource | None = None
