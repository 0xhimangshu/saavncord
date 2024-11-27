
from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import discord
from discord.utils import MISSING

from .queue import Queue
from .tracks import Track

if TYPE_CHECKING:
    from typing import Self
    from discord.abc import Connectable
    
    VocalGuildChannel = discord.VoiceChannel | discord.StageChannel


class Player(discord.VoiceProtocol):
    """The Player is a :class:`discord.VoiceProtocol` used to connect your :class:`discord.Client` to a
    :class:`discord.VoiceChannel`.
    """
    channel: VocalGuildChannel

    def __call__(self, client: discord.Client, channel: VocalGuildChannel) -> Self:
        super().__init__(client, channel)
        self._guild = channel.guild
        return self
    
    def __init__(self, client: discord.Client = MISSING, channel: Connectable = MISSING) -> None:
        super().__init__(client, channel)
        self.client = client
        self._guild = None

        self._connected = False
        self._connection_event = asyncio.Event()

        self._current: Track
        self._previous: Track
        self._original: Track

        self.queue: Queue = Queue() # TODO
        
        self._volume = 100
        self._paused = False

    # TODO
    async def connect(self, channel: VocalGuildChannel) -> None:
        ...

    async def disconnect(self) -> None:
        ...
    
    async def play(self, track: Track) -> None:
        ...
    
    async def stop(self) -> None:
        ...

    async def pause(self) -> None:
        ...
    
    async def resume(self) -> None:
        ...

    async def skip(self) -> None:
        ...
