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

from typing import Any, TypedDict, List, Dict, Optional, Union


class Equalizer(TypedDict):
    band: int
    gain: float


class Karaoke(TypedDict, total=False):
    level: Optional[float]
    monoLevel: Optional[float]
    filterBand: Optional[float]
    filterWidth: Optional[float]


class Timescale(TypedDict, total=False):
    speed: Optional[float]
    pitch: Optional[float]
    rate: Optional[float]


class Tremolo(TypedDict, total=False):
    frequency: Optional[float]
    depth: Optional[float]


class Vibrato(TypedDict, total=False):
    frequency: Optional[float]
    depth: Optional[float]


class Rotation(TypedDict, total=False):
    rotationHz: Optional[float]


class Distortion(TypedDict, total=False):
    sinOffset: Optional[float]
    sinScale: Optional[float]
    cosOffset: Optional[float]
    cosScale: Optional[float]
    tanOffset: Optional[float]
    tanScale: Optional[float]
    offset: Optional[float]
    scale: Optional[float]


class ChannelMix(TypedDict, total=False):
    leftToLeft: Optional[float]
    leftToRight: Optional[float]
    rightToLeft: Optional[float]
    rightToRight: Optional[float]


class LowPass(TypedDict, total=False):
    smoothing: Optional[float]


class FilterPayload(TypedDict, total=False):
    volume: Optional[float]
    equalizer: Optional[List[Equalizer]]
    karaoke: Karaoke
    timescale: Timescale
    tremolo: Tremolo
    vibrato: Vibrato
    rotation: Rotation
    distortion: Distortion
    channelMix: ChannelMix
    lowPass: LowPass
    pluginFilters: Dict[str, Any]
