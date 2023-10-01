from pymavlink import mavutil

connection = mavutil.mavlink_connection('udpin:localhost:14540')
print("Waiting for heartbeat on port 14540")
connection.recv_match(type='HEARTBEAT', blocking=True)
print("Got heartbeat")

while True:
    connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
    print(f"Sent heartbeat")
    message = connection.recv_match(blocking=True)
    print(f"Got message: {message}")
