from deskpet import *
from deskpet.plugins.examples import *


def main():
    choice_manager = ChoiceManager()
    choice_manager.add_choice(AboutChoice)
    choice_manager.add_choice(MenuExampleChoice)
    choice_manager.add_choice(ExitChoice)

    pet = Pet(
        image_path="./logo.png",
        choice_manager=choice_manager,
    )
    app = App(pet=pet)

    app.run()


if __name__ == "__main__":
    main()
