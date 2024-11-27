

import discord
from saavn import Track as SaavnTrack

from .utils import ExtrasNamespace


class Track:
    """Represents a track."""
    def __init__(self, track: SaavnTrack):
        self.track = track
        self.source = discord.FFmpegPCMAudio(track.media_url)
        self.extras = ExtrasNamespace()
