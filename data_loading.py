from db_definition import CoolingWaterTemperature, Pressure, Temperature, TemperatureChannelEnum, CoolingWaterIO, PressureChannelEnum, CoolingWaterEnum, KELVIN, MILLIKELVIN,DB_Paths,create_session
import matplotlib.dates as md

def load_data(channel_type, channel, date1, date2, io_type = None):
    all_data = []

    for db_path in DB_Paths:
        session = create_session(db_path)

        with session:
            # Determine the correct Enum based on the channel type
            if channel_type == 'temperature':
                channel_enum = TemperatureChannelEnum
                table = Temperature
            elif channel_type == 'pressure':
                channel_enum = PressureChannelEnum
                table = Pressure
            elif channel_type == 'cooling_water':
                channel_enum = CoolingWaterEnum
                table = CoolingWaterTemperature
            else:
                raise ValueError(f"Invalid channel type provided: {channel_type}")

            # Retrieve the integer value of the channel based on the string provided
            channel_value = getattr(channel_enum, channel, None)
            
            # Check if a valid channel was found
            if channel_value is None:
                raise ValueError(f"Invalid channel provided: {channel}")
            
            if io_type is not None:
                io_value = getattr(CoolingWaterIO, io_type, None)
                if io_value is None:
                    raise ValueError(f"Invalid channel or io type provided: {io_type}")
            
            result = session.query(table).filter(
                table.channel == channel_value,  # Use the integer value for the channel
                table.io == io_value if io_type is not None else True,  # Only filter by io if a value is provided
                table.datetime > date1,
                table.datetime < date2
            ).order_by(table.id.asc()).all()

            if channel_type == 'temperature': 
                    all_data.extend([(md.date2num(data.datetime), data.value * MILLIKELVIN) for data in result])
            else:
                    all_data.extend([(md.date2num(data.datetime), data.value) for data in result])

        # Now, sort all_data based on timestamp, which is the first item of each tuple
        all_data.sort(key=lambda x: x[0])

        # Unpack the sorted data into separate lists
        timestamps, values = zip(*all_data) if all_data else ([], [])
    
    return values, timestamps