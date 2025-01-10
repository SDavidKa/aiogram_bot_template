import json
from typing import Any, Dict, Optional
from aiogram.fsm.storage.base import BaseStorage, StorageKey
from aiogram.fsm.state import State
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.future import select
from services.db import FSMState, FSMData, Base

class PostgresStorage(BaseStorage):
    def __init__(self, dsn: str):
        self.engine = create_async_engine(dsn, echo=True)
        self.async_session = async_sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )

    async def connect(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def close(self) -> None:
        await self.engine.dispose()

    async def set_state(self, key: StorageKey, state: Optional[State] = None) -> None:
        async with self.async_session() as session:
            query = select(FSMState).filter_by(
                bot_id=key.bot_id,
                chat_id=key.chat_id,
                user_id=key.user_id,
            )
            result = await session.execute(query)
            fsm_state = result.scalar_one_or_none()
            if fsm_state is None:
                fsm_state = FSMState(
                    bot_id=key.bot_id, chat_id=key.chat_id, user_id=key.user_id
                )
                session.add(fsm_state)
            fsm_state.state = state.state if state else None
            await session.commit()

    async def get_state(self, key: StorageKey) -> Optional[str]:
        async with self.async_session() as session:
            query = select(FSMState).filter_by(
                bot_id=key.bot_id,
                chat_id=key.chat_id,
                user_id=key.user_id,
            )
            result = await session.execute(query)
            fsm_state = result.scalar_one_or_none()
            return fsm_state.state if fsm_state else None

    async def set_data(self, key: StorageKey, data: Dict[str, Any]) -> None:
        async with self.async_session() as session:
            query = select(FSMData).filter_by(
                bot_id=key.bot_id,
                chat_id=key.chat_id,
                user_id=key.user_id,
            )
            result = await session.execute(query)
            fsm_data = result.scalar_one_or_none()
            if fsm_data is None:
                fsm_data = FSMData(
                    bot_id=key.bot_id, chat_id=key.chat_id, user_id=key.user_id
                )
                session.add(fsm_data)
            fsm_data.data = json.dumps(data, ensure_ascii=False)
            await session.commit()

    async def get_data(self, key: StorageKey) -> Dict[str, Any]:
        async with self.async_session() as session:
            query = select(FSMData).filter_by(
                bot_id=key.bot_id,
                chat_id=key.chat_id,
                user_id=key.user_id,
            )
            result = await session.execute(query)
            fsm_data = result.scalar_one_or_none()
            return json.loads(fsm_data.data) if fsm_data else {}

    async def update_data(self, key: StorageKey, data: Dict[str, Any]) -> Dict[str, Any]:
        current_data = await self.get_data(key=key)
        current_data.update(data)
        await self.set_data(key=key, data=current_data)
        return current_data
