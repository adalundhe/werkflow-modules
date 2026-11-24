from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_declarative_policies_report import EC2DeclarativePoliciesReport


class EC2DescribeDeclarativePoliciesReportsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Reports: list[EC2DeclarativePoliciesReport] | None = None
    ResponseMetadata: dict[str, Any] | None = None
