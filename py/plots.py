import matplotlib.pyplot as plt
import numpy as np

def make_simplest_classifier_plot(arrow_x=2.5):
    reds = [-4.4, -2.1, -1.9, 1.1, 1.9]
    blues = [3.1, 3.8, 6.6, 8.8]

    plt.scatter(reds, np.zeros_like(reds), c='r')
    plt.scatter(blues, np.zeros_like(blues), c='b')
    # plt.arrow(arrow_x, 0.5, 0, -0.5, width=0.1, head_length=0.2, head_width=0.5,
    #           length_includes_head=True, color='black')
    plt.plot([arrow_x, arrow_x], [0.5, -0.5], 'k--')
    plt.ylim(-0.75, 0.75)
    # plt.axis('off')
    # plt.yaxis('off')
    plt.yticks([], [])
    plt.savefig(f'../out/1d_classifier_{arrow_x}.png', bbox_inches='tight')
    plt.close()

def make_2d_classifier_plot():
    np.random.seed(0)
    red_x = np.random.rand(10)
    red_y = np.random.rand(10)
    print('test')
    points_x = np.random.rand(50)
    points_y = np.random.rand(50)
    points_x *= 5
    points_x += 1.5
    points_y *= 3
    points_y += 1.5

    reds = [(points_x[i], points_y[i]) for i in range(len(points_x)) if points_y[i] > 0.5*points_x[i] + 0.5]
    blues = [(points_x[i], points_y[i]) for i in range(len(points_x)) if points_y[i] <= 0.5*points_x[i] + 0.5]
    red_x = [r[0] for r in reds]
    red_y = [r[1] for r in reds]
    blue_x = [b[0] for b in blues]
    blue_y = [b[1] for b in blues]
    # plt.scatter(points_x, points_y, c='k')
    plt.scatter(red_x, red_y, c='r')
    plt.scatter(blue_x, blue_y, c='b')
    # plt.plot([1.5, 4.5], [1.5, 4.5], 'k--')
    plt.plot([1.5, 6.5], [1.5/1.5 + 0.25, 6.5/1.5 + 0.25], 'k--')
    # plt.plot([1.5, 6.5], [1.5/2 + 0.5, 6.5/2 + 0.5], 'k--')
    plt.savefig(f'../out/2d_classifier_v2.png')


if __name__ == '__main__':
    # make_simplest_classifier_plot(arrow_x=0.0)
    # make_simplest_classifier_plot(arrow_x=2.5)
    make_2d_classifier_plot()
