from enum import Enum
from typing import Literal

RegionName = Literal[
    'af-south-1',
    'ap-east-1',
    'ap-northeast-1',
    'ap-northeast-2',
    'ap-northeast-3',
    'ap-south-1',
    'ap-south-2',
    'ap-southeast-1',
    'ap-southeast-2',
    'ap-southeast-3',
    'ap-southeast-4',
    'ca-central-1',
    'eu-central-1',
    'eu-central-2',
    'eu-north-1',
    'eu-south-1',
    'eu-south-2',
    'eu-west-1',
    'eu-west-2',
    'eu-west-3',
    'il-central-1',
    'me-central-1',
    'me-south-1',
    'sa-east-1',
    'us-east-1',
    'us-east-2',
    'us-gov-east-1',
    'us-gov-west-1',
    'us-west-1',
    'us-west-2',
]


class AWSRegion(Enum):
    AF_SOUTH_1='af-south-1'
    AP_EAST_1='ap-east-1'
    AP_NORTHEAST_1='ap-northeast-1'
    AP_NORTHEAST_2='ap-northeast-2'
    AP_NORTHEAST_3='ap-northeast-3'
    AP_SOUTH_1='ap-south-1'
    AP_SOUTH_2='ap-south-2'
    AP_SOUTHEAST_1='ap-southeast-1'
    AP_SOUTHEAST_2='ap-southeast-2'
    AP_SOUTHEAST_3='ap-southeast-3'
    AP_SOUTHEAST_4='ap-southeast-4'
    CA_CENTRAL_1='ca-central-1'
    EU_CENTRAL_1='eu-central-1'
    EU_CENTRAL_2='eu-central-2'
    EU_NORTH_1='eu-north-1'
    EU_SOUTH_1='eu-south-1'
    EU_SOUTH_2='eu-south-2'
    EU_WEST_1='eu-west-1'
    EU_WEST_2='eu-west-2'
    EU_WEST_3='eu-west-3'
    IL_CENTRAL_1='il-central-1'
    ME_CENTRAL_1='me-central-1'
    ME_SOUTH_1='me-south-1'
    SA_EAST_1='sa-east-1'
    US_EAST_1='us-east-1'
    US_EAST_2='us-east-2'
    US_GOV_EAST_1='us-gov-east-1'
    US_GOV_WEST_1='us-gov-west-1'
    US_WEST_1='us-west-1'
    US_WEST_2='us-west-2'


class AWSRegionMap:

    def __init__(self):
        self._region_map = {
            'af-south-1': AWSRegion.AF_SOUTH_1,
            'ap-east-1': AWSRegion.AP_EAST_1,
            'ap-northeast-1': AWSRegion.AP_NORTHEAST_1,
            'ap-northeast-2': AWSRegion.AP_NORTHEAST_2,
            'ap-northeast-3': AWSRegion.AP_NORTHEAST_3,
            'ap-south-1': AWSRegion.AP_SOUTH_1,
            'ap-south-2': AWSRegion.AP_SOUTH_2,
            'ap-southeast-1': AWSRegion.AP_SOUTHEAST_1,
            'ap-southeast-2': AWSRegion.AP_SOUTHEAST_2,
            'ap-southeast-3': AWSRegion.AP_SOUTHEAST_3,
            'ap-southeast-4': AWSRegion.AP_SOUTHEAST_4,
            'ca-central-1': AWSRegion.CA_CENTRAL_1,
            'eu-central-1': AWSRegion.EU_CENTRAL_1,
            'eu-central-2': AWSRegion.EU_CENTRAL_2,
            'eu-north-1': AWSRegion.EU_NORTH_1,
            'eu-south-1': AWSRegion.EU_SOUTH_1,
            'eu-south-2': AWSRegion.EU_SOUTH_2,
            'eu-west-1': AWSRegion.EU_WEST_1,
            'eu-west-2': AWSRegion.EU_WEST_2,
            'eu-west-3': AWSRegion.EU_WEST_3,
            'il-central-1': AWSRegion.IL_CENTRAL_1,
            'me-central-1': AWSRegion.ME_CENTRAL_1,
            'me-south-1': AWSRegion.ME_SOUTH_1,
            'sa-east-1': AWSRegion.SA_EAST_1,
            'us-east-1': AWSRegion.US_EAST_1,
            'us-east-2': AWSRegion.US_EAST_2,
            'us-gov-east-1': AWSRegion.US_GOV_EAST_1,
            'us-gov-west-1': AWSRegion.US_GOV_WEST_1,
            'us-west-1': AWSRegion.US_WEST_1,
            'us-west-2': AWSRegion.US_WEST_2,
        }

    def get(
        self,
        region_name: RegionName,
        default_region: AWSRegion = AWSRegion.US_EAST_1
    ):
        return self._region_map.get(region_name, default_region)

