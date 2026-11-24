from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class BedrockPutAccountDataRetentionRequest(BaseModel):
    mode: Literal['default', 'none', 'aws_review', 'provider_data_share', 'inherit']
