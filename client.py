import requests


def main():
    response = requests.get("http://localhost:9080/temp/get/")
    values = response.json()

    print(values)


if __name__ == "__main__":
    main()
