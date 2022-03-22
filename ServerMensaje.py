#!/usr/bin/env python

import asyncio
import websockets
import time
import threading

connections=set()

def mandar():
    global connections
    vPrint=True
    while True:
            
        if len(connections)>0:
            print(connections)
            mensaje=input("Esto es un mensaje : ")
            if mensaje!="u":
                websockets.broadcast(connections,mensaje)
            vPrint=True
        elif vPrint:
            print("Conexiones: ")
            print(connections)
            vPrint=False


async def handler(websocket):
    global connections
    connections.add(websocket)
    await websocket.wait_closed()
    connections.remove(websocket)
    
        
async def main():
    threading.Thread  (target=mandar).start()
    async with websockets.serve(handler, "172.24.50.15", 8765):
        await asyncio.Future()  # run forever..

if __name__ == "__main__":
    asyncio.run(main())