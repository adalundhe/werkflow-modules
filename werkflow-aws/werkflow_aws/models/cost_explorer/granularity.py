from enum import Enum
from typing import Literal


GranularityLevel = Literal['hourly', 'daily', 'monthly']
AWSGranularityLevel = Literal['HOURLY', 'DAILY', 'MONTHLY']


class Granularity(Enum):
    HOURLY='HOURLY'
    DAILY='DAILY'
    MONTHLY='MONTHLY'

    def to_granularity(self, granularity: GranularityLevel):
        levels = {
            'hourly': Granularity.HOURLY,
            'daily': Granularity.DAILY,
            'monthly': Granularity.MONTHLY
        }

        return levels.get(granularity, Granularity.DAILY)


    def to_aws_granularity_slug(self, granularity: GranularityLevel):
        levels: dict[GranularityLevel, AWSGranularityLevel] = {
            level.name.lower(): level.value for level in Granularity
        }

        return levels.get(granularity, Granularity.DAILY.value)