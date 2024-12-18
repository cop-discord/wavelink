"""
MIT License

Copyright (c) 2019-Current PythonistaGuild, EvieePy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeAlias, TypedDict, Optional, Dict


if TYPE_CHECKING:
    from typing_extensions import NotRequired

    from .filters import FilterPayload


class VoiceRequest(TypedDict):
    token: str
    endpoint: Optional[str]
    sessionId: str


class TrackRequest(TypedDict, total=False):
    encoded: Optional[str]
    identifier: str
    userData: Dict[str, Any]


class _BaseRequest(TypedDict, total=False):
    voice: VoiceRequest
    position: int
    endTime: Optional[int]
    volume: int
    paused: bool
    filters: FilterPayload
    track: TrackRequest


class EncodedTrackRequest(_BaseRequest):
    encodedTrack: Optional[str]


class IdentifierRequest(_BaseRequest):
    identifier: str


class UpdateSessionRequest(TypedDict):
    resuming: NotRequired[bool]
    timeout: NotRequired[int]


Request: TypeAlias = _BaseRequest | EncodedTrackRequest | IdentifierRequest
