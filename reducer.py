import zmq
import pickle

if __name__ == "__main__":
    context = zmq.Context()

    reducer_receiver = context.socket(zmq.PULL)
    reducer_receiver.bind('tcp://*:5557')
    
    reducer_sender = context.socket(zmq.PUSH)
    reducer_sender.bind('tcp://*:5558')

    data_len = reducer_receiver.recv().decode('utf-8')
    print(data_len)

    students = []
    for _ in range(int(data_len)-1):
        data = reducer_receiver.recv()
        student = pickle.loads(data)
        students.append(student)

    print('Sorted')
    students = sorted(students, key=lambda student: student[2])
    for student in students:
        print(student)

    msg = pickle.dumps(students)
    reducer_sender.send(msg)
