from environs import Env
from dataclasses import dataclass


@dataclass
class BotWater:
    # TELEGRAM
    tg_admin_id: int
    tg_bot_token: str

    # DB
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: int


@dataclass
class Settings:
    setting: BotWater


def get_settings(patch: str):
    env = Env()
    env.read_env(patch)

    return Settings(
        setting=BotWater(
            tg_admin_id=env.int('TG_ADMIN_ID'),
            tg_bot_token=env.str('TG_BOT_TOKEN'),

            db_user=env.str('DB_USER'),
            db_password=env.str('DB_PASSWORD'),
            db_name=env.str('DB_NAME'),
            db_host=env.str('DB_HOST'),
            db_port=env.int('DB_PORT'),
        )
    )


data_settings = get_settings('settings/.env')
