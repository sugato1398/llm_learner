from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = 'llm_tool'
    debug: bool = False
    database_url :str
    api_key: str

    model_config={"env_file":".env"}


settings = Settings()