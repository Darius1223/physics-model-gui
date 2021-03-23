from physics_model import BallMovement
from animation import Animation

if __name__ == '__main__':
    ball_move = BallMovement(
        x_0=0,
        y_0=0,
        vx_0=40,
        vy_0=40,
    )

    movement = ball_move.move(
        t_start=0,
        t_end=20,
        dt=0.1,
    )

    x, y = [], []

    for data in movement:
        x.append(data[1])
        y.append(data[2])

    print(x)
    print(y)

    anim = Animation(x=x, y=y)
    anim.save()
