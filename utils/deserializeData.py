import phpserialize

def read_php_serialized_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            deserialized_data = phpserialize.loads(data)
            return deserialized_data
    except Exception as e:
        print(f"Error: {e}")
        return None

file_path = "data/files/servers/servers.php" 
deserialized_data = read_php_serialized_data(file_path)

if isinstance(deserialized_data, dict):
    data_list = list(deserialized_data.items())
    #print(data_list)
else:
    print("The deserialized data is not a dictionary.")