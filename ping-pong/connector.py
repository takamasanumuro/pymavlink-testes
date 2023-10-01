from pymavlink import mavutil
import time

port = 14540
connection = mavutil.mavlink_connection(f'udpout:localhost:{port}')
print(f"Sending heartbeat on port {port}")
connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GROUND_ROVER, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

print(f"Waiting for heartbeat on port {port}")
while True:
    message = connection.recv_match(blocking=True)
    print(f"Got message: {message}")
    connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GROUND_ROVER, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
    time.sleep(1)
