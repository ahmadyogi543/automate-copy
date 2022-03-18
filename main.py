from shutil import copytree
from os import system, name as os_name


def print_msg(msg):
    print(msg)
    input("\nTekan enter untuk keluar...")


def header():
    print("===========================")
    print("++ Automate Copy - Python++")
    print("===========================")
    print()


def clear_screen():
    if os_name == "nt":
        system("cls")
    else:
        system("clear")
    header()


def get_separator():
    if os_name == "nt":
        return "\\"
    else:
        return "/"


def main():
    try:
        with open("config.txt", "r") as file:
            config = file.read().splitlines()

        try:
            src_path = config[0][config[0].find("=")+1:]
            dst_path = config[1][config[1].find("=")+1:]
            folder_list = config[2][config[2].find("=")+1:].split(",")

            try:
                separator = get_separator()

                for fl in folder_list:
                    full_src_path = src_path + separator + fl
                    full_dst_path = dst_path + separator + fl
                    copytree(full_src_path, full_dst_path)
                clear_screen()
                print_msg(
                    "Tugas selesai, semua folder sudah tersalin pada folder tujuan!")

            except FileExistsError:
                clear_screen()
                print_msg("Error: folder yang ingin disalin sudah ada!")

            except FileNotFoundError:
                clear_screen()
                print_msg("Error: folder tujuan atau destinasi salah!")

        except IndexError:
            clear_screen()
            print_msg(
                "Error: pastikan format dari config.txt sudah sesuai!")

    except FileNotFoundError:
        clear_screen()
        print_msg(
            "Error: file config.txt tidak ada, pastikan file tersebut berada pada satu folder dengan program!")


if __name__ == '__main__':
    main()
