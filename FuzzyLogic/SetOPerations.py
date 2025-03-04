class FuzzySet:
    def __init__(self,elements=None):
        self.elements = elements or {}
    def union(self,other):
        return FuzzySet({x:max(self.elements.get(x,0),other.elements.get(x,0)) for x in set(self.elements) | set(other.elements)})
    def intersection(self, other):
        return FuzzySet({x:min(self.elements.get(x,0),other.elements.get(x,0)) for x in set(self.elements) & set(other.elements)})
    def cartesian_product(self, other):
        return {(x,y): min(self.elements[x],other.elements[y]) for x in self.elements for y in other.elements}
    def sum(self,other):
        return FuzzySet({x:min(1,self.elements.get(x,0) + other.elements.get(x,0)) for x in set(self.elements) | set(other.elements)})
    def difference(self,other):
        return FuzzySet({x:max(self.elements.get(x,0) - other.elements.get(x,0),0) for x in set(self.elements) | set(other.elements)})
    def complement(self,other):
        return FuzzySet({x : 1 - self.elements[x] for x in self.elements})
    def __repr__(self):
        return str(self.elements)

def create_Fuzzy_Set():
    """Fuzzy Set creation as per as User Input"""
    elements =  {}
    while True:
        element= input("Enter an Element (or press enter to finish):").strip()
        if not element:
            break

        while True: 
                try:
                    membership = float(input(f"Enter membership value for {element} (0-1):"))
                    if 0 <= membership <= 1:
                        elements[element]=membership
                        break
                    else: 
                         print("Membership Value must be between 0 and 1.")
                except ValueError:
                    print("Please enter a valid number between 0 and 1.")

    return FuzzySet(elements)
def main():
    print("Fuzzy Set OPerations")
    print("1. Create Fuzzy Set A")
    A = create_Fuzzy_Set()

    print("\n2. Create Fuzzy Set B")
    B=create_Fuzzy_Set()

    while True:
        print("\n Choose an Operation:")
        print("1. Union")
        print("2. Intersection")
        print("3. Cartesian Product")
        print("4. Sum")
        print("5. Difference (A-B)")
        print("6. Difference (B-A)")
        print("7. Complement of A")
        print("8. Complement of B")
        print("9. Exit")

        try:
            choice=int(input("Enter your Choice (1-9):"))

            if choice == 1 :
                print("Union: ",A.union(B))
            elif choice == 2 :
                print("Intersection:",A.intersection(B))
            elif choice == 3 :
                print("Cartesian Product:",A.cartesian_product(B))
            elif choice == 4 :
                print("Sum:",A.sum(B))
            elif choice == 5:
                print("Difference (A-B):",A.difference(B))
            elif choice == 6:
                 print("Difference (B-A):",B.difference(A))
            elif choice == 7:
                 print(" Complement of A:",A.complement())
            elif choice == 8:
                 print("Complement of B:",B.complement())
            elif choice == 9:
                 print("Exiting...")
                 break
            else:
                print("Not a Choice.Enter a number between 1 and 9.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()



