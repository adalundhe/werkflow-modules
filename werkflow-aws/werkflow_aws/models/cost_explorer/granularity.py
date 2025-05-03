from enum import Enum
from typing import Literal


GranularityLevel = Literal['hourly', 'daily', 'monthly']
AWSGranularityLevel = Literal['HOURLY', 'DAILY', 'MONTHLY']


class Granularity(Enum):
    HOURLY='HOURLY'
    DAILY='DAILY'
    MONTHLY='MONTHLY'

    @classmethod
    def to_granularity(cls, granularity: GranularityLevel):
        levels = {
            'hourly': Granularity.HOURLY,
            'daily': Granularity.DAILY,
            'monthly': Granularity.MONTHLY
        }

        return levels.get(granularity, Granularity.DAILY)

    @classmethod
    def to_aws_granularity_slug(cls, granularity: GranularityLevel):
        levels: dict[GranularityLevel, AWSGranularityLevel] = {
            level.name.lower(): level.value for level in Granularity
        }

        return levels.get(granularity, Granularity.DAILY.value)