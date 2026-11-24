import re
from typing import Dict, Optional


def get_next_page(headers: Dict[bytes, bytes]) -> Optional[str]:
    links = headers.get(b'link')
    if links is None:
        for key, value in headers.items():
            if key.lower() == b'link':
                links = value
                break

    if links is None:
        return None

    urls = links.split(b',')

    try:
        next_page = next(
            filter(
                lambda url: b'rel="next"' in url,
                urls,
            )
        )

        url, _ = next_page.split(b';', 1)

        return re.sub(
            r'[<>]',
            '',
            url.decode('utf-8'),
        ).strip()

    except Exception:
        return None
