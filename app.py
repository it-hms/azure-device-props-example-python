# Copyright (c) HMS Networks. All rights reserved.
# Licensed under the MIT license.

import os

from azure.iot.device import IoTHubDeviceClient, Message

#SAS TOKEN - Connection String is not stored in code, but read from environment
SAS_TOKEN = os.getenv("IOTHUB_DEVICE_SAS_TOKEN", default="error")

def get_client():
	if SAS_TOKEN == "error":
		raise Exception("SAS Token not set in evironment")
	return IoTHubDeviceClient.create_from_connection_string(SAS_TOKEN)



def run():
	client = get_client()
	

if __name__ == '__main__':
	run()