# Copyright (c) HMS Networks. All rights reserved.
# Licensed under the MIT license.

import os
import random
import json
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Connection String is not stored in code, but read from environment
CONN = os.getenv("IOTHUB_DEVICE_CONN_STR", default="error")


def get_client():
    try:
        if CONN == "error":
            raise Exception("SAS Token not set in environment")
        client = IoTHubDeviceClient.create_from_connection_string(CONN)
        client.connect()
    except Exception as e:
        print(e)
    return client


def run():
    client = get_client()
    while True:
        body = {"rand1": random.random() * 100, "rand2": random.random() * 100}
        message = Message(json.dumps(body))
        message.custom_properties["appProp1"] = "valueProp"
        message.content_type = "application/json"
        message.content_encoding = "utf-8"

        print(f"Sending message: {message}")
        client.send_message(message)
        time.sleep(10)


if __name__ == '__main__':
    run()
