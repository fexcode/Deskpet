from deskpet import *
from deskpet.plugins.examples import *


def main():
    choice_manager = ChoiceManager()
    choice_manager.add_choice(TutorialChoice)
    choice_manager.add_choice(ExitChoice)

    pet = Pet(
        image_path="./logo.png", choice_list=choice_manager.all_choices
    )  # 可以自定义图片路径等参数
    app = App(pet=pet)

    app.run()


if __name__ == "__main__":
    main()
