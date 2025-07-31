from sqlalchemy import Table, Column, Integer, String, ForeignKey, func, text
from typing import Annotated
from sqlalchemy.dialects.postgresql import INET, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, str_256
from datetime import datetime

#Кастомные типы вместо mapped_column
int_pk = Annotated[int, mapped_column(primary_key=True)]
date_time_cr = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]            #определение переменной даты в формате UTC создания записи через запрос к серверу БД (server_default) на уровне приложения (default)
date_time_up = Annotated[datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.utcnow,
    )]

class Devices(Base):
    __tablename__="devices"
    id: Mapped[int_pk]
    ip_address: Mapped[str_256]
    jump_host: Mapped[str] = mapped_column(String(20), nullable=False)
    type_device: Mapped[str] = mapped_column(String(20), nullable=False)
    hostname: Mapped [str] = mapped_column(String(20), unique=True, nullable=False)
    region: Mapped [str] = mapped_column(String(20), nullable=False)
    filial: Mapped [str] = mapped_column(String(20), nullable=False)
    function: Mapped [str] = mapped_column(String(20), nullable=False)
    level: Mapped [str] = mapped_column(String(20), nullable=False)
    territory: Mapped [str] = mapped_column(String(20), nullable=False)
    group: Mapped [str] = mapped_column(String(20), nullable=False)
    utc: Mapped [int] = mapped_column(nullable=False)
    id_host_zabbix: Mapped [int] = mapped_column(nullable=False)
    instance_zabbix: Mapped [str] = mapped_column(String(20), nullable=False)
    count_ar: Mapped [int] = mapped_column(nullable=False)
    count_unvail: Mapped [int] = mapped_column(nullable=False)
    create_date_time: Mapped[date_time_cr]
    update_date_time: Mapped[date_time_up]

class Interfaces(Base):
    __tablename__="interfaces"
    id: Mapped[int] = mapped_column(primary_key=True)
    interface_a: Mapped[str]
    interface_b: Mapped[str]
    id_interface_b: Mapped[str]
    device_id_a: Mapped[int] = mapped_column(ForeignKey("devices.id", ondelete="CASCADE"))          #внешний ключ 
    create_date_time: Mapped[date_time_cr]
    update_date_time: Mapped[date_time_up]