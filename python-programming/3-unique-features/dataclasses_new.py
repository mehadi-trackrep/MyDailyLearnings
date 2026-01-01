# python dataclasses module example
from dataclasses import dataclass, field
from typing import List

# Define a dataclass with frozen instances and default factory for mutable fields
# A simple immutable data model
@dataclass(frozen=True)
class User:
    id: int
    name: str
    roles: List[str] = field(default_factory=list)

@dataclass
class Product:
    id: int
    name: str
    price: float = 0.0
    in_stock: bool = True

def main():
    # Create instances of the dataclasses
    user1 = User(id=1, name="Alice", roles=["admin", "user"])
    user2 = User(id=2, name="Bob")

    product1 = Product(id=101, name="Laptop", price=999.99)
    product2 = Product(id=102, name="Mouse")

    # Display the instances
    print("user1: ", user1)
    print("user2: ", user2)
    print("product1: ", product1)
    print("product2: ", product2, "\n")

    # Attempting to modify a frozen dataclass will raise an error
    try:
        user1.name = "Charlie"
    except Exception as e:
        print(f"Error: {e}")

    # Modifying a non-frozen dataclass
    product2.price = 19.99
    print("-> product2: ", product2)

    match product1:
        case Product(id=id, name=name, price=price) if price > 500:
            print(f"Expensive product: {name} at ${price}")
        case Product(id=_, name=name):
            print(f"Affordable product: {name}")
        case _:
            print("Unknown product")

if __name__ == "__main__":
    main()