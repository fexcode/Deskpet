from core.pet import Pet
from core.app import App
from plugins.manager import ALL_CHOICES


def main():
    pet = Pet(
        image_path="./logo.png", choice_list=ALL_CHOICES
    )  # 可以自定义图片路径等参数
    app = App(pet=pet)

    app.run()


if __name__ == "__main__":
    main()
