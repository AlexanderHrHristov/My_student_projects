import requests


def check_directory(url, directory):
    full_url = url + "/" + directory
    response = requests.get(full_url)

    if response.status_code == 200:
        print(f"Directory found: {full_url}")
    else:
        print(f"Directory not found: {full_url}")


def main():
    target_url = "https://www.test.com"  # Заменете със съответния протокол (http/https)
    common_directories = [
        "admin", "login", "wp-admin", "wp-login", "adminpanel", "phpmyadmin", "administrator"
        # Добавете други директории, които искате да проверите
    ]

    for directory in common_directories:
        check_directory(target_url, directory)


if __name__ == "__main__":
    main()
