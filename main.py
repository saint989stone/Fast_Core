from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Device(BaseModel):
    id: int
    ip_address: str
    jump_host: str 
    type_device: str
    hostname: str 
    region: str 
    filial: str 
    function: str 
    level: str 
    territory: str
    group: str 
    utc: str
    id_host_zabbix: str
    instance_zabbix: str
    count_ar: int
    count_unvail: int 
    date_time: int


devices = [
    {
        'id': 1232,
        'ip_address': '192.168.2.3',
        'jump_host': '2345', 
        'type_device': 'AR',
        'hostname': '23-Gol-AR1', 
        'region': 'UG', 
        'filial': 'KRDR', 
        'function': 'AR', 
        'level': 'RSPD', 
        'territory': 'KRDR',
        'group': 'KRDR-AR', 
        'utc': '+3',
        'id_host_zabbix': '23455',
        'instance_zabbix': 'rspd',
        'count_ar': 0,
        'count_unvail': 0, 
        'date_time': 0
    },
    {
        'id': 1234,
        'ip_address': '192.168.2.4',
        'jump_host': '2345', 
        'type_device': 'AR',
        'hostname': '23-Bel-AR1', 
        'region': 'UG', 
        'filial': 'KRDR', 
        'function': 'AR', 
        'level': 'RSPD', 
        'territory': 'KRDR',
        'group': 'KRDR-AR', 
        'utc': '+3',
        'id_host_zabbix': '23456',
        'instance_zabbix': 'rspd',
        'count_ar': 0,
        'count_unvail': 0, 
        'date_time': 0
    }
]
                    # Column('id', Integer, primary_key=True),
                    # Column('ip_address', String(45), unique=True, nullable=False),
                    # Column('jump_host', String(20), nullable=False),
                    # Column('type_device', String(20), nullable=False),
                    # Column('hostname', String(20), unique=True, nullable=False),
                    # Column('region', String(20), nullable=False),
                    # Column('filial', String(20), nullable=False),
                    # Column('function', String(20), nullable=False),
                    # Column('level', String(20), nullable=False),
                    # Column('territory', String(20), nullable=False),
                    # Column('group', String(20), nullable=False),
                    # Column('utc', SmallInteger, nullable=False),
                    # Column('id_host_zabbix', SmallInteger, nullable=False),
                    # Column('instance_zabbix', String(20), nullable=False),
                    # Column('count_ar', SmallInteger),
                    # Column('count_unvail', SmallInteger),
                    # Column('date_time', DateTime, default=datetime.utcnow)

@app.get(
        "/devices", 
        summary='Получить список устройств', 
        tags=['Main']
)
def get_devices():
    return devices

@app.get(
        "/devices/{device_id}",
         summary='Получить кодно устройство', 
         tags=['Main']
)
def get_device(device_id: int):
    for device in devices:
        if device['id'] == device_id:
            print(device_id, )
            return device
        
    raise HTTPException(status_code=404)        #устройство не найдено

@app.post('/books')
def post_devices(new_device: Device):
    print(type(new_device))
    devices.append({
        'id': len(devices) + 1,
        'ip_address': new_device.ip_address,
        'jump_host': new_device.jump_host, 
        'type_device': new_device.type_device,
        'hostname': new_device.hostname, 
        'region': new_device.region, 
        'filial': new_device.filial, 
        'function': new_device.function, 
        'level': new_device.level, 
        'territory': new_device.territory,
        'group': new_device.group, 
        'utc': new_device.utc,
        'id_host_zabbix': new_device.id_host_zabbix,
        'instance_zabbix': new_device.instance_zabbix,
        'count_ar': new_device.count_ar,
        'count_unvail': new_device.count_unvail, 
        'date_time': new_device.date_time
    })
    print(devices)
    return {'result': True, 'message': 'Устройство добавлено'}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)