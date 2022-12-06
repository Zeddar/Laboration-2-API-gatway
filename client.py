import requests


def main():
    menu_loop = True
    while menu_loop:
        response = requests.get("http://localhost:9080/temp/get/")
        values = response.json()
        print()
        print(values["text"], "Celsius ", '\n')
        val = input("Refresh? Y/N: ")
        if val.lower() == 'n':
            menu_loop = False
        else:
            menu_loop = True


if __name__ == "__main__":
    main()
