import model
import view


def start():
    user_choice = 0
    res = []
    while user_choice != 8:
        user_choice = view.main_menu()
        
        
        match user_choice:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
            case 5:
                new = list(view.new_contact())
                model.change_phone_book(res, new)
            case 6:
                model.delete_line_in_book(res)
                view.delete_success()
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                res = list(*result)
                view.show_contacts(result)
          