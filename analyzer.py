import zmq
import pickle
from datetime import datetime

def get_age(date_of_birth):
    curr_year = datetime.now().year
    curr_month = datetime.now().month
    
    month, year = date_of_birth.split('/')

    age = curr_year - int(year)
    if (curr_month < int(month)):
        age -= 1
    
    return age

if __name__ == "__main__":
    context = zmq.Context()
    analyzer_receiver = context.socket(zmq.PULL)
    analyzer_receiver.connect('tcp://localhost:5556')

    analyzer_sender = context.socket(zmq.PUSH)
    analyzer_sender.connect('tcp://localhost:5557')
    
    data = analyzer_receiver.recv()
    students = pickle.loads(data)

    for i in range(1, len(students)):
        first_name = students[i]['first_name']
        last_name = students[i]['last_name']
        date_of_birth = students[i]['date_of_birth']
        print(f"First name {first_name}, Last name {last_name}, Date of birth {date_of_birth}")
        age = get_age(date_of_birth)

        student = (first_name, last_name, age)

        msg = pickle.dumps(student)

        analyzer_sender.send(msg)