from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_model_data_source_model import SageMakerModelDataSourceModel


class SageMakerSourceAlgorithm(BaseModel):
    ModelDataUrl: StrictStr | None = None
    ModelDataSource: SageMakerModelDataSourceModel | None = None
    ModelDataETag: StrictStr | None = None
    AlgorithmName: StrictStr | None = None
