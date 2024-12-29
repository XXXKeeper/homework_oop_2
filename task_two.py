def create_recept_book(local_path: str) -> dict:
    cook_book = {}
    with open(local_path, encoding='utf-8') as f:
        while True:
            dish_name = f.readline().rstrip()
            if dish_name == "":
                break
            cook_book[dish_name] = []
            count_ingredients = int(f.readline().rstrip())
            counter = 0
            while counter < count_ingredients:
                cook_book[dish_name].append({})
                ingredient = f.readline().rstrip().split(" | ")
                cook_book[dish_name][counter]["ingredient_name"] = ingredient[0]
                cook_book[dish_name][counter]["quantity"] = int(ingredient[1])
                cook_book[dish_name][counter]["measure"] = ingredient[2]
                counter += 1
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    cook_book = create_recept_book('recipes.txt')
    shop_list = {}
    for dish in dishes:
        ingredients = cook_book.get(dish)
        for ingredient in ingredients:
            ingredient_name = ingredient.get("ingredient_name")
            if not shop_list.get(ingredient_name):
                shop_list[ingredient_name] = {"measure": ingredient.get("measure"),
                                              "quantity": ingredient.get("quantity") * person_count}
            else:
                shop_list[ingredient_name]["quantity"] += ingredient.get("quantity") * person_count
    return shop_list


def main():
    shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    print(shop_list)


if __name__ == '__main__':
    main()
