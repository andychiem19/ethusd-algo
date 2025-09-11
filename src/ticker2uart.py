# code to convert ticker data to integers, pack it into bytes and write them over UART

import websockets
import asyncio
import json
import serial
import struct

ser = serial.Serial("COM3", 115200) # port and baud rate

def pack_values(last_str, vol_str): # converts strings to integers and packs them into bytes for fpga-chan
    last_int = int(float(last_str) * 100)
    vol_int  = int(float(vol_str))
    frame = struct.pack('>ii', last_int, vol_int) # big-endian, 2 4-byte signed integers
    return frame

async def main(): 
    url = "wss://ws.okx.com:8443/ws/v5/public"
    async with websockets.connect(url) as ws: 
        subscribe_message = {
            "op": "subscribe",
            "args": [{"channel": "tickers", "instId": "ETH-USDT"}]
            }
        await ws.send(json.dumps(subscribe_message))

        while True:
            msg = await ws.recv()
            data = json.loads(msg)

            if "data" in data:
                t = data["data"][0]
                frame = pack_values(t["last"], t["vol24h"])
                ser.write(frame)
                print([hex(b) for b in frame])

asyncio.run(main())
