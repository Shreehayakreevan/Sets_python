def main():
    # Creating sets of five items
    set1 = {"India","Australia","Afghanistan","Bangladesh"}
    set2 = {"India","USA","Ireland","Canada"}

    # Printing the sets
    print("S:et 1:", set1)
    print("Set 2", set2)

    # Union of sets
    print("\nUnion of Set 1 and Set 2:", set1.union(set2))

    # Intersection of sets
    print("Intersection of Set 1 and Set 2:", set1.intersection(set2))

    # Difference between sets
    print("Difference (Set 1 - Set 2):", set1.difference(set2))
    print("Difference (Set 2 - Set 1):", set2.difference(set1))

if __name__ == "__main__":
    main()
