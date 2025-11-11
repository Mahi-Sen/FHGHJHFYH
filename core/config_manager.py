# core/config_manager.py

from .database import database
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Get a new collection dedicated to system configuration
config_collection = database.get_collection("system_config")

class SystemConfig(BaseModel):
    id: str = Field("global_settings", alias="_id")
    api_enabled: bool = True
    # REMOVE old datetime fields
    # lockdown_start: Optional[datetime] = None
    # lockdown_end: Optional[datetime] = None
    
    # ADD new time string fields
    daily_lockdown_start_utc: Optional[str] = None # e.g., "22:30"
    daily_lockdown_end_utc: Optional[str] = None   # e.g., "05:00"

    maintenance_message: Optional[str] = "The service is temporarily unavailable for maintenance. Please try again later."

async def get_system_config() -> SystemConfig:
    """Retrieves the global system configuration from the database."""
    config_doc = await config_collection.find_one({"_id": "global_settings"})
    if config_doc:
        return SystemConfig(**config_doc)
    # If no config exists, return the default one
    return SystemConfig()

async def update_system_config(config_update: dict):
    """Updates the global system configuration."""
    await config_collection.update_one(
        {"_id": "global_settings"},
        {"$set": config_update},
        upsert=True # Creates the document if it doesn't exist
    )