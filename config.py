from dataclasses import dataclass
from typing import Optional

from environs import Env


@dataclass
class DatabaseConfig:
    SECRET_KEY: str
    SOCIAL_AUTH_FACEBOOK_KEY: str
    SOCIAL_AUTH_FACEBOOK_SECRET: str
    SOCIAL_AUTH_TWITTER_KEY: str
    SOCIAL_AUTH_TWITTER_SECRET: str
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY: str
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET: str


@dataclass
class Config:
    db: DatabaseConfig


def load_config(path: Optional[str]) -> Config:
    env: Env = Env()
    env.read_env(path)
    return Config(db=DatabaseConfig(SECRET_KEY=env('SECRET_KEY'),
                                    SOCIAL_AUTH_FACEBOOK_KEY=env('SOCIAL_AUTH_FACEBOOK_KEY'),
                                    SOCIAL_AUTH_FACEBOOK_SECRET=env('SOCIAL_AUTH_FACEBOOK_SECRET'),
                                    SOCIAL_AUTH_TWITTER_KEY=env('SOCIAL_AUTH_TWITTER_KEY'),
                                    SOCIAL_AUTH_TWITTER_SECRET=env('SOCIAL_AUTH_TWITTER_SECRET'),
                                    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=env('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'),
                                    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=env('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
                                    ))
