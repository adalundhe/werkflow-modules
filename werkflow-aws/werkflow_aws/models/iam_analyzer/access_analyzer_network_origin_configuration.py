from __future__ import annotations
from pydantic import BaseModel
from .access_analyzer_internet_configuration import AccessAnalyzerInternetConfiguration
from .access_analyzer_vpc_configuration import AccessAnalyzerVpcConfiguration


class AccessAnalyzerNetworkOriginConfiguration(BaseModel):
    vpcConfiguration: AccessAnalyzerVpcConfiguration | None = None
    internetConfiguration: AccessAnalyzerInternetConfiguration | None = None
