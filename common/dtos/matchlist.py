from dataclasses import dataclass
import typing


@dataclass
class MatchReferenceDto:
    game_id: int
    role: str
    season: int
    platform_id: str
    champion: int
    queue: int
    lane: str
    timestamp: int


@dataclass
class MatchlistDto:
    start_index: int
    total_games: int
    end_index: int
    matches: typing.List[MatchReferenceDto]
