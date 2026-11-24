from __future__ import annotations
from pydantic import BaseModel
from .ssms3_output_url import SSMS3OutputUrl


class SSMInstanceAssociationOutputUrl(BaseModel):
    S3OutputUrl: SSMS3OutputUrl | None = None
