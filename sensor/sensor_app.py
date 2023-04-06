# Runner script for all modules
from house_info import HouseInfo
from load_data import load_sensor_data 
##############################
# Do not remove these two lines
# They are needed to validate your unittest
data=[]
data = load_sensor_data()
print("Sensor Data App")
##############################
print("Loaded records: {}".format(len(data)))
# Module 1 code here:

# Module 2 code here:

# Module 3 code here:
house_info = HouseInfo(data)

# Set test_area variable to 1
test_area = 1

# Get records by area
recs = house_info.get_data_by_area("id", rec_area=test_area)

# Print length of records list
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))

# Set test_date variable to datetime object with "5/9/20" as input and "%m/%d/%y" as format
test_date = datetime.strptime("5/9/20", "%m/%d/%y")

# Get records by date
recs = house_info.get_data_by_date("id", rec_date=test_date)

# Print date and length of records list
print("\nHouse sensor records for date: {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))




# Module 4 code here:

# Module 5 code here: