from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class RedshiftDescribeIntegrationsFilter(BaseModel):
    Name: Literal['integration-arn', 'source-arn', 'source-types', 'status']
    Values: list[StrictStr]
