# Demonstrating reasoning with family relationships

# Facts
family = {
    "parent": [
        ("John", "Mary"),
        ("John", "Peter"),
        ("Susan", "Mary"),
        ("Susan", "Peter"),
        ("Mary", "James"),
        ("Mary", "Sophia"),
    ]
}

# Function to find siblings
def find_siblings(person):
    siblings = set()
    for p1, child1 in family["parent"]:
        for p2, child2 in family["parent"]:
            if p1 == p2 and child1 != child2 and (child1 == person or child2 == person):
                siblings.add(child1 if child2 == person else child2)
    return siblings

# Function to find grandparents
def find_grandparents(person):
    grandparents = set()
    for grandparent, parent in family["parent"]:
        for p, child in family["parent"]:
            if parent == p and child == person:
                grandparents.add(grandparent)
    return grandparents


# Queries and Reasoning
query1 = "Mary"
siblings_of_query1 = find_siblings(query1)
print(f"Siblings of {query1}: {siblings_of_query1}")

query2 = "James"
grandparents_of_query2 = find_grandparents(query2)
print(f"Grandparents of {query2}: {grandparents_of_query2}")
