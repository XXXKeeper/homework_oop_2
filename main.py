def create_recept_book(local_path: str):
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


def main():
    cook_book = create_recept_book('recipes.txt')
    print(cook_book)


if __name__ == '__main__':
    main()
