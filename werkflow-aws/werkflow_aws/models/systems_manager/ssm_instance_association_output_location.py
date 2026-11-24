from __future__ import annotations
from pydantic import BaseModel
from .ssms3_output_location import SSMS3OutputLocation


class SSMInstanceAssociationOutputLocation(BaseModel):
    S3Location: SSMS3OutputLocation | None = None
