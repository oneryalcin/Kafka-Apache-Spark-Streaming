import logging
from kafka import KafkaProducer
import json
import time

logger = logging.getLogger(__name__)

class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):
        with open(self.input_file) as f:
            data = json.load(f)
            for row in data:
                message = self.dict_to_binary(row)
                # TODO send the correct data
                self.send(self.topic, message)
                time.sleep(0.1)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
#         x = datetime.strptime("2018-12-31T00:00:00.000","%Y-%m-%dT%H:%M:%S.%f") 
        json_dict['crime_id'] = int(json_dict['crime_id'])
        json_dict['agency_id'] = int(json_dict['agency_id'])
        
        logger.debug("sending: %s", json.dumps(json_dict, indent=4, sort_keys=True))
        
        return json.dumps(json_dict).encode() 
        

# if __name__ == "__main__":
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.DEBUG)
#     p = ProducerServer(
#         input_file='/home/workspace/police-department-calls-for-service.json',
#         topic="com.udacity.apache.spark.police.calls.raw.v1"
#     )
#     p.generate_data()