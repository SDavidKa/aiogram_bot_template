from aiogram.types import Message
from sqlalchemy import Integer, String, BigInteger, MetaData
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config import PostgresConfig
from sqlalchemy.future import select

engine = create_async_engine(PostgresConfig.URL)


class Base(AsyncAttrs, DeclarativeBase):
    metadata = MetaData(schema=PostgresConfig.SCHEMA)


class FSMState(Base):
    __tablename__ = 'fsm_states'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    bot_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    chat_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    state: Mapped[str] = mapped_column(String, nullable=True)


class FSMData(Base):
    __tablename__ = 'fsm_data'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    bot_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    chat_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    data: Mapped[JSONB] = mapped_column(JSONB, nullable=True)

async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_all_user_ids(message: Message):
    async with async_session() as session:
        result = await session.execute(select(FSMState.chat_id).filter_by(
            bot_id=message.bot.id
        ))
        user_ids = result.scalars().all()

        return user_ids


async def get_list_users_with_data(message: Message):
    async with async_session() as session:
        result = await session.execute(
            select(FSMData).filter_by(
                bot_id=message.bot.id
            )
        )
        data = result.scalars().all()

        return data
