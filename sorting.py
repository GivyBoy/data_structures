import pandas as pd

cat1 = pd.CategoricalIndex(
                            ["a", "a", "b"],
                            categories=["a", "b"],
                            ordered=False
                          )

cat2 = pd.CategoricalIndex(
                            ["b", "a", "b"],
                            categories=["b", "a"],
                            ordered=False
                          )

df1 = pd.DataFrame({"A": [1, 2, 3]}, index=cat1)
df2 = pd.DataFrame({"A": [3, 4, 5]}, index=cat2)

d = pd.concat((df1, df2, df2, df1, df2, df1))

# print(cat1.append(cat2.set_categories(cat1.categories)))

print(d)

"""
New code that works with more than 2 DataFrames being append


def check_permutations(indexes):
    return all([sorted(indexes[0].categories) == sorted(i.categories) for i in indexes[1:]])

def _concat_indexes(indexes) -> Index.append():

    if check_permutations(indexes):
        return indexes[0].append([i.set_categories(indexes[0].categories) for i in indexes[1:]])

    return indexes[0].append(indexes[1:]) # here

"""