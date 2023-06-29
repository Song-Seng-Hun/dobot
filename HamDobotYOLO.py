import DobotDetect
# from DobotDetect import *


def get_results():

    result = DobotDetect.run()
    # result = run()


    c_dict = {'0': 'red', '1': 'yellow', '2': 'green'}
    s_dict = {'0': 'Hexagonal Prism', '1': 'Cylinder', '2': 'Cube'}


    result_list = []
    for boxes in result:

        w = float(boxes.split()[-2])
        h = float(boxes.split()[-1])

        for i, v in enumerate(boxes.split()):
            if i == 0:
                color = c_dict[v]
                shape = s_dict[v]
            elif i == 1:
                x = int(float(v) * w)
            elif i == 2:
                y = int(float(v) * h)

        result_list.append([color, shape, x, y])
                                  
    print(result_list)
    return result_list


def main():
    get_results()

if __name__ == "__main__":
    main()
