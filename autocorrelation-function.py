import sys


def read_file(input_file):
    data = []
    with open(input_file, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.split()
            x, y, z = float(line[0]), float(line[1]), float(line[2])
            data.append([x, y, z])

    return data


def compute_acf(data):
    data_size = len(data)
    length_acf = int(data_size / 100 * 10)
    values_for_one_point = data_size - length_acf

    acf_values = []
    for T in range(length_acf + 1):
        acf_value_T_x = 0
        acf_value_T_y = 0
        acf_value_T_z = 0

        for t in range(values_for_one_point):
            x_t, y_t, z_t = data[t][0], data[t][1], data[t][2]
            x_t_T, y_t_T, z_t_T = data[t + T][0], data[t + T][1], data[t + T][2]

            acf_value_T_x += x_t * x_t_T
            acf_value_T_y += y_t * y_t_T
            acf_value_T_z += z_t * z_t_T

        acf_values.append(
            [
                acf_value_T_x / values_for_one_point,
                acf_value_T_y / values_for_one_point,
                acf_value_T_z / values_for_one_point,
            ]
        )

    return acf_values


def write_to_file(acf_values):
    n = (len(acf_values) - 1) * 10
    with open(f"acf_output_{n}.txt", "w") as file:
        for line in acf_values:
            print(f"{line[0]}\t\t{line[1]}\t\t{line[2]}", file=file)


if __name__ == "__main__":
    file_name = sys.argv[1]
    data = read_file(file_name)
    acf_values = compute_acf(data)
    write_to_file(acf_values)
