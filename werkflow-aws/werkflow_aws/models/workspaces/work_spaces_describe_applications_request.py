from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class WorkSpacesDescribeApplicationsRequest(BaseModel):
    ApplicationIds: list[StrictStr] | None = None
    ComputeTypeNames: list[Literal['VALUE', 'STANDARD', 'PERFORMANCE', 'POWER', 'GRAPHICS', 'POWERPRO', 'GENERALPURPOSE_4XLARGE', 'GENERALPURPOSE_8XLARGE', 'GRAPHICSPRO', 'GRAPHICS_G4DN', 'GRAPHICSPRO_G4DN', 'GRAPHICS_G6_XLARGE', 'GRAPHICS_G6_2XLARGE', 'GRAPHICS_G6_4XLARGE', 'GRAPHICS_G6_8XLARGE', 'GRAPHICS_G6_16XLARGE', 'GRAPHICS_GR6_4XLARGE', 'GRAPHICS_GR6_8XLARGE', 'GRAPHICS_G6F_LARGE', 'GRAPHICS_G6F_XLARGE', 'GRAPHICS_G6F_2XLARGE', 'GRAPHICS_G6F_4XLARGE', 'GRAPHICS_GR6F_4XLARGE', 'GRAPHICS_G7_2XLARGE', 'GRAPHICS_G7_4XLARGE', 'GRAPHICS_G7_8XLARGE', 'GRAPHICS_G7_12XLARGE']] | None = None
    LicenseType: Literal['LICENSED', 'UNLICENSED'] | None = None
    OperatingSystemNames: list[Literal['AMAZON_LINUX_2', 'UBUNTU_18_04', 'UBUNTU_20_04', 'UBUNTU_22_04', 'UNKNOWN', 'WINDOWS_10', 'WINDOWS_11', 'WINDOWS_7', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022', 'WINDOWS_SERVER_2025', 'RHEL_8', 'ROCKY_8', 'UBUNTU_24_04', 'RHEL_9', 'ROCKY_9', 'UBUNTU_26_04', 'RHEL_10', 'ROCKY_10']] | None = None
    Owner: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
