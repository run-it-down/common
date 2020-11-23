from dataclasses import dataclass
import typing


@dataclass
class MatchPositionDto:
    x: int
    y: int


@dataclass
class MatchEventDto:
    lane_type: str
    skill_slot: int
    ascended_type: str
    creator_id: int
    after_id: int
    event_type: str
    type: str
    level_up_type: str
    ward_type: str
    participant_id: int
    tower_type: str
    item_id: int
    before_id: int
    point_captured: str
    monster_type: str
    monster_sub_type: str
    team_id: int
    position: MatchPositionDto
    killer_id: int
    timestamp: int
    assisting_participant_ids: typing.List[int]
    building_type: str
    victim_id: int


@dataclass
class MatchParticipantFrameDto:
    participant_id: int
    minions_killed: int
    team_score: int
    dominion_score: int
    total_gold: int
    level: int
    xp: int
    current_gold: int
    position: MatchPositionDto
    jungle_minions_killed: int


@dataclass
class MatchFrameDto:
    participant_frames: typing.Mapping[str, MatchParticipantFrameDto]
    events: typing.List[MatchEventDto]
    timestamp: int


@dataclass
class MatchTimelineDto:
    frames: typing.List[MatchFrameDto]
    frame_interval: int
