#! /usr/bin/env python3

# You didn't think I'd do it all by hand, did you?

import pathlib
import json
import copy
import itertools

TARGET_FOLDER = pathlib.Path('src/main/resources/data/tictaccursed/recipes/generated/')

BASE_RECIPE = {
    "type": "minecraft:crafting_shaped",
    "pattern": [],
    "key": {},
    "result": {
        "item": None,
        "count": 1
    }
}

X_KEY = {
    "item": "tictaccursed:cross"
}
O_KEY = {
    "item": "tictaccursed:circle"
}

def main():
    TARGET_FOLDER.mkdir(parents=True, exist_ok=True)

    # Empty the folder
    for file in TARGET_FOLDER.glob("**/*.json"):
        file.unlink()

    for folder in TARGET_FOLDER.iterdir():
      folder.rmdir()

    for recipe in itertools.product(['X', 'O', ' '], repeat=9):
        # Skip all empty recipes
        if recipe.count(' ') == 9:
            continue

        # Determine the output
        win_x = False
        win_o = False

        # Rows and columns
        for i in range(3):
            if (recipe[i*3] == recipe[i*3+1] == recipe[i*3+2] == "X") or (recipe[i] == recipe[i+3] == recipe[i+6] == "X"):
                win_x = True
            if (recipe[i*3] == recipe[i*3+1] == recipe[i*3+2] == "O") or (recipe[i] == recipe[i+3] == recipe[i+6] == "O"):
                win_o = True

        # Diagonals
        if (recipe[0] == recipe[4] == recipe[8] == "X") or (recipe[2] == recipe[4] == recipe[6] == "X"):
            win_x = True
        if (recipe[0] == recipe[4] == recipe[8] == "O") or (recipe[2] == recipe[4] == recipe[6] == "O"):
            win_o = True

        # Set the output
        output = "unknown"
        if win_x and not win_o:
            output = "cross"
        if win_o and not win_x:
            output = "circle"

        # Create the recipe
        recipe_string = ''.join(recipe)
        new_recipe = copy.deepcopy(BASE_RECIPE)
        new_recipe["pattern"] = [recipe_string[0:3], recipe_string[3:6], recipe_string[6:9]]
        new_recipe["result"]["item"] = f"tictaccursed:{output}"

        # Add the keys
        if "X" in recipe_string:
            new_recipe["key"]["X"] = X_KEY
        if "O" in recipe_string:
            new_recipe["key"]["O"] = O_KEY

        # Write the recipe
        simple_id = recipe_string.replace(' ', '.').lower()

        dest_folder = TARGET_FOLDER / f"{simple_id[:3]}"
        dest_folder.mkdir(exist_ok=True)
        with open(dest_folder / f"{simple_id}.json", "w") as f:
            json.dump(new_recipe, f, indent=4)


if __name__ == "__main__":
    main()
