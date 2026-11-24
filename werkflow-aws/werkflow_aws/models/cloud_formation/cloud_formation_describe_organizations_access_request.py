from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class CloudFormationDescribeOrganizationsAccessRequest(BaseModel):
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None
