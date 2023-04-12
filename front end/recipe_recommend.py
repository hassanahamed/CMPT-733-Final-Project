import itertools
import pandas as pd

prods_rec_map=pd.read_json('prods_rec_map.json')
recipes_df = pd.read_json("recipes.json")


def get_intersection_recipes(prod_list):
    recipe_lists = [list(prods_rec_map[prods_rec_map['name'].str.lower() == i.lower()]["recipe_index"].values)[0] for i in prod_list]
    if len(recipe_lists)==1:
        common_elements = set(recipe_lists[0])
        recipes = recipes_df.iloc[list(common_elements),[0,1]]
        return recipes
    
    common_elements = set(recipe_lists[0]).intersection(*recipe_lists[1:])
    recipes = recipes_df.iloc[list(common_elements),[0,1]]

    return recipes

def get_combinations(prod_list):
    combinations = []
    for i in range(1, len(prod_list) + 1):
        combinations += itertools.combinations(prod_list, i)
    return combinations

def get_recipes(input_prod_list):
    combinations = get_combinations(input_prod_list)
    combinations = sorted(combinations, key=lambda x: len(x), reverse=True)
    merged_df = pd.concat([get_intersection_recipes(c) for c in [input_prod_list]])
    # recipes_df = merged_df.sample(frac=1)
    return merged_df.head(10)

input_prod_list = ["ice cream"]

get_recipes(input_prod_list)