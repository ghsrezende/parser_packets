from utils.util import (
    battery_voltage, bytes_to_latitude, bytes_to_longitude, external_voltage,
    device_information, timestamp, horimeter, course_status, gps_information,
    battery_voltage_level
)

def translated_location_packet(byte_array):
    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": {
            "Value Hex": f"0x{byte_array[2]:02X}",
            "Value": int(f"0x{byte_array[2]:02X}", 16),
        },
        "Protocol Number": {
            "Value Hex": f"0x{byte_array[3]:02X}",
            "Value": "Location Data Packet",
        },
        "GPS information" : {   
            "Date Time": {
                "Value Hex": f"0x{byte_array[4:10].hex()}",
                "Value": timestamp(byte_array[4:10]),
            },
            "Number Satellites": {
                "Value Hex": f"0x{byte_array[10]:02X}",
                "GPS Information" : gps_information(f"0x{byte_array[10]:02X}"),               
            },
            "Latitude": {
                "Value Hex": f"0x{byte_array[11:15].hex()}",
                "Value": bytes_to_latitude(byte_array[11:15]),
            },
            "Longitude": {
                "Value Hex": f"0x{byte_array[15:19].hex()}",
                "Value": bytes_to_longitude(byte_array[15:19]),
            },
            "Speed": {
                "Value Hex": f"0x{byte_array[19]:02X}",
                "Value": int(f"0x{byte_array[19]:02X}", 16),
            },
            "Course Status": course_status(byte_array[20:22]),
        },
        "LBS Information":  {
            "MCC": {
                "Value Hex": f"0x{byte_array[22:24].hex()}",
                "Value": int(f"0x{byte_array[22:24].hex()}", 16),
            },
            "MNC": {
                "Value Hex": f"0x{byte_array[24]:02X}",
                "Value": int(f"0x{byte_array[24]:02X}", 16),
            },
            "LAC": {
                "Value Hex": f"0x{byte_array[25:27].hex()}",
                "Value": int(f"0x{byte_array[25:27].hex()}", 16),
            },
            "Cell ID": {
                "Value Hex": f"0x{byte_array[27:30].hex()}",
                "Value": int(f"0x{byte_array[27:30].hex()}", 16),
            },
        },
        "Status Information": {
            "Device Information": device_information(byte_array[30]),
            "Battery Voltage Level": battery_voltage_level(f"0x{byte_array[31]:02X}"),
            "GSM Signal": {
                "Value Hex": f"0x{byte_array[32]:02X}",
                "Value": int(f"0x{byte_array[32]:02X}", 16),
            },
            "Battery Voltage": {
                "Value Hex": f"0x{byte_array[33:35].hex()}",
                "Value": battery_voltage(byte_array[33:35]),
            },
            "External Voltage": {
                "Value Hex": f"0x{byte_array[35:37].hex()}",
                "Value": external_voltage(byte_array[35:37]),
            },
        },
        "Mileage": {
            "Value Hex": f"0x{byte_array[37:41].hex()}",
            "Value": int(f"0x{byte_array[37:41].hex()}", 16),
        },
        "Horimeter": {
            "Value Hex": f"0x{byte_array[41:45].hex()}",
            "Value": horimeter(byte_array[41:45]),
        },
        "Serial Number": {
            "Value Hex": f"0x{byte_array[45:47].hex()}",
            "Value": int(f"0x{byte_array[45:47].hex()}", 16),
        },
        "CRC": byte_array[47:49].hex(),
        "End Bit": byte_array[49:].hex(),
    }
    
    return parse_packet

def parse_location_data_packet(byte_array):

    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": f"0x{byte_array[2]:02X}",
        "Protocol Number": f"0x{byte_array[3]:02X}",
        "GPS information": {
            "Date Time": byte_array[4:10].hex(),
            "Number Satellites": f"0x{byte_array[10]:02X}",
            "Latitude": byte_array[11:15].hex(),
            "Longitude": byte_array[15:19].hex(),
            "Speed": f"0x{byte_array[19]:02X}",
            "Course Status": byte_array[20:22].hex()
        },
        "LBS Information": {
            "MCC": byte_array[22:24].hex(),
            "MNC": f"0x{byte_array[24]:02X}",
            "LAC": byte_array[25:27].hex(),
            "Cell ID": byte_array[27:30].hex()
        },
        "Status Information": {
            "Device Information": f"0x{byte_array[30]:02X}",
            "Battery Voltage Level": f"0x{byte_array[31]:02X}",
            "GSM Signal": f"0x{byte_array[32]:02X}",
            "Battery Voltage": byte_array[33:35].hex(),
            "External Voltage": byte_array[35:37].hex()
        },
        "Mileage": byte_array[37:41].hex(),
        "Horimeter": byte_array[41:45].hex(),
        "Serial Number": byte_array[45:47].hex(),
        "CRC": byte_array[47:49].hex(),
        "End Bit": byte_array[49:].hex(),
    }

    return parse_packet

