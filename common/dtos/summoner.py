from dataclasses import dataclass


@dataclass
class SummonerDto:
    account_id: str
    profile_icon_id: int
    revision_date: int
    name: str
    id: str
    puuid: str
    summoner_level: int
