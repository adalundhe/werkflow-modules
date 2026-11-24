from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .comprehend_dataset_input_data_config import ComprehendDatasetInputDataConfig
from .comprehend_tag import ComprehendTag


class ComprehendCreateDatasetRequest(BaseModel):
    FlywheelArn: StrictStr
    DatasetName: StrictStr
    InputDataConfig: ComprehendDatasetInputDataConfig
    DatasetType: Literal['TRAIN', 'TEST'] | None = None
    Description: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
    Tags: list[ComprehendTag] | None = None
