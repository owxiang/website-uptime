import os
import matplotlib.pyplot as plt

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the history and graph folders
history_folder = os.path.join(script_dir, "history")
graph_folder = os.path.join(script_dir, "graph")

# Create the graph folder if it doesn't exist
if not os.path.exists(graph_folder):
    os.makedirs(graph_folder)

# Get a list of all text files in the history folder
file_list = [f for f in os.listdir(history_folder) if f.endswith(".txt")]

# Iterate over the text files and plot the data
for filename in file_list:
    file_path = os.path.join(history_folder, filename)

    # Read data from file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Extract response time values from the last 24 records
    response_times = []
    start_index = max(0, len(lines) - 24)
    for line in lines[start_index:]:
        parts = line.split(", ")
        if len(parts) >= 2:
            response_time_str = parts[1].split(": ")[1]
            response_time = float(response_time_str)
            response_times.append(response_time)

    # Generate a new plot for each file
    plt.figure()

    # Generate the line graph
    num_records = range(1, len(response_times) + 1)
    plt.plot(num_records, response_times, marker='o')

    # Set plot labels and title
    plot_title = f"Website Response Time ({filename.rsplit('.', 1)[0]})"
    plt.xlabel("No. of Requests (Last 24)")
    plt.ylabel("Response Time (s)")
    plt.title(plot_title)

    # Set x-axis tick locations as integers
    plt.xticks(list(num_records))

    # Save the plot in the graph folder with the ".png" extension
    graph_file = os.path.join(graph_folder, f"{filename.rsplit('.', 1)[0]}.png")
    plt.savefig(graph_file)

    # Show the plot for the current file
    # plt.show()
