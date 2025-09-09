from enum import Enum
from typing import Literal


AppitoRegionName = Literal["AU", "DEFAULT", "EU", "US"]

class AppitoRegion(Enum):
    AU = "AU"
    DEFAULT = "DEFAULT"
    EU = "EU"
    US = "US"
