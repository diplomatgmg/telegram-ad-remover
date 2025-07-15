from pathlib import Path

from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict, TomlConfigSettingsSource


__all__ = [
    "BASE_DIR",
    "app_config",
]

BASE_DIR = Path(__file__).parent.parent
FILTER_CONFIG_TOML_PATH = BASE_DIR / "core" / "filter_config.toml"


class AppConfig(BaseSettings):
    telethon_api_id: int
    telethon_api_hash: str

    channel_ids: list[int]
    patterns: list[str]

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        toml_file=FILTER_CONFIG_TOML_PATH,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,  # noqa: ARG003
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,  # noqa: ARG003
        file_secret_settings: PydanticBaseSettingsSource,  # noqa: ARG003
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return env_settings, TomlConfigSettingsSource(settings_cls)


app_config = AppConfig()
