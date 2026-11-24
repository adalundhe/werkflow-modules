from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .athena_tag_model import AthenaTagModel


class AthenaCreateSystemTableConfigurationRequest(BaseModel):
    TableName: Literal['ALL']
    ClientRequestToken: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    Tags: list[AthenaTagModel] | None = None
