import re

#REGEX pattern to group data into columns
log_pattern = re.compile( 
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)'
    r' - - \[(?P<datetime>[^\]]+)\] '
    r'"(?P<http_method>[A-Z]+) '
    r'(?P<resource>[^ ]+) '
    r'HTTP/(?P<protocol_version>\d.\d)" '
    r'(?P<status>\d+) '
    r'(?P<response_time>\d+) '
    r'"(?P<referrer>[^"]+)" '
    r'"(?P<user_agent>[^"]+)" '
    r'(?P<process_time>\d+)'
)

# Function to parse logs using the re module
def parse_logs(file_path):
    
    parsed_logs = []

    try:
        with(open(file_path, "r")) as file: 
            for line in file:         
                try:
                    match = re.match(log_pattern,line)
                    if match:
                        parsed_logs.append(match.groupdict())
                except re.error as e:
                    print(f"Regex error: {e}")
                    continue        
      
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found ")
    except IOError:
        print(f"Error: There was an issue  reading  the file at {file_path}.")

    return parsed_logs