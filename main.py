from RubberDuck import RubberDuck

def main():
    duck = RubberDuck()
    print(duck)

    RubberDuck.squeak()

    duck.quack_volume = 10
    print('New volume:', duck.quack_volume)

    duck.boost_volume()
    print('Boosted volume:', duck.quack_volume)

    print('Default color:', RubberDuck.get_color())

if __name__ == "__main__":
    main()
