def parse_settings(config_lines):
    settings = {}

    for line in config_lines:
        try:
            # Split
            key, value_str = line.split(":")

            # Convert type
            value = int(value_str)

            # Logic validation
            if not 0 <= value <= 100:
                raise ValueError("Out of range")

            # If everything is OK → add to dictionary
            settings[key] = value

        except IndexError:
            print(f"Format error in: {line}")

        except ValueError as e:
            print(f"Invalid value in: {line} ({e})")

    return settings


# Test Cases
configs = [
    "volume:80",        # Valid
    "brightness:120",   # Invalid Range
    "difficulty:hard",  # Invalid Type
    "mute",             # Invalid Format (no colon)
    "contrast:50"       # Valid
]

settings = parse_settings(configs)
print(f"Loaded Settings: {settings}")
