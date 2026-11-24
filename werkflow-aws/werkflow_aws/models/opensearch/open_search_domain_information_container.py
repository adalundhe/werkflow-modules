from __future__ import annotations
from pydantic import BaseModel
from .open_search_aws_domain_information import OpenSearchAWSDomainInformation


class OpenSearchDomainInformationContainer(BaseModel):
    AWSDomainInformation: OpenSearchAWSDomainInformation | None = None
