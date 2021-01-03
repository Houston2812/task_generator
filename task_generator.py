import zmq
import pickle

if __name__ == "__main__":
    
    context = zmq.Context()
    generator = context.socket(zmq.PUSH)
    generator.bind('tcp://*:5555')

    receiver = context.socket(zmq.PULL)
    receiver.connect('tcp://localhost:5558')

    print("Enter the filename: ")
    filename = input()

    print("Press enter to start...")
    _ = input()

    msg = filename
    generator.send_string(msg)

    students = receiver.recv()
    for i in pickle.loads(students):
        print(i)