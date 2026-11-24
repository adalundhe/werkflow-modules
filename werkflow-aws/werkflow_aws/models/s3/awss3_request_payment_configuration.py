from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class AWSS3RequestPaymentConfiguration(BaseModel):
    Payer: Literal['Requester', 'BucketOwner']
