import model
import view


def start():
    while True:
        command = view.show_menu()
        match command:
            case '1':
                model.get_contacts()
            case '2':
                model.read_file()
            case '3':
                model.save_file()
            case '4':
                model.add_contact()
            case '5':
                model.rename_contact()
            case '6':
                model.delete_contact()
            case '7':
                model.find_contact()
            case '0':
                break
