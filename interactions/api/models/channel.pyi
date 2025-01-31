from datetime import datetime
from enum import IntEnum
from typing import List, Optional, Union

from .message import Message, Embed, MessageInteraction
from ...models.component import ActionRow, Button, SelectMenu
from .misc import DictSerializerMixin, Overwrite, Snowflake
from .user import User
from ..http import HTTPClient

class ChannelType(IntEnum): ...

class ThreadMetadata(DictSerializerMixin):
    _json: dict
    archived: bool
    auto_archive_duration: int
    archive_timestamp: datetime.timestamp
    locked: bool
    invitable: Optional[bool]
    def __init__(self, **kwargs): ...

class ThreadMember(DictSerializerMixin):
    _json: dict
    id: Optional[Snowflake]  # intents
    user_id: Optional[Snowflake]
    join_timestamp: datetime.timestamp
    flags: int
    def __init__(self, **kwargs): ...

class Channel(DictSerializerMixin):
    _json: dict
    _client: HTTPClient
    id: Snowflake
    type: ChannelType
    guild_id: Optional[Snowflake]
    position: Optional[int]
    permission_overwrites: List[Overwrite]
    name: str  # This apparently exists in DMs. Untested in v9, known in v6
    topic: Optional[str]
    nsfw: Optional[bool]
    last_message_id: Optional[Snowflake]
    bitrate: Optional[int]  # not really needed in our case
    user_limit: Optional[int]
    rate_limit_per_user: Optional[int]
    recipients: Optional[List[User]]
    icon: Optional[str]
    owner_id: Optional[Snowflake]
    application_id: Optional[Snowflake]
    parent_id: Optional[Snowflake]
    last_pin_timestamp: Optional[datetime]
    rtc_region: Optional[str]
    video_quality_mode: Optional[int]
    message_count: Optional[int]
    member_count: Optional[int]
    thread_metadata: Optional[ThreadMetadata]
    member: Optional[ThreadMember]
    default_auto_archive_duration: Optional[int]
    permissions: Optional[str]
    def __init__(self, **kwargs): ...
    async def send(
        self,
        content: Optional[str] = None,
        *,
        tts: Optional[bool] = False,
        # attachments: Optional[List[Any]] = None,  # TODO: post-v4: Replace with own file type.
        embeds: Optional[Union[Embed, List[Embed]]] = None,
        allowed_mentions: Optional[MessageInteraction] = None,
        components: Optional[Union[ActionRow, Button, SelectMenu, List[Union[ActionRow, Button, SelectMenu]]]] = None,
    ) -> Message: ...
    async def delete(self) -> None: ...
    async def modify(
        self,
        name: Optional[str] = None,
        topic: Optional[str] = None,
        bitrate: Optional[int] = None,
        user_limit: Optional[int] = None,
        rate_limit_per_user: Optional[int] = None,
        position: Optional[int] = None,
        # permission_overwrites,
        parent_id: Optional[int] = None,
        nsfw: Optional[bool] = False,
        reason: Optional[str] = None,
    ) -> "Channel": ...
    async def add_member(
        self,
        member_id: int,
    ) -> None: ...
    async def pin_message(
            self,
            message_id: int,
    ) -> None: ...
    async def unpin_message(
        self,
        message_id: int,
    ) -> None: ...
    async def publish_message(
        self,
        message_id: int,
    ) -> Message: ...
    async def get_pinned_messages(self) -> List[Message]: ...


class Thread(Channel): ...
