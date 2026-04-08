import matplotlib.pyplot as plt

def show_graph():
    labels = ["Secure", "Weak", "Open"]
    values = [5, 2, 1]

    plt.bar(labels, values)
    plt.title("Security Overview")
    plt.xlabel("Type")
    plt.ylabel("Count")

    plt.show()
