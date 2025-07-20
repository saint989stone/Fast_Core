from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.dialects.postgresql import INET, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Devices(Base):
    __tablename__="devices"
    id: Mapped[int] = mapped_column(primary_key=True)
    ip_address: Mapped[str]
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
    count_ar: Mapped [str] = mapped_column(String(20), nullable=False)
    count_unvail: Mapped [int] = mapped_column(nullable=False)
    date_time: Mapped [str] = mapped_column(nullable=False)
