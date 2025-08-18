from typing import Literal

AWSS3StorageClass = Literal[
    'STANDARD',
    'REDUCED_REDUNDANCY',
    'STANDARD_IA',
    'ONEZONE_IA',
    'INTELLIGENT_TIERING',
    'GLACIER',
    'OUTPOSTS',
    'GLACIER_IR',
    'SNOW'
]