from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_transform_data_source import SageMakerTransformDataSource


class SageMakerTransformInput(BaseModel):
    DataSource: SageMakerTransformDataSource | None = None
    ContentType: StrictStr | None = None
    CompressionType: StrictStr | None = None
    SplitType: StrictStr | None = None
