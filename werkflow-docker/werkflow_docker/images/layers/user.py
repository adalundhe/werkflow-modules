import re
from typing import Literal, Optional, Tuple

from pydantic import BaseModel, StrictStr


class User(BaseModel):
    layer_type: Literal['user'] = 'user'
    user_id: StrictStr
    group_id: Optional[StrictStr] = None

    def to_string(self) -> str:
        if self.group_id:
            return f'USER {self.user_id}:{self.group_id}'

        return f'USER {self.user_id}'

    @classmethod
    def parse(cls, line: str) -> 'User':
        stripped = re.sub(r'^USER\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()
        user_id, group_id = cls._match_permissions(stripped)

        return cls(
            user_id=user_id,
            group_id=group_id,
        )

    @classmethod
    def _match_permissions(cls, token: str) -> Tuple[str, Optional[str]]:
        if ':' in token:
            user_id, group_id = token.split(':', 1)
            return user_id, group_id
        return token, None
