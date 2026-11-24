import re
from typing import Literal, Optional

from pydantic import BaseModel, StrictStr


class Stage(BaseModel):
    layer_type: Literal['stage'] = 'stage'
    base: StrictStr
    tag: StrictStr
    platform: Optional[StrictStr] = None
    alias: Optional[StrictStr] = None

    def to_string(self) -> str:
        from_args = ['FROM']

        if self.platform:
            from_args.append(f'--platform={self.platform}')

        if self.tag.startswith('sha256:'):
            from_args.append(f'{self.base}@{self.tag}')
        else:
            from_args.append(f'{self.base}:{self.tag}')

        if self.alias:
            from_args.append(f'AS {self.alias}')

        return ' '.join(from_args)

    @classmethod
    def parse(cls, line: str) -> 'Stage':
        stripped = re.sub(r'^FROM\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()
        templated_platform_pattern = re.compile(r'--platform=([^\s]+)')
        templated_alias_pattern = re.compile(r'\s+AS\s+([^\s]+)\s*$', re.IGNORECASE)

        platform: Optional[str] = None
        alias: Optional[str] = None

        if platform_match := templated_platform_pattern.search(stripped):
            platform = platform_match.group(1)
            stripped = templated_platform_pattern.sub('', stripped, count=1).strip()

        if alias_match := templated_alias_pattern.search(stripped):
            alias = alias_match.group(1).strip()
            stripped = templated_alias_pattern.sub('', stripped, count=1).strip()

        if '@' in stripped:
            base, tag = stripped.split('@', 1)
        else:
            last_slash = stripped.rfind('/')
            last_colon = stripped.rfind(':')
            if last_colon > last_slash:
                base = stripped[:last_colon]
                tag = stripped[last_colon + 1:]
            else:
                base = stripped
                tag = 'latest'

        return cls(
            base=base.strip(),
            tag=tag.strip(),
            platform=platform,
            alias=alias,
        )
