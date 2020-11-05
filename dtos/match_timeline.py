from dataclasses import dataclass
import typing


@dataclass
class MatchPositionDto:
    x: int
    y: int


@dataclass
class MatchEventDto:
    laneType: str
    skillSlot: int
    ascendedType: str
    creatorId: int
    afterId: int
    eventType: str
    type: str
    levelUpType: str
    wardType: str
    participantId: int
    towerType: str
    itemId: int
    beforeId: int
    pointCaptured: str
    monsterType: str
    monsterSubType: str
    teamId: int
    position: MatchPositionDto
    killerId: int
    timestamp: int
    assistingParticipantIds: typing.List[int]
    buildingType: str
    victimId: int


@dataclass
class MatchParticipantFrameDto:
    participantId: int
    minionsKilled: int
    teamScore: int
    dominionScore: int
    totalGold: int
    level: int
    xp: int
    currentGold: int
    position: MatchPositionDto
    jungleMinionsKilled: int


@dataclass
class MatchFrameDto:
    participant_frames: typing.Mapping[str, MatchParticipantFrameDto]
    events: typing.List[MatchEventDto]
    timestamp: int


@dataclass
class MatchTimelineDto:
    frames: typing.List[MatchFrameDto]
    frame_interval: int
