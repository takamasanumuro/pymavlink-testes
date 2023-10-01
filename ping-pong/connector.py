from pymavlink import mavutil
import time
import turtle

#initiate turtle
window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=150, height=150)

indicator = turtle.Turtle()
indicator.speed(0)
indicator.shape("circle")
indicator.color("#800000")
indicator.penup()
indicator.goto(0, 0)

port = 14550
connection = mavutil.mavlink_connection(f'udpin:localhost:{port}')
print(f"Sending heartbeat on port {port}")
connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GROUND_ROVER, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

print(f"Waiting for heartbeat on port {port}")
while True:
    message = connection.recv_match(blocking=True)
    if not message:
        continue
    message_type = message.get_type()
    if message_type == 'HEARTBEAT':
        print(f"Received heartbeat on port {port}")
        #Get flight mode
        flight_mode = message.custom_mode
        print(f"Flight mode: {flight_mode}")
        indicator.color("#FF0000")
    elif message_type == 'GPS_RAW_INT':
        print(f"Received GPS_RAW_INT on port {port}")
        #Get GPS data
        lat = message.lat
        lon = message.lon
        alt = message.alt
        print(f"GPS data: {lat}, {lon}, {alt}")
        indicator.color("#FF0000")
    connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GROUND_ROVER, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
    indicator.color("#800000")
    #time.sleep(1)
