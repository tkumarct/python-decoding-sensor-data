class HouseInfo:
    def __init__(self,data):
        self.data=data
    
    def get_data_by_area(self, field, rec_area=0):
        field_data=[]
        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif int(record['area']) == str(rec_area):
                field_data.append(record[field])
        return field_data
    
    def get_data_by_date(self, field, rec_date=None):
        field_data = []
        for record in self.data:
            record_date = datetime.strptime(record['date'], '%m/%d/%y')
            if rec_date.strftime('%m/%d/%y') == record_date.strftime('%m/%d/%y'):
                field_data.append(record[field])
        return field_data