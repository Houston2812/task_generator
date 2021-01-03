import zmq
import csv
import pickle

if __name__ == "__main__":
    context = zmq.Context()

    receiver = context.socket(zmq.PULL)
    receiver.connect('tcp://localhost:5555')

    sender = context.socket(zmq.PUSH)
    sender.bind('tcp://*:5556')

    starter = context.socket(zmq.PUSH)
    starter.connect('tcp://localhost:5557')

    filename = receiver.recv().decode('utf-8')
    print(filename)
    

    students = []
    with open(filename, 'r') as f:
        csv_reader = csv.DictReader(f)
        for line in csv_reader:
            print(line)
            students.append(line)

    starter.send_string(f'{len(students)}')

    enc_data = pickle.dumps(students)    
    sender.send(enc_data)

