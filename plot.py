# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    loss_table = []
    train_loss_table = []
    accuracy_table = []
    epochs = []

    epoch_num = 0;

    path = "result/Resnet34/"
    title = "ResNet34"
    f = open(path+"resnet34.txt", "r")
    line = f.readline()

    while line:

        line = f.readline()
        if line == "":
            break

        epochs.append(epoch_num)
        epoch_num = epoch_num + 1

        line = f.readline().strip('\n')
        lines = line.split(':')
        loss_table.append(float(lines[-1]))

        f.readline()

        line = f.readline().strip('\n')
        lines = line.split(' ')

        print(lines)
        train_loss_table.append(float(lines[3]))
        accuracy_table.append(float(lines[-1]))

    print(len(epochs))
    print(len(accuracy_table))
    print(len(train_loss_table))
    print(len(loss_table))
    f.close()

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(range(0,30), accuracy_table, 'r', label="Accuracy");
    ax1.legend(loc=1)
    ax1.set_ylabel("Accuracy Over Epochs")
    ax2 = ax1.twinx()  # this is the important function
    ax2.plot(range(0,30), train_loss_table, 'g', label="Training Loss")
    ax2.legend(loc=2)
    ax2.set_ylabel("Training Loss Over Epochs");
    ax1.set_xlabel("Epochs")
    plt.title("Training: " + title)
    plt.savefig(path + "Training")
    plt.show()

'''
    plt.plot(range(0,30),train_loss_table)
    plt.xlabel("Epochs")
    plt.ylabel("Training Loss")
    plt.title("Training Loss Over Epochs: " + title)
    plt.savefig(path + "TrainLoss")
    plt.show()

    plt.plot(range(0, 30), loss_table)
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.title("Loss Over Epochs: " + title)
    plt.savefig(path + "Loss")
    plt.show()

    plt.plot(range(0, 30), accuracy_table)
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.title("Accuracy Over Epochs: " + title)
    plt.savefig(path + "Accuracy")
    plt.show()
'''
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

clone https://github.com/tensorflow/tflite-micro-arduino-examples Arduino_TensorFlowLite
